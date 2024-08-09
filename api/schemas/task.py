from typing import Optional
from pydantic import BaseModel, Field
    
class TaskBase(BaseModel):
      title: Optional[str] = Field(None, example="Raise arms x20")

class Task(TaskBase):
    id: int
    done: bool = Field(False, description="done flag")
    class Config:
        orm_mode = True
        
class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskBase):
    id: int
    class Config:
        orm_mode = True