from bson.objectid import ObjectId


class MongoUserRepo:
    def __init__(self, client):
        self.client = client

    async def get_all_users(self) -> list:
        users = []
        for user in await self.client.users.find():
            users.append(user_helper(user))
        return users

    async def get_user(self, user_id: str) -> dict:
        user = await self.client.users.find_one({"_id": ObjectId(user_id)})
        if user:
            return user_helper(user)

    async def add_user(self, user_data: dict) -> dict:
        user = await self.client.users.insert_one(user_data)
        new_user = await self.client.users.find_one({"_id": user.inserted_id})
        return user_helper(new_user)

    async def update_user(self, user_id: str, data: dict) -> bool:
        if len(data) < 1:
            return False
        user = await self.client.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return False
        updated_user = await self.client.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": data}
        )
        return updated_user is not None

    async def delete_user(self, user_id: str) -> bool:
        user = await self.client.users.find_one({"_id": ObjectId(user_id)})
        if user:
            await self.client.users.delete_one({"_id": ObjectId(user_id)})
            return True


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "surname": user["surname"],
        "lastname": user["lastname"],
        "email": user["email"],
        "password": user["password"],
        "position": user["position"],
    }
