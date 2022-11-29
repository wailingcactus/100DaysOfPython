import tkinter

window = tkinter.Tk()
window.title("Miles to km converter")
window.config(padx=20,pady=20)

#Functions

def button_clicked():
    text = float(input.get())
    km_value["text"] = text*1.6

#Entry

input = tkinter.Entry(width=10)
input.grid(column=1,row=0)

#Label

miles_label =tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(column=2, row=0)

km_label =tkinter.Label(text="km", font=("Arial", 12, "bold"))
km_label.grid(column=2, row=1)

equal_label =tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
equal_label.grid(column=0, row=1)

km_value =tkinter.Label(text="0", font=("Arial", 12, "bold"))
km_value.grid(column=1, row=1)



#Button

my_button = tkinter.Button(text="Calculate",command=button_clicked)
my_button.grid(column=1,row=2)




window.mainloop()



