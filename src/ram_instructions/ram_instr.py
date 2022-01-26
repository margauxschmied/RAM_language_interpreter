from tkinter import *
from tkhtmlview import HTMLLabel
import sys


def open_ram_instr(parent):
    window_instr = Toplevel(parent)
    window_instr.title("About")

# Set Geometry
    window_instr.geometry("600x600")

# Add label
    my_label = HTMLLabel(window_instr, html="""
            <i><h2 style="color: red;">RAM INSTRUCTION</h2></i>
            <i>A <b>RAM program</b> is made by 4 instructions:
            <ul>
                <li><b>Rk = Rk + 1</b> which increases the value stock in the register k by one.</li>
                <li><b>Rk = Rk .− 1</b> which decreases the value stock in the register k by one. (NB: if the value in Rk is equal to 0, we have that 0 .− 1 = 0 since
                            RAM machines work in N number set </li>
                <li><b>IF Rk! = 0 T HEN GOT OB n </b> means that if the register k does not
                        equal 0 then RC = RC .−n (here, as before the subtraction is done as
                        follow A .− B = max(0, A − B))</li>
                <li><b>IF Rk! = 0 T HEN GOT OF n </b> which makes the following operation :
                        RC = RC + n</li>
            </ul>
            </i>

            """)
    my_label.pack(pady=20, padx=20)
    window_instr.mainloop()
