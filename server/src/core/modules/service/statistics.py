import logging

from src.core.modules.database.errors import RepoNotFoundError
from src.core.modules.service.errors import SessionNotFoundError


class StatisticsService:
    def __init__(self, repo):
        self.repo = repo

    async def get_all_sessions(self):
        try:
            return await self.repo.get_all_sessions()
        except Exception as e:
            logging.error(f"error getting all sessions: {str(e)}")
            raise

    async def get_session(self, session_id):
        try:
            return await self.repo.get_session(session_id)
        except Exception as e:
            if isinstance(e, RepoNotFoundError):
                logging.error(f"error getting session {session_id}: {str(e)}")
                raise SessionNotFoundError(f"error getting session {session_id}: {str(e)}") from e
            else:
                raise

    async def delete_session(self, session_id):
        try:
            return await self.repo.delete_session(session_id)
        except Exception as e:
            if isinstance(e, RepoNotFoundError):
                logging.error(f"error deleting session {session_id}: {str(e)}")
                raise SessionNotFoundError(f"error deleting session {session_id}: {str(e)}") from e
            else:
                raise

    async def create_session(self, session_data):
        try:
            return await self.repo.add_session(session_data)
        except Exception as e:
            logging.error(f'error creating session data {session_data}: {str(e)}')
            raise Exception(f'error creating session data {session_data}: {str(e)}') from e
