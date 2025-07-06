from pydantic import BaseModel, Field
import barcode
from tkinter import ttk
import tkinter as tk
from PIL import Image
import io
from PIL import ImageTk

class DispLabel(BaseModel):
    proc_order: str = Field(..., description="Process order for the label")
    mat_code: str = Field(..., description="Material code for the label")
    container_id: str = Field(..., description="Container ID for the label")
    def __str__(self):
        return f"{self.proc_order}_{self.mat_code}_{self.container_id}"
    