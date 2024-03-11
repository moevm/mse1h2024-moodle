import os
import motor.motor_asyncio as aio_motor

from src.core.modules.database.statistics import MongoStatisticRepo
from src.core.modules.database.user import MongoUserRepo
from src.core.modules.service.statistics import StatisticsService
from src.core.modules.service.user import UserService

user = os.getenv('MONGODB_INITDB_ROOT_USERNAME')
password = os.getenv('MONGODB_INITDB_ROOT_PASSWORD')

client = aio_motor.AsyncIOMotorClient(f'mongodb://user:pass@mongodb:27017/?authMechanism=DEFAULT')
user_service = UserService(MongoUserRepo(client["moodle-statistics"]))
statistics_service = StatisticsService(MongoStatisticRepo(client["moodle-statistics"]))


def get_user_service() -> UserService:
    return user_service


def get_statistics_service() -> StatisticsService:
    return statistics_service
