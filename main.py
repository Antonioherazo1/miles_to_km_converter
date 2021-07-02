from tkinter import *


def calculate_button():
    pass


# window
window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

# label
isEqualTo_label = Label(text='Is equal to', font=("Arial", 20, "bold"))
isEqualTo_label.grid(column=0, row=1)
isEqualTo_label.config(padx=10, pady=10)

# label
miles_label = Label(text='Miles', font=("Arial", 20, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

# label
km_label = Label(text='Km', font=("Arial", 20, "bold"))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

# result
result_label = Label(text=0, font=("Arial", 20, "bold"))
result_label.grid(column=1, row=1)
result_label.config(padx=40, pady=10)

# Entry
entry = Entry(width=10)
entry.grid(column=1, row=0)


# funtion button

def button_clicked():
    miles_entry = entry.get()
    km_result = int(miles_entry) * 1.609
    result_label.config(text=f'{km_result}')


# button
button = Button(text='Calculate', font=('Arial', 20, 'bold'), command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
