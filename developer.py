from tkinter import*
from tkinter import ttk 
from PIL import Image, ImageTk 
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        
        title_lbl=Label(self.root,text="DEVELOPER INFORMATION",font=("times new roman",30,"bold"),bg="white",fg="hotpink")
        title_lbl.place(x=0,y=0,width=1300,height=45)
        
        img_top=Image.open(r"C:\Users\KIIT\Desktop\FACE_RECOGNITION_SYSTEM\images\dev.jpg")
        img_top= img_top.resize((1290,600), Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=40,width=1290,height=600)
        
        #Frame
        main_frame=Frame (f_lbl, bd=2, bg="white")
        main_frame.place(x=120,y=50, width=300,height=300)
        
        #Developer Info
        dev_label=Label(main_frame,text="Avinash Anand",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=5,y=5)
        
        dev_label=Label(main_frame,text="Bharti Kumari",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=5,y=35)
        
        dev_label=Label(main_frame,text="Kushagra Yadav",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=5,y=65)
        
        dev_label=Label(main_frame,text="Sneha Kumari",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=5,y=95)
        
        dev_label=Label(main_frame,text="Pranjal Kumar",font=("times new roman",13,"bold"),bg="white")
        dev_label.place(x=5,y=125)
        
        
        
        
        
        
        
if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()

