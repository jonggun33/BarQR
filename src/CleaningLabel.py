from pydantic import BaseModel, Field

class CleaningLabel(BaseModel):
    log_id: str = Field(..., description="Log ID for the cleaning label")
    yyyymmdd:str = Field(..., description="Date in YYYYMMDD format for the cleaning label")
    suffix:str = Field(..., description="Suffix for the cleaning label")
    def __str__(self):
        return f"{self.log_id}_{self.yyyymmdd}_{self.suffix}" 