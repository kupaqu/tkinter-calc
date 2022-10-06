import tkinter as tk
import tkinter.ttk as ttk
import numexpr as ne

def click(entry, lbl):
    if lbl == "C":
        entry.delete(0, "end")
    elif lbl == "=":
        expression = entry.get()
        entry.delete(0, "end")
        try:
            evaluated = ne.evaluate(expression)

            # https://docs.python.org/3/tutorial/floatingpoint.html
            if evaluated.dtype == 'float':
                evaluated = round(float(evaluated), 10)
                
            entry.insert(0, evaluated)
        except SyntaxError:
            entry.insert(0, "Syntax error! Clear to continue!")
        except ZeroDivisionError:
            entry.insert(0, "Zero division error! Clear to continue!")
    else:
        entry.insert("end", lbl)

window = tk.Tk() # объект интерфейса
window.title("Calculator") # название окна
window.resizable(0, 0)

main_frame = ttk.Frame(window) # фрейм 
main_frame.grid(sticky='nesw')

calc_input = tk.StringVar()
input_entry = tk.Entry(main_frame, textvariable=calc_input)
input_entry.grid(column=0, row=0, columnspan=4, sticky='nsew')

btn = ['123+', '456-', '789*', 'C0=/']

for i in range(1, 5):
    for j in range(4):
        btn_lbl = btn[i-1][j]
        ttk.Button(main_frame, text=btn_lbl, command=lambda l=btn_lbl, e=input_entry :click(e, l)).grid(column=j, row=i)

main_frame.pack(padx=10, pady=10)
window.mainloop()