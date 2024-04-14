from bson.objectid import ObjectId

from src.core.modules.database.errors import RepoNotFoundError


class MongoStatisticRepo:
    def __init__(self, client):
        self.client = client

    async def get_all_sessions(self, filters) -> list:
        stats = []
        query = {
            'actions': {
                '$elemMatch': {
                    'timestamp': {
                        '$gte': filters.timestamp__gte,
                        '$lte': filters.timestamp__lte
                    }
                }
            }
        }
        for session in await self.client.statistics.find(query).to_list(length=None):
            session["_id"] = str(session["_id"])
            stats.append(session)
        return stats

    async def get_session(self, record_id: str) -> dict:
        stat = await self.client.statistics.find_one({"_id": ObjectId(record_id)})
        if stat:
            stat["_id"] = str(stat["_id"])
            return stat
        raise RepoNotFoundError(f'record {record_id} not found')

    async def add_session(self, session_data: dict) -> dict:
        stat = await self.client.statistics.insert_one(session_data)
        new_stat = await self.client.statistics.find_one({"_id": stat.inserted_id})
        new_stat["_id"] = str(new_stat["_id"])
        return new_stat

    async def delete_session(self, record_id: str):
        stat = await self.client.statistics.find_one({"_id": ObjectId(record_id)})
        if stat:
            return await self.client.statistics.delete_one({"_id": ObjectId(record_id)})
        raise RepoNotFoundError(f'record {record_id} not found')
