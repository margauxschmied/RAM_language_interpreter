# Import Module
from tkinter import *
from tkhtmlview import HTMLLabel
 
# Create Object
root = Tk()
 
# Set Geometry
root.geometry("400x400")
 
# Add label
my_label = HTMLLabel(root, html="""

    <i><h2 style="color: deeppink;">ICONS</h2></i>
<i>In the menu bar you can find some <b>icons</b>, useful to <b>easy accesible</b> some important commands.
<br>let’s see in detail what they are used for:
<b>First icon</b>
<br><img src="images_icons/icon1.png" title="Icon 1" alt="icon_1" >
<br>This icon is used to <b>save</b> the current file. 
<br><br>
<b>Second icon</b>
<img src="icon2.png" title="Icon 2" alt="icnon_2">
<br>The second icon is used to <b>run</b> the file. 
<br><br>
<b>Third icon</b>
<img src="icon3.png" title="Icon 3" alt="icon_3">
<br>It is an other <b>run</b> icon, but this time it is useful to run instrcution by instrcution.
<br><br>
<b>Fourth icon</b>
<img src="icon4.png" title="Icon 4" alt="icon_4">
<br>It allows to <b>stop</b> instrcution by instrcution.
<br>The use of the icon is another quick alternative (the other is the shortcuts) 
to the use of the commands that can be found in the different "File", "Run" and "Stop" sections.</i>





    """)
 
# Adjust label
my_label.pack(pady=20, padx=20)
 
# Execute Tkinter
root.mainloop()

