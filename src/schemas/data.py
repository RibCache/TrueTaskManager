from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CreateTask(BaseModel):
    title: str
    description: str | None = None
    
class TaskRead(CreateTask):
    id: int
    is_completed: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)