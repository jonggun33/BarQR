from pydantic import BaseModel, Field

class HalbLabel(BaseModel):
    batch_id: str = Field(...)
    second:str = Field(...)
    third: str = Field(...)
    def __str__(self):
        return f"{self.batch_id}_{self.second}_{self.third}"