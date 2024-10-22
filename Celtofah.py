from tkinter import *
import tkinter.font as font

root=Tk()
root.geometry("500x250")
root.title("CtoF")

def convert():
    temp_celsius=konichiwa_entry.get()
    if(temp_celsius.replace(".","").isdigit()):
        error_label.grid_forget()
        fahrenheit=(float(temp_celsius)*1.8)+32
        output_label.config(text="Temperature in Fahrenheit: " +str(fahrenheit))
    else:
        error_label.grid(row=1, column=1)

#making GUI

tempcon_label=Label(text="Celsius to fahrenheit converter",font=font.Font(size=20),fg="white")
tempcon_label.pack()

frame=Frame(root)
frame.pack(pady=20)

name_label=Label(frame,text="Enter Temprature to convert to fahrenheit: ",font=font.Font(size=10),fg="white")
name_label.grid(row=0, column=0)

konichiwa_entry=Entry(frame)
konichiwa_entry.grid(row=0, column=1)

error_label=Label(frame,text="Plz enter an valid temprature :)",font=font.Font(size=12),fg="red")

output_label=Label(frame,font=font.Font(size=12),fg="white")
output_label.grid(row=2, column=0, columnspan=2, pady=10)

convert_button=Button(frame,text="Convert",width=30,fg="black",background="light green",bd=0,padx=20,pady=10,command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()