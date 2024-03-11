from fastapi import APIRouter, HTTPException
from starlette import status

from src.core.modules.service.errors import SessionNotFoundError
from src.core.modules.service.statistics import StatisticsService
from src.models.session_data import SessionData

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_sessions(service: StatisticsService):
    try:
        return await service.get_all_sessions()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/{session_id}", status_code=status.HTTP_200_OK)
async def get_session_by_id(service: StatisticsService, session_id):
    try:
        return await service.get_session(session_id)
    except Exception as e:
        if isinstance(e, SessionNotFoundError):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_session(service: StatisticsService, session: SessionData):
    try:
        return await service.create_session(session)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))