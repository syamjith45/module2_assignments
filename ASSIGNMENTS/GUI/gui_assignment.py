# from tkinter import *

# root=Tk()
# root.title('welcome to GUI')
# root.geometry('600x400')
# lbl=Label(root,text="NAME :",fg='blue')
# entry = Entry(root)
# entry.grid(row=0,column=3)

# lbl.grid(row=0, column=0)
# lbl1 = Label(root, text="EMAIL:", fg="blue")
# entry1 = Entry(root)
# entry1.grid(row=1,column=3)
# lbl1.grid(row=1, column=0)
# lbl2 = Label(root, text="PHONE_NO:", fg="blue")
# entry2 = Entry(root)
# entry2.grid(row=2,column=3)
# lbl2.grid(row=2, column=0)
# lbl3 = Label(root, text="ADDRESS:", fg="blue")
# entry3 = Entry(root)
# entry3.grid(row=3,column=3)
# lbl3.grid(row=3, column=0)
# def clicked():
#     print('success')

# btn = Button(root, text="submit", command = clicked)
# btn.place(x=70,y=90)
# root.mainloop()


# import tkinter as tk

# def print_data():
#     user_input = text_entry.get("1.0", "end-1c")
#     print(user_input)

# # Create the main application window
# app = tk.Tk()
# app.title("Data Printer")

# # Create a label to instruct the user
# label = tk.Label(app, text="Enter your data:")
# label.pack()

# # Create a text area where the user can input data
# text_entry = tk.Text(app, height=5, width=30)
# text_entry.pack()

# # Create a button to print the entered data
# print_button = tk.Button(app, text="Print Data", command=print_data)
# print_button.pack()

# # Start the GUI main loop
# app.mainloop()


# ry to configure Label widget with various options like background red and font   with Times New Roman 18 size

import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Label with Custom Styling")

# Configure label with red background and custom font
custom_font = ("Times New Roman", 18)
label = tk.Label(app, text="Custom Styled Label", bg="red", font=custom_font)
label.pack()

# Start the GUI main loop
app.mainloop()
