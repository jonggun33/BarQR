from pydantic import BaseModel, Field

class CleaningLabel(BaseModel):
    log_id: str = Field(..., description="Log ID for the cleaning label")
    expiry:str = Field(..., description="Expiry date for the cleaning label")
    def __str__(self):
        return str(self.model_dump_json() ) 