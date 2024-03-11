from fastapi import APIRouter, HTTPException
from starlette import status

from src.core.modules.service.errors import UserNotFoundError, UserAlreadyExistsError, UserEmptyDataError
from src.core.modules.service.user import UserService

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users(service: UserService):
    try:
        return await service.get_all_users()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(service: UserService, user_id):
    try:
        return await service.get_user(user_id)
    except Exception as e:
        if isinstance(e, UserNotFoundError):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(service: UserService, user_data):
    try:
        return await service.create_user(user_data)
    except Exception as e:
        if isinstance(e, UserAlreadyExistsError):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"User already exists: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(service: UserService, user_id, user_data):
    try:
        return await service.update_user(user_id, user_data)
    except Exception as e:
        if isinstance(e, UserNotFoundError):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Updating user {user_id} failed: {str(e)}")
        elif isinstance(e, UserEmptyDataError):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Updating user {user_id} failed: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(service: UserService, user_id):
    try:
        return await service.delete_user(user_id)
    except Exception as e:
        if isinstance(e, UserNotFoundError):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Deleting user {user_id} failed: {str(e)}")
        else:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
