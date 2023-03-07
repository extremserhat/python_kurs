from tkinter import *
import customtkinter


root = customtkinter.CTk()

def button_fuction():
    print("hallo")

def button_kill():
    root.destroy()

customtkinter.set_appearance_mode("Dark") #other "Light", "System"

# Use CTkButton instead of tkinter button
button = customtkinter.CTkButton(master=root, 
                                 fg_color=("black"),
                                 hover_color=("grey"),
                                 text="press",
                                 corner_radius=15, 
                                 command=button_fuction)
button.place(relx=0.5, rely=0.5, anchor=CENTER)


label = customtkinter.CTkLabel(master=root,
                               text="CTkLabel",
                               width=120,
                               height=25,
                               fg_color=("green"),
                               corner_radius=8)
label.place(relx=3.5, rely=0.5, anchor=CENTER)


root.mainloop()
root.update()


