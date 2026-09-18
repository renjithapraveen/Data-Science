from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("denomination counter")
root.geometry("650x400")
root.configure(bg="light blue")
label1 = Label(root, text="Enter the amount in rupees", font=("Arial", 14), bg="light blue")
label1.place(relx=0.5, y=340, anchor=CENTER)
def msg():
    MsgBox = messagebox.showinfo("denomination counter", "This is a denomination counter application. Enter the amount in rupees and click the button to see the breakdown of denominations.")
    if MsgBox == 'ok':
        topwin()
Button1 = Button(root, text="Click here for instructions", command=msg, font=("Arial", 12), bg="light green")
Button1.place(x=260, y=360)
def topwin():
    top = Toplevel()
    top.title("denomination counter")
    top.geometry("600x450")
    top.configure(bg="light yellow")
    label = Label(top, text="enter total amount :", font=("Arial", 12), bg="light yellow")
    entry = Entry(top)
    lbl = Label(top, text="here are the denominations :", font=("Arial", 12), bg="light yellow")
    l1=Label(top, text="2000", font=("Arial", 12), bg="light yellow")
    l2=Label(top, text="500", font=("Arial", 12), bg="light yellow")
    l3=Label(top, text="200", font=("Arial", 12), bg="light yellow")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculate():
        try:
            global amount 
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note200 = amount // 200
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t1.insert(END ,str(note2000))
            t2.insert(END ,str(note500))
            t3.insert(END ,str(note200))
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer amount.")
    btn = Button(top, text="Calculate", command=calculate, font=("Arial", 12), bg="light green")
    label.place(x=200, y=50)
    entry.place(x=200, y=80)
    lbl.place(x=140, y=160)
    btn.place(x=240, y=120)
    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)
    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)
    top.mainloop()
root.mainloop()