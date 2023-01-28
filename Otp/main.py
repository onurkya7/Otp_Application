from multiprocessing.sharedctypes import Value
import tkinter
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
screen_width = 1920
screen_height = 1080
app.geometry(f"500x450+{(screen_width//2)-300}+{(screen_height//2)-300}") 
app.title("Kamikaze")

def giris():
    if entry_1.get() == "ahmet3434try@outlook.com" and entry_2.get() == "3434":
       messagebox.showinfo("Giris basarili!")
    else: 
       messagebox.showinfo("Hata!", "E-mail ya da parola yanlış")

def hatırla():
    a = entry_1.get() 

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=30, padx=30, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT,text = "E-mail: ")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1,width=150, placeholder_text="examples@outlook.com   ")
entry_1.pack(pady=10, padx=10)

label_2 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT,text = "Parola: ")
label_2.pack(pady=10, padx=10)

entry_2 = customtkinter.CTkEntry(master=frame_1,width=150, placeholder_text="********")
entry_2.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(master=frame_1, command=giris, text="Giriş")
button_1.pack(pady=30, padx=10)

checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text="E-mail Hatırlat")
checkbox_1.pack(pady=12, padx=10)

radiobutton_var = tkinter.IntVar(value=1)

app.mainloop()
