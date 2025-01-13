from tkinter import *

window = Tk()
window.minsize(width=500,height=400)
window.title("Demo Excercise")
window.config(padx=50,pady=50)

labe_name = Label(text="Lable")
labe_name.grid(row=0,column=0)


button_1 = Button(text="New Button")
button_1.grid(row=0,column=2)
button_1.config(padx=5,pady=5)

button_2 = Button(text="Button")
button_2.grid(row=1,column=1)
button_2.config(padx=10,pady=10)

entry1 = Entry()
entry1.grid(row=2,column=3)




window.mainloop()