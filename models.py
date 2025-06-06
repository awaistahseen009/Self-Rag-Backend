from pydantic import BaseModel , Field
from uuid import UUID
class UserQuery(BaseModel):
    query: str = Field(description="User question or query here")
    user_id: UUID = Field(description="User id from the database")
    chat_id: UUID = Field(description= "Current chat id of the user")
