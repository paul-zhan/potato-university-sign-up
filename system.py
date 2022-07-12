from email import message_from_file
from tabnanny import check
import tkinter as tk
from PIL import ImageTk, Image
import tkinter.messagebox
import sqlite3
from database import Database


class Front_page:
    
    check_number = 0 
    database = Database()

    def __init__(self , window):
         self.window = window
        
    # function i made to make shortcut for labels
    def label(self ,label_name, w, text, row, column, padx, pady):
        label_name = tk.Label(w, text=text)
        label_name.grid(row=row, column=column, padx=padx, pady=pady)


    # funtion i made to make a shortut for entries
    def entry(self, entry_name, w ,number1, number2 ):
        entry_name = tk.Entry(w, width=30)
        entry_name.grid(row=number1, column=number2, sticky="W")
        return entry_name


    # display message when the account is created 
    def message(self):
        self.win.destroy()
        tkinter.messagebox.showinfo(title="new account ", message="account created!!")
        

    # doing all the check on all the entry
    def checks(self):
        self.check_number = 0
        # checking the name 
        if isinstance(self.name.get() , (str)) and len(self.name.get())> 0 :
            self.check_number += 1
        else :
            self.warning_name = tk.Label(self.win, text="Please enter your name ", fg= 'red')
            self.warning_name.grid(row=1, column = 3, padx = 10, pady =10)
            self.win.after(2000, lambda :self.warning_name.grid_forget())
            

        if isinstance(self.surname.get(), (str)) and len(self.surname.get())> 0:
            self.check_number += 1
        else :
            self.warning_surname = tk.Label(self.win, text="Please enter your surname ", fg= 'red')
            self.warning_surname.grid(row =2 , column= 3 , padx = 10 , pady = 10)
            self.win.after(2000, lambda :self.warning_surname.grid_forget())
               
        # checking the sex orientation      
        if isinstance(self.sex.get(), (str)) and len(self.sex.get())> 0:
            self.check_number += 1
        else:
            self.warning_sex = tk.Label(self.win, text="please enter your sex ", fg = "red")
            self.warning_sex.grid(row = 4, column = 3, padx = 10, pady =10)
            self.win.after(2000, lambda :self.warning_sex.grid_forget())

        # checking emails
        if "@" in self.email.get(): 
            self.check_number += 1
        else:
            self.warning_email = tk.Label(self.win, text="the email does not contain '@'", fg= 'red')
            self.warning_email.grid(row= 5 , column= 3 , padx = 10 , pady =10 )
            self.win.after(2000, lambda :self.warning_email.grid_forget())

        # checking the age
        if self.age.get().isnumeric() == True:
            self.check_number += 1 
        else :
            self.warning_age = tk.Label(self.win, text="please enter a number", fg = "red")
            self.warning_age.grid(row =3 , column= 3 , padx = 10 , pady = 10)
            self.win.after(2000, lambda :self.warning_age.grid_forget())
        

        # checking the password and the re enter password
        if isinstance(self.password.get(), (str)) and len(self.password.get())> 0 :
            self.check_number += 1  
        else:
            self.warning_password = tk.Label(self.win, text="Please insert a password", fg = "red")
            self.warning_password.grid(row = 7 , column = 3, padx = 10 , pady = 10 )
            self.win.after(2000, lambda :self.warning_password.grid_forget())
            

        if isinstance(self.re_enter_password.get(), (str)) and len(self.re_enter_password.get())> 0:
            if self.password.get() != self.re_enter_password.get():
                self.equal_label = tk.Label(self.win, text="Password different", fg = "red")
                self.equal_label.grid(row = 8 , column = 3 , padx = 20 , pady = 20 )
                self.win.after(2000, lambda :self.equal_label.grid_forget())
            else :
                self.check_number += 1
                
                if self.check_number == 7: 
                    print(f'the check number is :{self.check_number, type(self.check_number)}')
                    self.database_work()
                    self.message()
                else :
                    pass

        else: 
            self.warning_re_enter_password = tk.Label(self.win, text="Please re-enter the password", fg = "red")
            self.warning_re_enter_password.grid(row= 8 , column = 3 , padx=10 , pady = 10 )
            self.win.after(2000, lambda :self.warning_re_enter_password.grid_forget())

        # checking the username 
        # check if there is already the same username in the file once i have the text file 
              
    
    # done
    def new_window(self):

        self.win = tk.Tk()
        self.win.geometry('600x400')
        self.win.title("creating account")
        
        # Label -----------------
        self.label("text", self.win, "Creating a new account", 0, 2, 0, 5)
        self.label("name", self.win, "Name", 1, 1, 10, 10)
        self.label("surname", self.win , "Surname", 2, 1, 10, 10)
        self.label("age", self.win, "Age", 3, 1, 10, 10)
        self.label("sex", self.win, "Sex", 4, 1, 10, 10)
        self.label("email", self.win, "Email", 5,1, 10, 10)
        self.label("username", self.win, "Username ", 6, 1, 10, 10)
        self.label("password", self.win , "Password", 7, 1, 10, 10)
        self.label("re-enter", self.win, "Re-enter the password", 8, 1, 10,10)

        # Entry -----------------
        self.name = self.entry("entry_name", self.win, 1, 2)
        self.surname = self.entry("entry_surname", self.win, 2, 2)
        self.age = self.entry("entry_age", self.win, 3, 2)
        self.sex = self.entry("entry_sex", self.win, 4, 2)
        self.email = self.entry("entry_email" , self.win, 5, 2)
        self.username = self.entry("entry_username", self.win, 6, 2)
        self.password = self.entry("entry_password", self.win ,7, 2)
        self.re_enter_password = self.entry("entry_password_again" ,self.win, 8 , 2)

        # Button -------------------------------------
        button = tk.Button(self.win, text="submit", command= lambda: [self.checks()])
        button.grid(row=9, column=2)
        self.win.mainloop()

    # done
    def drawing(self):
        #------------------------------------- Label --------------
        self.label("username", self.window, "Username", 4, 1, 20, 10)
        self.label("password", self.window, "Password", 6, 1, 20, 10)

        # --------------------------------------Entry -------------
        self.login_username = tk.Entry(width=30)
        self.login_username.grid(row=4, column=2, sticky="W")
        self.login_password = tk.Entry(self.window, show='*', width=30)
        self.login_password.grid(row=6, column=2, sticky="W")

        # --------------------------------------Image----------------
        img = Image.open("potato graduate.png")
        image1 = img.resize((150, 150), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image1)
        image_resized = tk.Label(self.window, image=image, padx=40, pady=40)
        image_resized.grid(row=2, column=2)

        #---------------------------------------- Button---------------------------
        check_button = tk.Checkbutton(self.window, text="show password", command=self.show_password)
        check_button.grid(row=8, column=2)
        submit_button = tk.Button(self.window, text="submit", command=self.submit)
        submit_button.grid(row=9, column=2)
        sign_up_button = tk.Button(self.window, text="sign up", command= self.new_window) 
        sign_up_button.grid(row=10, column=2)
        presentation_text = tk.Label(self.window, text="Welcome to Potato University")
        presentation_text.grid(row=0, column=2)

        self.window.mainloop()

    def show_password(self):
        if self.login_password.cget('show') == '*':
            self.login_password.config(show='')
        else:
            self.login_password.config(show='*')
   

        
    # create a table and insert data 
    def database_work(self):
        self.database.setup()
        self.database.insert_data(self.name.get() , self.surname.get(), self.age.get(), self.sex.get() ,self.email.get(), self.username.get() , self.password.get())



       
    # this is the function that run if the someone click the submit button at the front page 
    def submit(self):
        self.con = sqlite3.connect('user.db')
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM user ")
        self.tuples = self.cur.fetchall()
        self.password_id_tuples = {i[5]: i[6] for i in self.tuples}

        print(self.password_id_tuples)
        if self.login_username.get() in self.password_id_tuples and self.password_id_tuples[self.login_username.get()] == self.login_password.get(): 
            print("welcome to potato university ")
        else:
            self.login_username_warning = tk.Label(self.window, text="username or password are wrong ", fg="red")
            self.login_username_warning.grid(row = 7 , column= 2 , padx = 10 , pady = 10)
            self.window.after(2000, lambda :self.login_username_warning)
  
        
    















