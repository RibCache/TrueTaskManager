from sqlalchemy.ext.asyncio import AsyncSession
from src.models.data import Task
from src.schemas.data import CreateTask
from sqlalchemy import select

async def create_task(db: AsyncSession, task_in: CreateTask) -> Task:
    new_task = Task(**task_in.model_dump())
    
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    
    return new_task

async def get_tasks(db: AsyncSession) -> list[Task]:
    query = select(Task)
    
    result = await db.execute(query)
    
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: int):
    query = select(Task).filter(Task.id == task_id)
    
    result = await db.execute(query)
    
    task = result.scalars().first()
    
    return task
    
    
    
    

    
    