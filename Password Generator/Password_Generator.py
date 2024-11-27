import customtkinter
import string
import random
from customtkinter import *
from tkinter import messagebox

characters = ''
password = ''
ok1=0
ok2=0
ok3=0
def reset():
    global password
    global characters
    global ok1
    global ok2
    global ok3
    characters = ''
    ok1 = 0
    ok2 = 0
    ok3 = 0
    password = ''

def digits():
    global ok1
    global characters
    if check_var1.get() == "on" and ok1<1:
        characters += string.digits
        ok1 = 1

def letters():
    global ok2
    global characters
    if check_var2.get() == "on" and ok2<1:
        characters += string.ascii_letters
        ok2 = 1

def special_characters():
    global ok3
    global characters
    if check_var3.get() == "on" and ok3<1:
        characters += string.punctuation
        ok3 = 1

def generate_pass():
    global password
    pass_length = entry.get()
    if not pass_length.isnumeric():
        messagebox.showerror("Characters","Please introduce a valid number!")
    elif pass_length.isnumeric():
        pass_length=int(pass_length)
        if pass_length>20:
            messagebox.showerror("Length", "Length must be 20 or less!")
        else:
            for i in range(pass_length):
                randomchar = random.choice(characters)
                password += randomchar
            print(password)
            textbox = customtkinter.CTkTextbox(root, font=("Arial", 16, "bold"), height=15, width=300)
            textbox.tag_config("center", justify="center")
            textbox.insert("0.0", f'{password}', "center")
            textbox.configure(state="disabled")
            textbox.place(relx=0.5, rely=0.7, anchor="center")


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("460x460")
root.resizable(height= False, width= False)

root.title("Password Generator")
label = customtkinter.CTkLabel(root, text="Choose what you want in your password:",font=("Arial", 16, "bold"),width=120, height=25,text_color="green")
label.place(relx=0.5,rely=0.1,anchor="center")

check_var1 = customtkinter.StringVar(value="")
checkbox1 = CTkCheckBox(root, checkbox_width=20, checkbox_height=20, text="Digits", variable=check_var1, onvalue="on", offvalue="off", font=("Arial", 16, "bold"), width=25 ,height=25, text_color="green")
checkbox1.place(relx=0.3,rely=0.2,anchor="w")

check_var2 = customtkinter.StringVar(value="")
checkbox2 = CTkCheckBox(root, checkbox_width=20, checkbox_height=20, text="Letters",variable=check_var2, onvalue="on", offvalue="off", font=("Arial", 16, "bold"), width=25 ,height=25, text_color="green")
checkbox2.place(relx=0.3,rely=0.3,anchor="w")

check_var3 = customtkinter.StringVar(value="")
checkbox3 = CTkCheckBox(root, checkbox_width=20, checkbox_height=20, text="Special characters",variable=check_var3, onvalue="on", offvalue="off", font=("Arial", 16, "bold"), width=25 ,height=25, text_color="green")
checkbox3.place(relx=0.3,rely=0.4,anchor="w")

label1 = customtkinter.CTkLabel(root, text="Insert password length (max. 20):",font=("Arial", 16, "bold"),width=120, height=25,text_color="green")
label1.place(relx=0.16,rely=0.5,anchor="w")

entry = customtkinter.CTkEntry(root, height=10, width=50)
entry.place(relx=0.72, rely=0.5, anchor="w")

generate = customtkinter.CTkButton(root, text="Generate", font=("Arial", 16, "bold"), text_color="green", height=30, width=50, hover_color="#1d3630", border_width=2, border_color="green", fg_color="transparent", command=lambda: [reset(), digits(),letters(),special_characters(),generate_pass()])
generate.place(relx=0.5, rely=0.6,anchor="center")

root.mainloop()
