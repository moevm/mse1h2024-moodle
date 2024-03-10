import logging

from src.core.modules.database.errors import RepoNotFoundError
from src.core.modules.service.errors import SessionNotFoundError


class StatisticsService:
    def __init__(self, repo):
        self.repo = repo

    def get_all_sessions(self):
        try:
            return self.repo.get_all_sessions()
        except Exception as e:
            logging.error(f"error getting all sessions: {str(e)}")
            raise

    def get_session(self, session_id):
        try:
            return self.repo.get_session(session_id)
        except Exception as e:
            if isinstance(e, RepoNotFoundError):
                logging.error(f"error getting session {session_id}: {str(e)}")
                raise SessionNotFoundError(f"error getting session {session_id}: {str(e)}") from e
            else:
                raise

    def delete_session(self, session_id):
        try:
            return self.repo.delete_session(session_id)
        except Exception as e:
            if isinstance(e, RepoNotFoundError):
                logging.error(f"error deleting session {session_id}: {str(e)}")
                raise SessionNotFoundError(f"error deleting session {session_id}: {str(e)}") from e
            else:
                raise
