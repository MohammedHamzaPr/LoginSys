import os
try:
    from customtkinter import *
except:
    os.system('pip install customtkinter')
    from customtkinter import *
from tkinter import filedialog,PhotoImage,Frame
from webbrowser import open_new_tab
import PIL.Image
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import *