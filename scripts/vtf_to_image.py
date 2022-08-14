import tkinter as tk
import os

#############################

from tkinter import filedialog
from vtf2img import Parser

#############################

# File dialog
file_path = filedialog.askopenfilename(filetypes=[("Valve texture file", "*.vtf")])

# vtf2img magic
parser = Parser(file_path)
header = parser.header

# Saving the image
image = parser.get_image()
image.save(os.path.basename(file_path).replace(".vtf", ".png")) # Replace PNG if you'd like