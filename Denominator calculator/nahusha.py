from tkinter import  *
from tkinter import messagebox

root= Tk()
root.title("denominator counter")
root.configure(bg='light blue')
root.geometry('600x400')

label1= Label(root, text= 'hey user! welcome to denominator counter', bg= 'light blue')
label1.place(relx= 0.5, y= 340, anchor= CENTER)

def msg():
    msgBox= messagebox.showinfo("Alert", "do you want to continue?")
    if msgBox == 'ok':
        topwin()

button1= Button(root, text= " let's get started!", command= msg, bg= 'light blue')
button1.place(x=260, y=360)

def topwin():
    top= Toplevel()
    top.title("denominations calculator")
    top.configure(bg= 'light grey')
    top.geometry("600x450")

    label= Label(top, text= "enter total amount", bg= 'light grey')
    entry= Entry(top)
    lb1= Label(top, text= "here are number of notes for each denomination", bg= 'light grey')

    l1= Label(top, text= "2000:", bg='light grey')
    l2= Label(top, text= "500:", bg= 'light grey')
    l3= Label(top, text= " 100:", bg='light grey')

    t1= Entry(top)
    t2= Entry(top)
    t3= Entry(top)
    try:
        def calculator():
            global amount
            amount= int(entry.get())
            note2000= amount//2000
            amount%= 2000
            note500= amount//500
            amount%= 500
            note100= amount//100
            amount%= 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

    btn= Button(top, text= "calculate", command=calculator, bg='brown', fg='white')

    label1.place(x=200, y=50)
    entry.place(x=200, y=50)
    btn.place(x=240, y=120)
    lb1.place(x=140, y=170)

    l1.place(x= 180, y= 200)
    l2.place(x= 180, y= 230)
    l3.place(x= 180, y= 260)

    t1.place(x= 270, y=200)
    t2.place(x= 270, y=230)
    t3.place(x= 270, y=260)

    top.mainloop()

root.mainloop()