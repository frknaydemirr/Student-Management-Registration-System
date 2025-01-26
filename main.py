from tkinter import *
from tkinter.ttk import Combobox
from tkinter import  messagebox
from tkinter.filedialog import  askopenfilename
from  PIL import Image, ImageTk
import re
import random
import sqlite3
import os
root=Tk()
root.geometry("500x600")
root.title("Student Management && Registration System")

bg_color="#273b7a"
login_student_icon=PhotoImage(file="student.gif")
login_admin_icon=PhotoImage(file="password-manager.gif")
add_student_icon=PhotoImage(file="user.gif")
locked_icon=PhotoImage(file="lock-_2_.gif")
unlocked_icon=PhotoImage(file="unlocked.gif")
add_student_pic_icon=PhotoImage(file="man-_1_.gif")


def confirmation_box(message):
    answer=BooleanVar()
    answer.set(False)


    def action(ans):
        answer.set(ans)
        confirmation_box_fm.destroy()

    confirmation_box_fm=Frame(root,highlightbackground=bg_color,
                          highlightthickness=3)


    message_lb=Label(confirmation_box_fm,text=message,font=("Bold,15"))
    message_lb.pack(pady=20)

    cancel_button=Button(confirmation_box_fm,text="Cancel",font=("Bold,15"),
                         bd=0,bg=bg_color,fg="white",
                         command=lambda:action(False))

    cancel_button.place(x=50,y=160)

    yes_button = Button(confirmation_box_fm, text="Yes", font=("Bold,15"),
                           bd=0, bg=bg_color, fg="white",
                        command=lambda:action(True))

    yes_button.place(x=190, y=160,width=80)


    confirmation_box_fm.place(x=100,y=120,width=320,height=220)

    root.wait_window(confirmation_box_fm)
    return answer.get()

def message_box(message):
    message_box_fm = Frame(root, highlightbackground=bg_color,
                                highlightthickness=3)

    close_btn=Button(message_box_fm,text="X",bd=0,font=("Bold,13"),
                     fg=bg_color,command=lambda:message_box_fm.destroy())

    close_btn.place(x=280,y=5)
    message_box_fm.place(x=100,y=120,width=320,height=200)

    message_lb=Label(message_box_fm,text=message,font=("Bold,15"))
    message_lb.pack(pady=50)

def welcome_page():

    def forward_to_student_login_page():
        welcome_page_fm.destroy()
        root.update()#change quickly
        student_login_page()


    def forward_to_admin_login_page():
        welcome_page_fm.destroy()
        root.update()
        admin_login_page()

    def forward_to_add_account_page():
        welcome_page_fm.destroy()
        root.update()
        add_account_page()



    welcome_page_fm=Frame(root,highlightbackground=bg_color,
                          highlightthickness=3)

    heading_lb=Label(welcome_page_fm,text="Welcome To Student Registration\n&& Management System",
                    bg=bg_color,fg="white",font=("Bold,18"))

    heading_lb.place(x=0,y=0,width=400)

    student_login_btn=Button(welcome_page_fm,text="Login Student",bg=bg_color,
                             fg="white",font=("Bold",15),bd=0,
                             command=forward_to_student_login_page)

    student_login_btn.place(x=120,y=125,width=200)

    student_login_img=Button(welcome_page_fm,image=login_student_icon,bd=0,
                             command=forward_to_student_login_page)

    student_login_img.place(x=60,y=110)


    admin_login_btn=Button(welcome_page_fm,text="Login Admin",bg=bg_color,
                             fg="white",font=("Bold",15),bd=0,
                           command=forward_to_admin_login_page)

    admin_login_btn.place(x=120,y=225,width=200)

    admin_login_img=Button(welcome_page_fm,image=login_admin_icon,bd=0,
                           command=forward_to_admin_login_page)

    admin_login_img.place(x=60,y=210)


    add_student_btn=Button(welcome_page_fm,text="Create Account",bg=bg_color,
                             fg="white",font=("Bold",15),bd=0,
                           command=forward_to_add_account_page)

    add_student_btn.place(x=120,y=325,width=200)

    add_student_img=Button(welcome_page_fm,image=add_student_icon,bd=0)

    add_student_img.place(x=60,y=310)

    welcome_page_fm.pack(pady=30)
    welcome_page_fm.pack_propagate(False)
    welcome_page_fm.configure(width=400, height=420)

def student_login_page():

    def register_button_clicked():
        response = messagebox.askquestion(title="Save Information", message="Do You Want To Save Your Information?")


        if response.lower() == "yes":
            with open("info.txt", "a", encoding="utf-8") as file:
                file.write(f"Student ID Number:{id_number_ent.get()}\nStudent Password:{password_ent.get()}\n")
        else:
            messagebox.showinfo(title="Save Information", message="Your Information Couldn't Have  Saved!")



    def remove_highlight_warning(entry):
        if entry["highlightbackground"]!="gray":
            if entry.get()!="":
                entry.config(highlightcolor=bg_color,
                                    highlightbackground="gray")

    def password_control(password):
        if len(password) < 8 :
            messagebox.showerror(title="Error⚠️",message="Password Must be at least 8 characters long⚠️")
        elif password.isdigit():
             messagebox.askyesno(title="Password Sequrity Warning⚠️",message="Your password consists only of digits. Are You Sure That Password?⚠️")


    def check_input_validation():
        if id_number_ent.get()=="":
            id_number_ent.config(highlightcolor="red",
                                    highlightbackground="red")
            id_number_ent.focus()
            # message_box(message="Student ID Number is Required!")
            messagebox.askretrycancel(title="Student ID Warning",message="Student ID is Required!")
        if not password_control(password_ent.get()):
            password_ent.config(highlightcolor="red",
                                        highlightbackground="red")
            password_ent.focus()


        elif password_ent.get()=="":
            password_ent.config(highlightcolor="red",
                                 highlightbackground="red")
            password_ent.focus()
            message_box(message="Password is Required To Login!")


    def show_hide_password():
        if password_ent['show']=="*":
            password_ent.configure(show="")
            show_hide_btn.config(image=unlocked_icon)

        else:
            password_ent.configure(show="*")
            show_hide_btn.config(image=locked_icon)

    def forward_to_welcome_page():
        student_login_page_fm.destroy()
        root.update()
        welcome_page()


    student_login_page_fm=Frame(root,highlightbackground=bg_color,
                              highlightthickness=3)




    heading_lb=Label(student_login_page_fm,text="Student Login Page",bg=bg_color,
                     fg="white",font=("Bold,18"))
    heading_lb.place(x=0,y=0,width=400)


    back_btn=Button(student_login_page_fm,text="←",font=("Bold,20"),
                    fg=bg_color,bd=0,command=forward_to_welcome_page)
    back_btn.place(x=5,y=40)


    student_icon_lb=Label(student_login_page_fm,image=login_student_icon)
    student_icon_lb.place(x=150,y=40)

    id_number_lb=Label(student_login_page_fm,text="Enter Student ID Number:",
                       font=("Bold,15"),fg=bg_color)
    id_number_lb.place(x=80,y=140)

    id_number_ent=Entry(student_login_page_fm,font=("Bold,15"),
                        justify=CENTER,highlightcolor=bg_color,
                        highlightbackground="gray",highlightthickness=2)#metindeki yazının başlatılma yönü...
    id_number_ent.place(x=80,y=190)

    id_number_ent.bind("<KeyRelease>", lambda e: remove_highlight_warning(entry=id_number_ent))


    password_lb=Label(student_login_page_fm,text="Enter Student Password:",
                       font=("Bold,15"),fg=bg_color)
    password_lb.place(x=80,y=240)

    password_ent=Entry(student_login_page_fm,show="*",font=("Bold,15"),
                        justify=CENTER,highlightcolor=bg_color,
                        highlightbackground="gray",highlightthickness=2)#metindeki yazının başlatılma yönü...
    password_ent.place(x=80,y=290)

    password_ent.bind("<KeyRelease>", lambda e: remove_highlight_warning(entry=password_ent))

    show_hide_btn=Button(student_login_page_fm,image=locked_icon,bd=0,
                         command=show_hide_password)
    show_hide_btn.place(x=310,y=280)

    login_btn=Button(student_login_page_fm,text="Login",
                     font=("Bold,15"),bg=bg_color,fg="white",
                     command=check_input_validation)
    login_btn.place(x=95,y=340,width=200,height=40)

    register_btn = Button(student_login_page_fm, text="Register",
                       font=("Bold,15"), bg="red", fg="white",
                       command=register_button_clicked)

    register_btn.place(x=300,y=390,width=70,height=40)

    forget_password_btn=Button(student_login_page_fm,text="⚠️\nForget Password",
                               fg=bg_color,bd=0)

    forget_password_btn.place(x=150,y=390)



    student_login_page_fm.pack(pady=30)
    student_login_page_fm.pack_propagate(False)
    student_login_page_fm.configure(width=400, height=450)

def admin_login_page():




    def show_hide_password():
        if password_ent['show']=="*":
            password_ent.configure(show="")
            show_hide_btn.config(image=unlocked_icon)

        else:
            password_ent.configure(show="*")
            show_hide_btn.config(image=locked_icon)

    def forward_to_welcome_page():
        admin_login_page_fm.destroy()
        root.update()
        welcome_page()


    admin_login_page_fm=Frame(root,highlightbackground=bg_color,
                                  highlightthickness=3)

    heading_lb=Label(admin_login_page_fm,text="Admin Login Page",
                     font=("Bold,18"),bg=bg_color,fg="white")
    heading_lb.place(x=0,y=0,width=400)

    back_btn = Button(admin_login_page_fm, text="←", font=("Bold,20"),
                      fg=bg_color, bd=0, command=forward_to_welcome_page)
    back_btn.place(x=5, y=40)

    admin_icon_lb=Label(admin_login_page_fm,image=login_admin_icon)
    admin_icon_lb.place(x=150,y=40)

    username_lb=Label(admin_login_page_fm,text="Enter Admin User Name:",
                           font=("Bold,15"),fg=bg_color)
    username_lb.place(x=80,y=140)

    username_ent=Entry(admin_login_page_fm,font=("Bold,15"),
                        justify=CENTER,highlightcolor=bg_color,
                        highlightbackground="gray",highlightthickness=2)#metindeki yazının başlatılma yönü...
    username_ent.place(x=80,y=190)


    password_lb=Label(admin_login_page_fm,text="Enter Admin Password:",
                           font=("Bold,15"),fg=bg_color)
    password_lb.place(x=80,y=240)

    password_ent=Entry(admin_login_page_fm,show="*",font=("Bold,15"),
                            justify=CENTER,highlightcolor=bg_color,
                            highlightbackground="gray",highlightthickness=2)#metindeki yazının başlatılma yönü...
    password_ent.place(x=80,y=290)

    show_hide_btn=Button(admin_login_page_fm,image=locked_icon,bd=0,
                             command=show_hide_password)
    show_hide_btn.place(x=310,y=280)

    login_btn=Button(admin_login_page_fm,text="Login",
                         font=("Bold,15"),bg=bg_color,fg="white")
    login_btn.place(x=95,y=340,width=200,height=40)

    forget_password_btn = Button(admin_login_page_fm, text="⚠️\nForget Password",
                                 fg=bg_color, bd=0)

    forget_password_btn.place(x=140, y=380)










    admin_login_page_fm.pack(pady=30)
    admin_login_page_fm.pack_propagate(False)
    admin_login_page_fm.configure(width=400, height=430)


student_gender=StringVar()
class_list=['5th','6th','7th','8th','9th','10th','11th','12th']


def add_account_page():
    # pic_path=StringVar()
    # pic_path.set("")
    # def open_pic():
    #     path=askopenfilename()
    #     if path:
    #         img=ImageTk.PhotoImage(Image.open(path).resize((75,75)))
    #         pic_path.set(path)
    #         add_pic_btn.config(image=img)
    #         add_pic_btn.image=img

    def forward_to_welcome_page():

        ans=confirmation_box(message="Do You Want To Leave\nRegisterration Foam?")

        if ans:
            add_account_page_fm.destroy()
            root.update()
            welcome_page()

    def remove_highlight_warning(entry):
        if entry["highlightbackground"]!="gray":
            if entry.get()!="":
                entry.config(highlightcolor=bg_color,
                                    highlightbackground="gray")


    def check_invalid_email(email):
        pattern = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

        match=re.match(pattern=pattern,string=email)

        return match

    def generated_id_number():
        generated_id=""

        for r in range(6):
            generated_id+=str(random.randint(0,9))

        print("id number:",generated_id)
        student_id.config(state=NORMAL)
        student_id.delete(0,END)
        student_id.insert(END,generated_id)
        student_id.config(state="readonly")




    def password_control(password):
        if len(password)<8:
            return False
        if not password.isdigit():
            return False
        return True

    # def email_control(email):
    #     if not email.find("@")==-1:
    #         return False
    #
    #     if not email.isdigit():
    #         return False
    #     return True

    def check_input_validation():
        if student_name_ent.get()=="":
            student_name_ent.config(highlightcolor="red",
                                    highlightbackground="red")
            student_name_ent.focus() #focus metodunun kullanılması, kullanıcının daha kolay ve hızlı bir şekilde gerekli düzeltmeleri yapmasına yardımcı olur.
            message_box(message="Student Full Name Is Requered!")
        elif student_age_ent.get()=="":
            student_age_ent.config(highlightcolor="red",
                                    highlightbackground="red")
            student_age_ent.focus()
            message_box(message="Enter Student Age Is Required!")

        elif not password_control(account_password_ent.get()) :
            account_password_ent.config(highlightcolor="red",
                                    highlightbackground="red")
            account_password_ent.focus()
            messagebox.showerror(title="Error!",message="Your Password Does Not Comply With The Required Rules! ")

        # elif email_control(student_email_ent.get()):
        #     student_email_ent.config(highlightcolor="red",
        #                                 highlightbackground="red")
        #     student_email_ent.focus()
        #     messagebox.showerror("Error!",message="The Student Email Should Include Number And @")

        elif student_contact_ent.get()=="":
            student_contact_ent.config(highlightcolor="red",
                                     highlightbackground="red")
            student_contact_ent.focus()
            message_box(message="Student Contact Num is Required!")

        elif select_class_btn.get()=="":
            select_class_btn.focus()
            message_box(message="Select Student Class is Required!")

        elif student_email_ent.get()=="":
            student_email_ent.config(highlightcolor="red",
                                       highlightbackground="red")
            student_email_ent.focus()
            message_box(message="Student Email Adress is Required!")

        elif not check_invalid_email(email=student_email_ent.get().lower()):
            student_email_ent.config(highlightcolor="red",
                                     highlightbackground="red")
            student_email_ent.focus()
            message_box(message="Please Enter a Valid\nEmail Adress")


        elif account_password_ent.get()=="":
            account_password_ent.config(highlightcolor="red",
                                     highlightbackground="red")
            account_password_ent.focus()
            message_box(message="Create a Password is Required!")

    add_account_page_fm=Frame(root,highlightbackground=bg_color,
                                      highlightthickness=3)

    add_pic_section_fm=Frame(add_account_page_fm,highlightbackground=bg_color,
                                      highlightthickness=2)

    # add_pic_btn=Button(add_pic_section_fm,image=add_student_pic_icon,
    #                    command=open_pic)
    # add_pic_btn.pack()
    add_pic_section_fm.place(x=5,y=5,width=75,height=75)


    student_name_lb=Label(add_account_page_fm,text="Enter Student Full Name:",
                          font=("Bold,12"))
    student_name_lb.place(x=5,y=90)

    student_name_ent=Entry(add_account_page_fm,font=("Bold,15"),
                           highlightcolor=bg_color,highlightbackground="gray",highlightthickness=2)
    student_name_ent.place(x=5,y=120,width=230)
    student_name_ent.bind("<KeyRelease>",lambda e:remove_highlight_warning(entry=student_name_ent))  #student_name_ent adlı giriş kutusuna herhangi bir tuşa basılıp bırakıldığında remove_highlight_warning fonksiyonunun çağrılmasını sağlar. Bu, kullanıcının herhangi bir giriş yaptığında hatalı giriş uyarılarının kaldırılmasını sağlar.


    student_gender_lb=Label(add_account_page_fm,text="Select Student Gender:",
                            font=("Bold,12"))
    student_gender_lb.place(x=5,y=160)

    male_gender_button=Radiobutton(add_account_page_fm,text="Male",
                                   font=("Bold,12"),variable=student_gender,
                                   value="Male")
    male_gender_button.place(x=5,y=190)


    female_gender_button=Radiobutton(add_account_page_fm,text="Famale",
                                   font=("Bold,12"),variable=student_gender,
                                     value="female")
    female_gender_button.place(x=95,y=190)

    student_gender.set("male")

    student_age_lb=Label(add_account_page_fm,text="Enter Student Age:",
                         font=("Bold,12"))
    student_age_lb.place(x=5,y=240)


    student_age_ent=Entry(add_account_page_fm,font=("Bold,15"),
                           highlightcolor=bg_color,highlightbackground="gray",highlightthickness=2)
    student_age_ent.place(x=5,y=270,width=230)

    student_age_ent.bind("<KeyRelease>", lambda e: remove_highlight_warning(entry=student_age_ent))

    student_contact_lb=Label(add_account_page_fm,text="Enter Contact Phone Number:",
                         font=("Bold,12"))
    student_contact_lb.place(x=5,y=320)


    student_contact_ent=Entry(add_account_page_fm,font=("Bold,15"),
                           highlightcolor=bg_color,highlightbackground="gray",highlightthickness=2)
    student_contact_ent.place(x=5,y=360,width=230)

    student_contact_ent.bind("<KeyRelease>", lambda e: remove_highlight_warning(entry=student_contact_ent))


    add_pic_btn=Button(add_pic_section_fm,image=add_student_pic_icon,
                       bd=0)
    add_pic_btn.pack()


    student_class_lb=Label(add_account_page_fm,text="Select Student Class:",
                         font=("Bold,12"))
    student_class_lb.place(x=5,y=420)

    select_class_btn=Combobox(add_account_page_fm,font=("Bold,15"),
                              state="readonly",values=class_list)
    select_class_btn.place(x=5,y=460,width=180,height=30)


    student_id_lb=Label(add_account_page_fm,text="Student ID Number:",
                        font=("Bold,12"))
    student_id_lb.place(x=215,y=25)

    student_id=Entry(add_account_page_fm,font=("Bold,18"),bd=0)
    student_id.place(x=390,y=28,width=70)

    student_id.config(state="readonly")

    generated_id_number()



    id_info_lb=Label(add_account_page_fm,text="""Automatically Generated ID Number
! Remember Using This ID Number
Student will Login Account.""",justify=LEFT)
    id_info_lb.place(x=240,y=65)

    student_email_lb=Label(add_account_page_fm,text="Enter Email Address:",
                         font=("Bold,12"))
    student_email_lb.place(x=240,y=130)


    student_email_ent=Entry(add_account_page_fm,font=("Bold,15"),
                           highlightcolor=bg_color,highlightbackground="gray",highlightthickness=2)
    student_email_ent.place(x=240,y=160,width=200)

    student_email_ent.bind("<KeyRelease>", lambda e: remove_highlight_warning(entry=student_email_ent))

    account_password_lb=Label(add_account_page_fm,text="Create Account Password:",
                              font=("Bold,12"))
    account_password_lb.place(x=220,y=200)

    account_password_ent=Entry(add_account_page_fm,font=("Bold,15"),
                           highlightcolor=bg_color,highlightbackground="gray",highlightthickness=2)
    account_password_ent.place(x=240,y=230,width=200)

    account_password_ent.bind("<KeyRelease>", lambda e: remove_highlight_warning(entry=account_password_ent))

    account_password_info_lb=Label(add_account_page_fm,text="""Via Student Created Student Password
And Provided Student ID Number
Student Can Login Account.""",justify=LEFT)
    account_password_info_lb.place(x=240,y=370)


    home_btn=Button(add_account_page_fm,text="Home",font=("Bold,15"),
                    bg="red",fg="white",bd=0,
                    command=forward_to_welcome_page)
    home_btn.place(x=240,y=450)


    submit_btn=Button(add_account_page_fm,text="Submit",font=("Bold,15"),
                    bg=bg_color,fg="white",bd=0,command=check_input_validation)
    submit_btn.place(x=360,y=450)




    add_account_page_fm.pack(pady=5)
    add_account_page_fm.pack_propagate(False)
    add_account_page_fm.configure(width=480, height=580)

welcome_page()
root.mainloop()
