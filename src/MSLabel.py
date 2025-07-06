from pydantic import BaseModel, Field

class MSLabel(BaseModel):
    mat_code: str = Field(..., description="Material code for the label")
    control_no: str = Field(..., description="Control number for the label")
    def __str__(self):
        return str(self.model_dump_json() )


