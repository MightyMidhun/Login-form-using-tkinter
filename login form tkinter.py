from tkinter import *
from tkinter import messagebox

def clear():
  t1.delete(0,10)
  t2.delete(0,10)


  

def login():
      a=(t1.get())
      b=(t2.get())
      if (a=="root"):
            if (b=="password"):
                  messagebox.showinfo("Login", "Login Successfull")

            else :
                  messagebox.showerror("Error", "Password is wrong")
            
      else :
            messagebox.showerror("Error", "Username is wrong")



top=Tk()

l1=Label(top,text="Enter the username :").grid(row=0,column=0)
l2=Label(top,text="Enter the password").grid(row=1,column=0)
t1=Entry(top,bd=4)
t1.grid(row=0,column=1)
t2=Entry(top,bd=4)
t2.grid(row=1,column=1)

s=Button(top,text="SUBMIT",command=login).grid(row=2,column=0, pady=10)
c=Button(top,text="CLEAR",command=clear).grid(row=2,column=1,pady=10)


mainloop()
