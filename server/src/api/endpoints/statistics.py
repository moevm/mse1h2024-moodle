import datetime
from typing import List

from fastapi import APIRouter, HTTPException, Body, Query
from fastapi.encoders import jsonable_encoder
from starlette import status

from starlette.responses import JSONResponse

from src.core.modules.service.errors import SessionNotFoundError
from src.depends import get_statistics_service
from src.models.filter import SessionFilter
from src.models.session_data import SessionData, CreateSessionData

router = APIRouter()
service = get_statistics_service()


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_description="Get statistics",
    response_model=List[SessionData],
    response_model_by_alias=False
)
async def get_all_sessions(
        begin_timestamp=Query(datetime.datetime(1970, 1, 1, 0, 0, 0, 0).isoformat(), description="start"),
        end_timestamp=Query(datetime.datetime.now().isoformat(), description="stop")
):
    try:
        session_filter = SessionFilter(
            datetime.datetime.fromisoformat(begin_timestamp),
            datetime.datetime.fromisoformat(end_timestamp)
        )
        return await service.get_all_sessions(session_filter)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get(
    "/{session_id}",
    status_code=status.HTTP_200_OK,
    response_description="Get session statistic",
    response_model=SessionData,
    response_model_by_alias=False
)
async def get_session_by_id(session_id: str):
    try:
        return await service.get_session(session_id)
    except Exception as e:
        if isinstance(e, SessionNotFoundError):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_description="Add new session",
    response_model=SessionData,
    response_model_by_alias=False
)
async def create_session(session: CreateSessionData = Body()):
    try:
        session = jsonable_encoder(session)
        session["timestamp"] = datetime.datetime.fromisoformat(session["timestamp"])
        return await service.create_session(session)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete(
    "/{session_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_description="Delete a session statistic",
)
async def delete_session(session_id: str):
    try:
        res = await service.delete_session(session_id)
        if res.deleted_count == 1:
            return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={"message": "Deleted successfully"})
    except Exception as e:
        if isinstance(e, SessionNotFoundError):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Deleting session {session_id} failed: {str(e)}"
            )
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
