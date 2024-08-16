from pydantic import BaseModel
class DoneResponse(BaseModel):
    id: int
    class Connfig:
        orm_mode = True