from tkinter import *
from tkinter import  messagebox
#from pil import image, imgagetk

#main window
root = Tk()
root.title("Denomination counter speaking!")
root.configure(bg="light blue")
root.geometry("650x400")


label1 = Label(root,text="Hey! Welcome to the DENOMINATION COUNTER!")
label1.place(relx=0.5, y=340, anchor=CENTER)

#display messagebox and ok butoon
def msg():
  MsgBox = messagebox.showinfo("Alert", "Do you want to proceed with the denomination?")
  if MsgBox == "ok":
    topwin()
    
#add buttons
button1 = Button(root,text="Let's Get Started!", command=msg, bg="brown", fg="white")
button1.place(x=260, y=360)

#function for opening new window
def topwin():
  top = Toplevel()
  top.title("Denominations Calculator pt.2")
  top.configure(bg="light grey")
  top.geometry("600x450")
  
  label = Label(top, text="Enter total amount", bg="light grey")
  entry = Entry(top)
  lbl = Label(top, text="Enter amount", bg="light grey" )
  l1 = Label(top, text="2000", bg="light grey")
  l2 = Label(top, text="500", bg="light grey")
  l3 = Label(top, text="100", bg="light grey")
  
  t1 = Entry(top)
  t2 = Entry(top)
  t3 = Entry(top)
  
  def calculator():
    try:
      global amount
      amount = int(entry.get())
      note2000 = amount // 2000
      amount %= 2000
      note2000 = amount // 500
      amount %= 500
      note2000 = amount // 100
      amount %= 100
      
      t1.delete(0, END)
      t2.delete(0, END)
      t3.delete(0, END)
      
      t1.insert(END, str(note2000))
      t2.insert(END, str(note500))
      t3.insert(END, str(note100))
    except ValueError:
      messagebox.showerrror("Error", "Please enter a valid input")
  
  btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")
  
  #centring widget
  label.place(x=200, y=50)
  entry.place(x=200, y=80)
  btn.place(x=240, y=120)
  label.place(x=140, y=170)
  
  l1.place(x=180, y=200)
  l2.place(x=180, y=230)
  l3.place(x=180, y=260)
  
  t1.place(x=270, y=200)
  t2.place(x=270, y=230)
  t3.place(x=270, y=260)
  
  top.mainloop()
  
root.mainloop()