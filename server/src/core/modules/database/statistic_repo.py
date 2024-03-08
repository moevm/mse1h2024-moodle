from bson.objectid import ObjectId


class MongoStatisticRepo:
    def __init__(self, client):
        self.client = client

    async def get_all_sessions(self) -> list:
        stats = []
        for session in self.client.statistics.find():
            stats.append(session_data_helper(session))
        return stats

    async def get_session(self, record_id: str) -> dict:
        stat = await self.client.statistics.find_one({"_id": ObjectId(record_id)})
        if stat:
            return session_data_helper(stat)

    async def add_session(self, session_data: dict) -> dict:
        stat = await self.client.statistics.insert_one(session_data)
        new_stat = await self.client.statistics.find_one({"_id": stat.inserted_id})
        return session_data_helper(new_stat)

    async def delete_session(self, record_id: str) -> bool:
        stat = await self.client.statistics.find_one({"_id": ObjectId(record_id)})
        if stat:
            await self.client.statistics.delete_one({"_id": ObjectId(record_id)})
            return True


def session_data_helper(session_data) -> dict:
    return {
        "id": str(session_data["_id"]),
        "student": session_data["student"],
        "group": session_data["group"],
        "email": session_data["email"],
        "course": session_data["course"],
        "session": session_data["session"],
        "actions": session_data["actions"]
    }
