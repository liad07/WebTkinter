# Import tkinter and webview libraries
from tkinter import *
import webview

# Define an instance of tkinter

tk = Tk()

# Size of the window where we show our website
tk.geometry("800x450")

# Open website
webview.create_window('data search', 'http://127.0.0.1:5000')

# Start the webview
webview.start()
