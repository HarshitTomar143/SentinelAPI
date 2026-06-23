from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class FindingResponse(BaseModel):
    id : UUID
    severity: str
    title : str
    description : str
    recommendation : str
    created_at : datetime

class FindingsListResponse(BaseModel):
    success : bool = True
    data : list[FindingResponse]    