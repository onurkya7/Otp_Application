import tkinter
import customtkinter
import random
from smtplib import SMTP
from tkinter import messagebox

def calis():
      # Mail yollama
      kod=str(random.randint(000000,1000000))
      subcjet = "Dogrulama Kodunuz: "
      message = kod
      content = "Subject: {0}\n\n{1}".format(subcjet,message)

      myMailAdress = "ahmet3434try@outlook.com"
      password = "valo3434"
      sendTo = "onur2323den@outlook.com"

      mail = SMTP("smtp.outlook.com", 587)
      mail.ehlo()
      mail.starttls()
      mail.login(myMailAdress,password)
      mail.sendmail(myMailAdress, sendTo, content.encode("utf-8"))
      messagebox.showinfo("Başarılı!","Doğrulama kodu e-mail ile yollandı")

      # Doğrulama ekranı
      customtkinter.set_appearance_mode("white") 
      customtkinter.set_default_color_theme("green")  
      app = customtkinter.CTk("")
      screen_width = 1920
      screen_height = 1080
      app.geometry(f"300x300+{(screen_width//2)}+{(screen_height//2)-200}") 
      app.title("OTP")

      def giris():
         if entry.get() == kod:
            messagebox.showinfo("Başarılı!", "Hoşgeldiniz")
            app.destroy()
         else: 
            messagebox.showinfo("Hata!", "E-mail ya da parola yanlış")

      frame_1 = customtkinter.CTkFrame(master=app)
      frame_1.pack(pady=20, padx=40, fill="both", expand=True)

      label_1 = customtkinter.CTkLabel(master=frame_1, justify=tkinter.LEFT,text = "Kodu girin: ")
      label_1.pack(pady=10, padx=10)

      entry = customtkinter.CTkEntry(master=frame_1, placeholder_text="4CSAQ")
      entry.pack(pady=10, padx=10)

      button_1 = customtkinter.CTkButton(master=frame_1, command=giris, text="Giriş")
      button_1.pack(pady=30, padx=10)

      radiobutton_var = tkinter.IntVar(value=1)

      app.mainloop()


