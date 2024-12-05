import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sorting Algorithms Visualizer")

def selected_option():


frame = ttk.Frame(root, width=100, height=200)
frame.grid(row=0, column=0)
frame.pack(side="left", padx=10)

start_button = ttk.Button(frame, text="START")
start_button.grid(row=0, column=0)

pause_button = ttk.Button(frame, text="PAUSE")
pause_button.grid(row=1, column=0)

resume_button = ttk.Button(frame, text="RESUME")
resume_button.grid(row=2, column=0)

stop_button = ttk.Button(frame, text="STOP")
stop_button.grid(row=3, column=0)

reset_button = ttk.Button(frame, text="RESET")
reset_button.grid(row=4, column=0)

shuffle_button = ttk.Button(frame, text="SHUFFLE")
shuffle_button.grid(row=5, column=0)

exit_button = ttk.Button(frame, text="EXIT", command=root.destroy)
exit_button.grid(row=6, column=0)

sorting_choose = ttk.Label(frame, text="Choose sorting algorithm")
sorting_choose.grid(row=7, column=0)

sorting_list = ["Bubble Sort","Stupid Sort"]
sorting_box = ttk.Combobox(frame, values=sorting_list)
sorting_box.grid(row=8, column=0)

number_of_elements = ttk.Label(frame, text="Set number of elements")
number_of_elements.grid(row=9, column=0, columnspan=1)

number_of_elements_entry = ttk.Entry(frame, width=5)
number_of_elements_entry.grid(row=10, column=0)

set_button_elements = ttk.Button(frame, text="SET")
set_button_elements.grid(row=11, column=0, pady=5)

delay_set = ttk.Label(frame, text="Set delay time")
delay_set.grid(row=12, column=0)

delay_entry = ttk.Entry(frame, width=5)
delay_entry.grid(row=13, column=0)

set_button_delay = ttk.Button(frame, text="SET")
set_button_delay.grid(row=14, column=0, pady=5)

canvas = tk.Canvas(root, width=600, height=600, bg="black")
canvas.pack(padx=5, pady=5)

root.mainloop()