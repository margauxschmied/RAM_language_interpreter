from tkinter import *
from tkhtmlview import HTMLLabel
from main import *
import sys

def open_about(self):
        window = tk.Toplevel(self.panel)
        window.title("About")
 
    # Set Geometry
        window.geometry("400x400")
 
    # Add label
        my_label = HTMLLabel(window, html="""
            <i><h2 style="color:blue">ABOUT</h2></i>
            <i>This project has been realized by a group of four student : Fissore Davide, Schmied Margaux, Venturelli Antoine, three students of the University of Côte d'Azur of Nice
            and Federica Galbiati, an Erasmus student coming from the University Bicocca of Milan.</i>

            """)
        my_label.pack(pady=20, padx=20)
        window.mainloop()