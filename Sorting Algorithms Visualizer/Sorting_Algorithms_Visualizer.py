import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import random

root = tk.Tk()
root.title("Sorting Algorithms Visualizer")
root.resizable(False, False)
data = []
shuffled = False
predefined_elements = [8,16,32,64,128,256,512]
seted_delay = -1
sort_algorithm = ''
paused = False
stopped = False

def resume():
    global paused
    paused = False
    pause_button.config(state="enabled")
    resume_button.config(state="disabled")

def pause():
    global paused
    paused = True
    pause_button.config(state="disabled")
    resume_button.config(state="enabled")

def stop():
    global stopped
    global paused
    stopped = True
    paused = False
    enable_buttons()
    pause_button.config(state="disabled")
    resume_button.config(state="disabled")
    start_button.config(state="disabled")
    shuffle_button.config(state="disabled")

def reset():
    global data
    global shuffled
    global paused
    global stopped
    shuffled = False
    paused = False
    stopped = False
    data = []
    canvas.delete("all")
    draw_bars()
    enable_buttons()
    pause_button.config(state="enabled")
    resume_button.config(state="disabled")
    number_of_elements_combobox.set(16)
    delay_combobox.set(50)

def sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def get_delay_input():
    global seted_delay
    seted_delay = int(delay_combobox.get())

def disable_buttons():
    start_button.config(state="disabled")
    shuffle_button.config(state="disabled")
    reset_button.config(state="disabled")
    set_button_elements.config(state="disabled")
    set_button_delay.config(state="disabled")

def enable_buttons():
    start_button.config(state="enabled")
    shuffle_button.config(state="enabled")
    reset_button.config(state="enabled")
    set_button_elements.config(state="enabled")
    set_button_delay.config(state="enabled")

def draw_bars():
    global shuffled
    canvas.delete("all")
    num_bars = int(number_of_elements_combobox.get())
    canvas_width = int(canvas["width"])
    canvas_height = int(canvas["height"])
    bar_width = canvas_width // num_bars
    heights = [i * canvas_height / num_bars for i in range(1, num_bars + 1)]
    for i, height in enumerate(heights):
        x0 = i * bar_width + 2
        y0 = canvas_height - height +2
        x1 = x0 + bar_width
        y1 = canvas_height + 2
        if num_bars>128:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white",outline="")
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
    shuffled = False

def shuffle_bars():
    global data
    global shuffled
    num_bars = int(number_of_elements_combobox.get())
    canvas_width = int(canvas["width"])
    canvas_height = int(canvas["height"])
    data = [i * canvas_height / num_bars for i in range(1, num_bars + 1)]
    random.shuffle(data)
    shuffled = True
    canvas.delete("all")
    bar_width = canvas_width // num_bars
    for i, height in enumerate(data):
        x0 = i * bar_width + 2
        y0 = canvas_height - height +2
        x1 = x0 + bar_width
        y1 = canvas_height + 2
        if num_bars>128:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white",outline="")
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")

def bubble_sort_visual(heights, bar_width, canvas_width, canvas_height, i=0, j=0):
    global seted_delay
    global shuffled
    global paused
    global stopped
    n = len(heights)
    if stopped:
        enable_buttons()
        start_button.config(state="disabled")
        shuffle_button.config(state="disabled")
        return
    if paused:
        root.after(seted_delay, bubble_sort_visual, heights, bar_width, canvas_width, canvas_height, i, j)
        return
    if i >= n - 1:
        for k, height in enumerate(heights):
            x0 = k * bar_width + 2
            y0 = canvas_height - height + 2
            x1 = x0 + bar_width
            y1 = canvas_height + 2
            if n>128:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#90EE90", outline="")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#90EE90", outline="black")
            root.update_idletasks()
            root.after(10)
        shuffled = False
        enable_buttons()
        return
    if j < n - 1 - i:
        canvas.delete("all")
        for k, height in enumerate(heights):
            x0 = k * bar_width + 2
            y0 = canvas_height - height + 2
            x1 = x0 + bar_width
            y1 = canvas_height + 2
            if k == j or k == j + 1:
                if n>128:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="black")
            else:
                if n>128:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
        root.update_idletasks()
        root.after(seted_delay)
        if heights[j] > heights[j + 1]:
            heights[j], heights[j + 1] = heights[j + 1], heights[j]
            canvas.delete("all")
            for k, height in enumerate(heights):
                x0 = k * bar_width + 2
                y0 = canvas_height - height + 2
                x1 = x0 + bar_width
                y1 = canvas_height + 2
                if k == j or k == j + 1:
                    if n > 128:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", outline="")
                    else:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", outline="black")
                else:
                    if n > 128:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="")
                    else:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
        root.update_idletasks()
        root.after(seted_delay)
        root.after(seted_delay, bubble_sort_visual, heights, bar_width, canvas_width, canvas_height, i, j + 1)
    else:
        root.after(seted_delay, bubble_sort_visual, heights, bar_width, canvas_width, canvas_height, i + 1, 0)


def selection_sort_visual(heights, bar_width, canvas_width, canvas_height, i=0, j=None, min_idx=None):
    global seted_delay
    global shuffled
    n = len(heights)
    if stopped:
        enable_buttons()
        start_button.config(state="disabled")
        shuffle_button.config(state="disabled")
        return
    if paused:
        root.after(seted_delay, selection_sort_visual, heights, bar_width, canvas_width, canvas_height, i, j, min_idx)
        return
    if min_idx is None:
        min_idx = i
    if j is None:
        j = i + 1
    if i >= n - 1:
        for k, height in enumerate(heights):
            x0 = k * bar_width + 2
            y0 = canvas_height - height + 2
            x1 = x0 + bar_width
            y1 = canvas_height + 2
            if n > 128:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
        for k, height in enumerate(heights):
            x0 = k * bar_width + 2
            y0 = canvas_height - height + 2
            x1 = x0 + bar_width
            y1 = canvas_height + 2
            if n>128:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#90EE90", outline="")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#90EE90", outline="black")
            root.update_idletasks()
            root.after(10)
        enable_buttons()
        shuffled = False
        return
    if j < n:
        canvas.delete("all")
        for k, height in enumerate(heights):
            x0 = k * bar_width + 2
            y0 = canvas_height - height + 2
            x1 = x0 + bar_width
            y1 = canvas_height + 2
            if k == j or k == min_idx:
                if n > 128:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="red", outline="black")
            else:
                if n > 128:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="")
                else:
                    canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
        root.update_idletasks()
        root.after(seted_delay)
        if heights[j] < heights[min_idx]:
            min_idx = j
        root.after(seted_delay, selection_sort_visual, heights, bar_width, canvas_width, canvas_height, i, j + 1,min_idx)
    else:
        if min_idx != i:
            heights[i], heights[min_idx] = heights[min_idx], heights[i]
            canvas.delete("all")
            for k, height in enumerate(heights):
                x0 = k * bar_width + 2
                y0 = canvas_height - height + 2
                x1 = x0 + bar_width
                y1 = canvas_height + 2
                if k == i or k == min_idx:
                    if n > 128:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", outline="")
                    else:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="yellow", outline="black")
                else:
                    if n > 128:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="")
                    else:
                        canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
            root.update_idletasks()
            root.after(seted_delay)
        root.after(seted_delay, selection_sort_visual, heights, bar_width, canvas_width, canvas_height, i + 1, None, None)

def bogo_sort_visual(data, bar_width, canvas_width, canvas_height):
    global seted_delay
    global stopped
    global paused
    global shuffled
    n = len(data)
    if stopped:
        enable_buttons()
        start_button.config(state="disabled")
        shuffle_button.config(state="disabled")
        return
    if paused:
        root.after(seted_delay, bogo_sort_visual, data, bar_width, canvas_width, canvas_height)
        return
    canvas.delete("all")
    for i, height in enumerate(data):
        x0 = i * bar_width + 2
        y0 = canvas_height - height + 2
        x1 = x0 + bar_width
        y1 = canvas_height + 2
        if n > 128:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="")
        else:
            canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black")
    root.update_idletasks()
    root.after(seted_delay)
    if sorted(data):
        canvas.delete("all")
        for i, height in enumerate(data):
            x0 = i * bar_width + 2
            y0 = canvas_height - height + 2
            x1 = x0 + bar_width
            y1 = canvas_height + 2
            if n>128:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#90EE90", outline="")
            else:
                canvas.create_rectangle(x0, y0, x1, y1, fill="#90EE90", outline="black")
        shuffled = False
        root.update_idletasks()
        enable_buttons()
        return
    else:
        random.shuffle(data)
        root.after(seted_delay, bogo_sort_visual, data, bar_width, canvas_width, canvas_height)

def start_algorithm():
    global data
    global shuffled
    global seted_delay
    global sort_algorithm
    global stopped
    sort_algorithm = sorting_box.get()
    disable_buttons()
    if not shuffled:
        msgbox.showerror("Not Shuffled", "Please press SHUFFLE button before!")
        enable_buttons()
        return
    if seted_delay == -1:
        msgbox.showerror("The delay has not been set", "Please set a delay")
        enable_buttons()
        return
    num_bars = int(number_of_elements_combobox.get())
    canvas_width = int(canvas["width"])
    canvas_height = int(canvas["height"])
    bar_width = canvas_width // num_bars
    canvas.delete("all")
    if sort_algorithm == "Bubble Sort":
        bubble_sort_visual(data, bar_width, canvas_width, canvas_height)
    elif sort_algorithm == "Selection Sort":
        selection_sort_visual(data, bar_width, canvas_width, canvas_height)
    elif sort_algorithm == "Bogo Sort":
        bogo_sort_visual(data, bar_width, canvas_width, canvas_height)


frame = ttk.Frame(root, width=100, height=200)
frame.grid(row=0, column=0)
frame.pack(side="left", padx=10)

start_button = ttk.Button(frame, text="START",command=start_algorithm)
start_button.grid(row=0, column=0)

pause_button = ttk.Button(frame, text="PAUSE", command=pause)
pause_button.grid(row=1, column=0)

resume_button = ttk.Button(frame, text="RESUME",command=resume)
resume_button.config(state="disabled")
resume_button.grid(row=2, column=0)

stop_button = ttk.Button(frame, text="STOP", command=stop)
stop_button.grid(row=3, column=0)

reset_button = ttk.Button(frame, text="RESET", command=reset)
reset_button.grid(row=4, column=0)

shuffle_button = ttk.Button(frame, text="SHUFFLE", command=shuffle_bars)
shuffle_button.grid(row=5, column=0)

exit_button = ttk.Button(frame, text="EXIT", command=root.destroy)
exit_button.grid(row=6, column=0)

sorting_choose = ttk.Label(frame, text="Choose sorting algorithm")
sorting_choose.grid(row=7, column=0)

sorting_box = ttk.Combobox(frame, values=["Bubble Sort","Selection Sort","Bogo Sort"], state="readonly")
sorting_box.set("Bubble Sort")
sorting_box.grid(row=8, column=0)

number_of_elements = ttk.Label(frame, text="Set number of elements")
number_of_elements.grid(row=9, column=0, columnspan=1)

number_of_elements_combobox = ttk.Combobox(frame,width=5, values=[4,8, 16, 32, 64, 128, 256, 512], state="readonly")
number_of_elements_combobox.set(16)
number_of_elements_combobox.grid(row=10, column=0)

set_button_elements = ttk.Button(frame, text="SET", command=draw_bars)
set_button_elements.grid(row=11, column=0, pady=5)

delay_set = ttk.Label(frame, text="Set delay time (in ms)")
delay_set.grid(row=12, column=0)

delay_combobox = ttk.Combobox(frame, width=5, values=[1,10,20,30,40,50,60,70,80,90,100,200,300,400,500,1000], state="readonly")
delay_combobox.set(50)
delay_combobox.grid(row=13, column=0)

set_button_delay = ttk.Button(frame, text="SET", command=get_delay_input)
set_button_delay.grid(row=14, column=0, pady=5)

canvas = tk.Canvas(root, width=512, height=512, bg="black")
canvas.pack(padx=5, pady=5)

draw_bars()
get_delay_input()
root.mainloop()