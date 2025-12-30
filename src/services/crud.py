from sqlalchemy.ext.asyncio import AsyncSession
from src.models.task import Task
from src.schemas.task import CreateTask, UpdateTask
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

async def get_task_by_id(db: AsyncSession, task_id: int) -> Task:
    query = select(Task).filter(Task.id == task_id)
    
    result = await db.execute(query)
    
    task = result.scalars().first()
    
    return task

async def update_task(db: AsyncSession, task_id: int, task_update: UpdateTask) -> Task | None:
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    
    if task is None:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(task, key, value)
        
    await db.commit()
    await db.refresh(task)
    return task
    
async def delete_task(db: AsyncSession, task_id: int) -> bool:
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()
    
    if task is None:
        return False
    
    await db.delete(task)
    await db.commit()
    return True
    
    
    
    
    

    
    