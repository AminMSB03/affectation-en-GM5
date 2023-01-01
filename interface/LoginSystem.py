import tkinter as tk
from tkinter import *
import tkinter.font as font
import os





checkboxes2 = []
checkboxes2KV = []

checkboxes1 = []
checkboxes1KV = []


def main_acc():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x260")
    main_screen.title("Main")
    Label(text="Login or Register", bg="#b1abf1", fg="white",
          width="300", height="2", font=("Calibri", 13)).pack(padx=20, pady=23 )
    Button(text="LOGIN", height="2", width="15", fg="#c0ecc0",command=login).pack(padx=1, pady=20)
    Button(text="REGISTER", height="2", width="15",fg="#D8BFD8", command=register).pack(padx=1, pady=5)
    main_screen.mainloop()

def register():
    main_screen.destroy()
    global register_screen
    register_screen = Tk()
    register_screen.title("Register")
    register_screen.geometry("320x350")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Enter Details Below to Login!",bg="#D8BFD8", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(register_screen, text="").pack()

    unLabel = Label(register_screen, text="Username",fg="black", bg="#D8BFD8")
    unLabel.pack(pady=5)

    unEntry = Entry(register_screen, textvariable=username)
    unEntry.pack()

    passLabel = Label(register_screen, text="Password",fg="black" , bg="#D8BFD8")
    passLabel.pack(pady=5)

    passEntry = Entry(register_screen,textvariable=password, show='*')
    passEntry.pack()

    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, fg="black", command=register_user).pack()

def login():
    main_screen.destroy()
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("320x350")
    Label(login_screen,text="Enter Details Below to Login!",bg="#c0ecc0", fg="black",
          width="300", height="2",font=("Calibri", 13)).pack(padx=20, pady=23 )
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username",fg="black", bg="#c0ecc0").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack(pady=5)

    Label(login_screen, text="").pack()
    Label(login_screen, text="Password",fg="black", bg="#c0ecc0").pack(pady=5)

    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login",width=10,fg="black" ,height=1, command=login_verify).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()

    if username1 in list_of_files:
        with open(username1, "r") as f:
            if password1 in f:
                login_sucess()
            else:
                password_not_recognised()
    else:
        user_not_found()







def login_sucess():
    login_screen.destroy()
    global login_success_screen
    login_success_screen = Tk()
    login_success_screen.title("AFFECTATIONS - GUI")
    login_success_screen.geometry("900x800")

    frame1 = Frame(login_success_screen,width=900,height=200)
    frame1.grid(row=0,column=0)

    frame1_1 = Frame(frame1,width=700,height=200)
    frame1_1.grid(row=0, column=0)

    myFont = font.Font(family='Helvetica', size=12, weight='normal')

    label1 = Label(frame1_1, text="Classez vos voeux par ordre de préference:",fg="#4c6085",font='Helvetica 15 underline')
    label1['font'] = myFont
    label1.place(relx=0.5, rely=0.4, anchor=CENTER)

    label2 = Label(frame1_1, text="- Cochez les cases dans ror&e de préférence voulu", fg="#4c6085")
    label2['font'] = myFont
    label2.place(relx=0.5, rely=0.5, anchor=CENTER)

    label3 = Label(frame1_1, text="- Tout validation est définitive", fg="#4c6085")
    label3['font'] = myFont
    label3.place(relx=0.5, rely=0.6, anchor=CENTER)



    frame1_2 = Frame(frame1, width=200, height=150)
    frame1_2.grid(row=0, column=1)

    button = Button(frame1_2, text='Valid', bg='#52528c', fg='#ffffff',width=10,command=get_selections)
    button['font'] = myFont
    button.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Create the frame with a border thickness of 5 pixels
    frame2 = tk.Frame(login_success_screen, width=900, height=650)
    frame2.grid(row=1, column=0)

    frame4 =  tk.Frame(frame2,width=450,height=650,bd=5)
    frame4.grid(row=0, column=0)

    ## the title
    label2 = Label(frame4, text="Parcours 1 : ", fg="#4c6085")
    label2['font'] = myFont
    label2.place(relx=0.2, rely=0, anchor=NE,relwidth=1)


    x=IntVar()
    def display():
        print(x.get())


    for i in range(1,8):
        check_button = Checkbutton(frame4,text=f"O1.{i+1}",variable=x, onvalue=i, command=display)
        check_button.place(relx=0, rely=i * 0.05)


    frame5 = tk.Frame(frame2,width=450,height=650, bd=5)
    frame5.grid(row=0, column=1)

    frame5_1 = tk.Frame(frame5, width=450, height=50, bd=5,bg="red")
    frame5_1.grid(row=0, column=0)

    frame5_2 = tk.Frame(frame5, width=450, height=600, bd=5,bg="blue")
    frame5_2.grid(row=1, column=0)




    label2 = Label(frame5_1, text="Parcours 2 : ", fg="#4c6085")
    label2['font'] = myFont
    label2.place(relx=0.2, rely=0.01, anchor=NE)


    def display():
        # change the color of the selected checkboxes to red
        for cb, var in checkboxes2KV:
            if var.get() == 1:
                cb.config(fg='red')
                if cb.cget("text") not in checkboxes2:
                    checkboxes2.append(cb.cget("text"))



    for i in range(10):
        var = tk.IntVar()
        cb = tk.Checkbutton(frame5_2, text=f"Option {i + 1}", variable=var,command=display)
        checkboxes2KV.append((cb, var))
        cb.place(relx=0, rely=i * 0.08)








def get_selections():
    print(checkboxes2)


def on_click(self):
    selected_options = []
    for checkbox, var in self.checkboxes:
        if var.get() == 1:
            selected_options.append(checkbox["text"])
    print(selected_options)




def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("ERROR")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("ERROR")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen,fg="red", text="User Not Found!").pack(pady=20)
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()

main_acc()

