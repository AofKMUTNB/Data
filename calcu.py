import tkinter as tk
from tokenize import Number

def show_output():
    number = int(number_input.get())

    output = ''
    for i in range(1,13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)
    if number == 0:
        output_label.configure(text='ไม่ได้')
    return

window = tk.Tk()
window.title('AofStudy')
window.minsize(width=400, height=400)

title_label = tk.Label(master=window,text='สูตรคูณ')
title_label.pack(pady=20)

number_input = tk.Entry(master=window ,width=50)
number_input.pack()

go_button = tk.Button(master=window,text='ได้แก่',command=show_output, width=5 , height=2)
go_button.pack(pady=20)

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()