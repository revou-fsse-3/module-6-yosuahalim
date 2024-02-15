from pydantic import BaseModel, Field


class update_user_request(BaseModel):
    name: str = Field(..., description="User Name", min_length=3, max_length=255)
