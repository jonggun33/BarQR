from pydantic import BaseModel, Field
import barcode
from tkinter import ttk
import tkinter as tk
from PIL import Image
import io
from PIL import ImageTk

class DispLabel(BaseModel):
    scan_type: str = Field(..., description="Type of scan for the label")
    charg:str = Field(..., description="Charge number for the label")
    matnr:str = Field(..., description="Material number for the label")
    ccharge:str =Field(...)
    rsnum: str = Field(...)
    disp_id: str = Field(...)
    cont_sel: str = Field(...)
    cont_amt: str = Field(...)
    cont_tot: str = Field(...)
    vfdat: str = Field(...)
    aufnr: str = Field(...)
    vornr: str = Field(...)
    mesid: str = Field(...)

    def __str__(self):
        return str(self.model_dump_json())
    