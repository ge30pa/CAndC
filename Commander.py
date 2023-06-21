from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry('500x140')
root.resizable(0,0)
root.configure(bg="black")
canvas = Canvas(root,width=500,height=100)
canvas.pack()
canvas.configure(bg="black")
pilImage = Image.open("logo.gif")
image = ImageTk.PhotoImage(pilImage)
imagesprite = canvas.create_image(250,50,image=image)


#sysinfobutton
sysinfo = Button(root, text="SysInfo")
sysinfo.place(y=105,x=125)

#Payloadsbutton
payloads = Button(root, text="Payloads")
payloads.place(y=105,x=55)

#serverbutton
startserver = Button(root, text="Server")
startserver.place(y=105, x=2)

#exitbutton
getout = Button(root, text="Exit",command= root.destroy)
getout.place(y=105, x=468)

root.mainloop()