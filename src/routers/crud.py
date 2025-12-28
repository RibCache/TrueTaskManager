from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.schemas.data import CreateTask, TaskRead
from src.models.data import Task
from src.services import crud
from src.db.database import get_async_session

router = APIRouter(
    prefix="/tasks",
    tags=['Tasks']
)

@router.post('/', response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_new_task(
    task_data: CreateTask,
    db: AsyncSession = Depends(get_async_session)
):
    return await crud.create_task(db=db, task_in=task_data)

@router.get('/', response_model=List[TaskRead])
async def get_all_tasks(
    db: AsyncSession = Depends(get_async_session)
):

    return await crud.get_tasks(db=db)

@router.get("/{task_id}", response_model=TaskRead)
async def task_by_id(
    task_id: int,
    db: AsyncSession = Depends(get_async_session)
):
    task = await crud.get_task_by_id(db, task_id)
    
    if task is None:
        raise HTTPException(status_code=404)

    return task