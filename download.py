from tkinter import *
import tkinter as tk
from pytube import YouTube

root=Tk()
root.geometry("1100x550")
root.title("Youtube Video Downloader")
root.resizable(False,False)
root.config(bg="light blue")

def download():
    link=textfield.get()
    YouTube(f'{link}').streams.first().download()

label1=Label(root,text="Download Youtube Videos for Free",font=('aerial',18),background="light blue",foreground="black")
label1.pack(padx=5,pady=15,side=TOP)

label2=Label(root,text="Enter Link for the youtube video",font=('aerial',18),background="light blue",foreground="black")
label2.place(x=700,y=190)

Search_image=PhotoImage(file=("search.png"))
myimage=Label(image=Search_image,bg="light blue")
myimage.place(x=640,y=220)

description=PhotoImage(file="Opera_Snapshot_2024-07-01_024835_www.vecteezy.com-removebg-preview.png")
label3=Label(image=description,bg="light blue")
label3.place(x=10,y=50)

textfield=tk.Entry(root,justify="center",width=20,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=700,y=240)
textfield.focus()

download=PhotoImage(file="icons8-download-64.png")
myimage_icon=Button(image=download,borderwidth=0,cursor="hand2",bg="light blue",fg="white",command=download)
myimage_icon.place(x=980,y=320)

root.mainloop()

