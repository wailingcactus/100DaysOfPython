import tkinter

window = tkinter.Tk()
window.title("First program")
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)

#Functions

def button_clicked():
    text = input.get()
    my_label["text"] = text

#Label

my_label =tkinter.Label(text="Test Label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0,row=0)

my_label["text"] = "New Text"

#Button

my_button = tkinter.Button(text="Click here",command=button_clicked)
my_button.grid(column=1,row=1)

my_button2 = tkinter.Button(text="Click here 2",command=button_clicked)
my_button2.grid(column=2,row=0)
#Entry

input = tkinter.Entry(width=10)
input.grid(column=3,row=3)


window.mainloop()



