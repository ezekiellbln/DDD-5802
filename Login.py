from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


#Login functionality
def login():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif UsernameEntry.get()=='Kiel' and PasswordEntry.get()=='123':
        messagebox.showinfo('Success','Welcome!')
        window.destroy()
        import StudentData
    else:
        messagebox.showerror('Error','Incorrect Username/Password')

#Window
window = Tk()
window.geometry('1280x700+50+0')
window.title('Student Database System')
window.resizable(False,False)

#GUI
BackgroundImage = ImageTk.PhotoImage(file = 'bg.jpg')
BGLabel = Label(window, image = BackgroundImage)
BGLabel.place(x = 0, y = 0)

LoginFrame = Frame(window)
LoginFrame.place(x = 400,y = 150)

LogoImage = PhotoImage(file = 'logo.png')

LogoLabel = Label(LoginFrame, image = LogoImage)
LogoLabel.grid(row =0, column = 0, columnspan= 2, pady = 10)

UsernameLabel = Label(LoginFrame, text = 'Username', compound = LEFT, font=('times new roman', 20, 'bold'), bg = 'white')
UsernameLabel.grid(row = 1, column = 0, pady = 10, padx = 20)

UsernameEntry = Entry(LoginFrame, font=('times new roman', 20,))
UsernameEntry.grid(row = 1, column = 1, pady = 10, padx = 20)

PasswordLabel = Label(LoginFrame, text = 'Password', compound = LEFT, font=('times new roman', 20, 'bold'), bg = 'white')
PasswordLabel.grid(row = 2, column = 0, pady = 10, padx = 20)

PasswordEntry = Entry(LoginFrame, font=('times new roman', 20,))
PasswordEntry.grid(row = 2, column = 1, pady = 10, padx = 20)


LoginButton = Button(LoginFrame, text = 'Login', font=('times new roman', 14, 'bold'), width = 15, fg = 'white'
                     , bg = 'cornflowerblue', activeforeground = 'cornflowerblue', command = login )
LoginButton.grid(row = 3, column = 1, pady = 10)

window.mainloop()