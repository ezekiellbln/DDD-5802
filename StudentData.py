from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox,filedialog
import pymysql
import pandas
#Funtionality

def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def Export_data():
    url = filedialog.asksaveasfilename(defaultextension = '.csv')
    indexing = StudentTable.get_children()
    newlist = []
    for index in indexing:
        content = StudentTable.item(index)
        datalist = content['values']
        newlist.append(datalist)

    table = pandas.DataFrame(newlist, columns= ['Student ID', 'First Name', 'Last Name', 'Middle Initial', 'Age',
                                                'Gender', 'Date of Birth', 'Course', 'Year Level', 'Email', 'Address', 'Date Added'])
    table.to_csv(url, index = False)
    messagebox.showinfo('Success', 'Data is saved successfully')



def field_data(title, button_text, command):
    global IDEntry, FNameEntry, LNameEntry, MIEntry, AgeEntry, GenderEntry, DoBEntry, CourseEntry, YLEntry, EmailEntry, AddressEntry, Screen
    Screen = Toplevel()
    Screen.title(title)
    Screen.grab_set()
    Screen.resizable(False, False)
    IDLabel = Label(Screen, text='Student ID', font=('times new roman', 20, 'bold'))
    IDLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    IDEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    IDEntry.grid(row=0, column=1, padx=10, pady=15)

    FNameLabel = Label(Screen, text='First Name', font=('times new roman', 20, 'bold'))
    FNameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    FNameEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    FNameEntry.grid(row=1, column=1, padx=10, pady=15)

    LNameLabel = Label(Screen, text='Last Name', font=('times new roman', 20, 'bold'))
    LNameLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    LNameEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    LNameEntry.grid(row=2, column=1, padx=10, pady=15)

    MILabel = Label(Screen, text='Middle Initial', font=('times new roman', 20, 'bold'))
    MILabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    MIEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    MIEntry.grid(row=3, column=1, padx=10, pady=15)

    AgeLabel = Label(Screen, text='Age', font=('times new roman', 20, 'bold'))
    AgeLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    AgeEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    AgeEntry.grid(row=4, column=1, padx=10, pady=15)

    GenderLabel = Label(Screen, text='Gender', font=('times new roman', 20, 'bold'))
    GenderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    GenderEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    GenderEntry.grid(row=5, column=1, padx=10, pady=15)

    DoBLabel = Label(Screen, text='Date of Birth', font=('times new roman', 20, 'bold'))
    DoBLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    DoBEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    DoBEntry.grid(row=6, column=1, padx=10, pady=15)

    CourseLabel = Label(Screen, text='Course', font=('times new roman', 20, 'bold'))
    CourseLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    CourseEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    CourseEntry.grid(row=7, column=1, padx=10, pady=15)

    YLLabel = Label(Screen, text='Year Level', font=('times new roman', 20, 'bold'))
    YLLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    YLEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    YLEntry.grid(row=8, column=1, padx=10, pady=15)

    EmailLabel = Label(Screen, text='Email', font=('times new roman', 20, 'bold'))
    EmailLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    EmailEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    EmailEntry.grid(row=9, column=1, padx=10, pady=15)

    AddressLabel = Label(Screen, text='Address', font=('times new roman', 20, 'bold'))
    AddressLabel.grid(row=10, column=0, padx=30, pady=15, sticky=W)
    AddressEntry = Entry(Screen, font=('roman', 15, 'bold'), width=24)
    AddressEntry.grid(row=10, column=1, padx=10, pady=15)

    Student_button = ttk.Button(Screen, text=button_text, command=command)
    Student_button.grid(row=11, columnspan=2, pady=15)

    if title=='Update Student':
        indexing = StudentTable.focus()
        content = StudentTable.item(indexing)
        listdata = content['values']
        IDEntry.insert(0, listdata[0])
        FNameEntry.insert(0, listdata[1])
        LNameEntry.insert(0, listdata[2])
        MIEntry.insert(0, listdata[3])
        AgeEntry.insert(0, listdata[4])
        GenderEntry.insert(0, listdata[5])
        DoBEntry.insert(0, listdata[6])
        CourseEntry.insert(0, listdata[7])
        YLEntry.insert(0, listdata[8])
        EmailEntry.insert(0, listdata[9])
        AddressEntry.insert(0, listdata[10])

def Update_data():
    query = 'update student set FirstName = %s, LastName = %s, MiddleInitial = %s, Age = %s, Gender = %s, DateofBirth = %s,' \
            'Course = %s, YearLevel = %s, Email = %s, Address = %s, DateAdded = %s where StudentID = %s'
    mycursor.execute(query, (FNameEntry.get(), LNameEntry.get(), MIEntry.get(), AgeEntry.get(), GenderEntry.get(), DoBEntry.get(),
                             CourseEntry.get(), YLEntry.get(), EmailEntry.get(), AddressEntry.get(), Date, IDEntry.get()))
    con.commit()
    messagebox.showinfo('Success', f'StudentID {IDEntry.get()} is updated successfully', parent = Screen)
    Screen.destroy()
    Show_student()


def Show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    StudentTable.delete(*StudentTable.get_children())
    for data in fetched_data:
        StudentTable.insert('', END, values=data)

def Delete_student():
    indexing = StudentTable.focus()
    print(indexing)
    content = StudentTable.item(indexing)
    content_ID = content['values'][0]
    query = 'delete from student where StudentID = %s'
    mycursor.execute(query, content_ID)
    con.commit()
    messagebox.showinfo('Deleted', f'StudentID {content_ID} is deleted successfully')
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    StudentTable.delete(*StudentTable.get_children())
    for data in fetched_data:
        StudentTable.insert('', END, values = data)


def Search_data():
    query = 'Select * from student where StudentID = %s or FirstName = %s or LastName = %s or MiddleInitial = %s or Age = %s or Gender = %s ' \
            'or DateofBirth = %s or Course = %s or YearLevel = %s or Email = %s or Address = %s'
    mycursor.execute(query, (IDEntry.get(), FNameEntry.get(), LNameEntry.get(), MIEntry.get(), AgeEntry.get(), GenderEntry.get(), DoBEntry.get(),
                             CourseEntry.get(), YLEntry.get(), EmailEntry.get(), AddressEntry.get()))
    StudentTable.delete(*StudentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        StudentTable.insert('', END, values = data)





def Add_data():
    if IDEntry.get()==''or FNameEntry.get()=='' or LNameEntry.get()=='' or MIEntry.get()=='' or AgeEntry.get()=='' or GenderEntry.get()=='' or DoBEntry.get()=='' or CourseEntry.get()=='' or YLEntry.get()=='' or EmailEntry.get()=='' or AddressEntry.get()=='':
        messagebox.showerror('Error', 'All Fields are Required', parent = Screen)

    else:
        currentdate = time.strftime('%d/%m/%Y')
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query, (IDEntry.get(), FNameEntry.get(), LNameEntry.get(), MIEntry.get(), AgeEntry.get(), GenderEntry.get(), DoBEntry.get(), CourseEntry.get(), YLEntry.get(), EmailEntry.get(), AddressEntry.get(), currentdate))
            con.commit()
            result = messagebox.askyesno('Confirm','Data added Successfully. Do you want to new form?', parent = Screen)
            if result:
                IDEntry.delete(0, END)
                FNameEntry.delete(0, END)
                LNameEntry.delete(0, END)
                MIEntry.delete(0, END)
                AgeEntry.delete(0, END)
                GenderEntry.delete(0, END)
                DoBEntry.delete(0, END)
                CourseEntry.delete(0, END)
                YLEntry.delete(0, END)
                EmailEntry.delete(0, END)
                AddressEntry.delete(0, END)
            else:
                pass
            Screen.destroy()

        except:
            messagebox.showerror('Error', 'Student ID cannot be repeated', parent = Screen)
            return

        query = 'select * from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        StudentTable.delete(*StudentTable.get_children())
        for data in fetched_data:
            StudentTable.insert('', END, values = data)


def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host = 'localhost', user = 'root', password = 'Ezekiel29!')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Invalid Details', parent = ConnectWindow)
            return
        try:
            query = 'create database StudentDatabaseSystem'
            mycursor.execute(query)
            query = 'use StudentDatabaseSystem'
            mycursor.execute(query)
            query = 'create table student (StudentID INT NOT NULL PRIMARY KEY, FirstName CHAR(45), LastName VCHAR(45), MiddleInitial CHAR(45),' \
                    'Age VARCHAR(45), Gender CHAR(45), DateofBirth DATE, Course VARCHAR(45), YearLevel VARCHAR(45), Email VARCHAR(45), Address VARCHAR(45), Date Added'
            mycursor.execute(query)
        except:
            query = 'use StudentDatabaseSystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is Successful', parent=ConnectWindow)
        ConnectWindow.destroy()
        AddStudentButton.config(state = NORMAL)
        SearchStudentButton.config(state=NORMAL)
        DeleteStudentButton.config(state=NORMAL)
        UpdateStudentButton.config(state=NORMAL)
        ShowStudentButton.config(state=NORMAL)
        ExportStudentButton.config(state=NORMAL)

    ConnectWindow = Toplevel()
    ConnectWindow.grab_set()
    ConnectWindow.geometry('470x250+730+230')
    ConnectWindow.title('Database Connection')
    ConnectWindow.resizable(False, False)

    HostNameLabel = Label(ConnectWindow, text = 'Host Name', font = ('arial', 20, 'bold'))
    HostNameLabel.grid(row = 0, column = 0, padx = 20)

    HostEntry = Entry(ConnectWindow, font = ('roman', 15, 'bold'), bd = 2)
    HostEntry.grid(row = 0, column = 1, padx = 40, pady = 20)

    UsernameLabel = Label(ConnectWindow, text = 'Username', font = ('arial', 20, 'bold'))
    UsernameLabel.grid(row = 1, column = 0, padx = 20)

    UsernameEntry = Entry(ConnectWindow, font = ('roman', 15, 'bold'), bd = 2)
    UsernameEntry.grid(row = 1, column = 1, padx = 40, pady = 20)

    PasswordLabel = Label(ConnectWindow, text ='Password', font = ('arial', 20, 'bold'))
    PasswordLabel.grid(row = 2, column = 0, padx = 20)

    PasswordEntry = Entry(ConnectWindow, font = ('roman', 15, 'bold'), bd = 2)
    PasswordEntry.grid(row = 2, column = 1, padx = 40, pady = 20)

    ConnectButton = ttk.Button(ConnectWindow, text = 'Connect', command = connect)
    ConnectButton.grid(row = 3, columnspan = 2)



def clock():
    global Date, CurrentTime
    Date = time.strftime('%d/%m/%Y')
    CurrentTime = time.strftime('%H: %M: %S')
    DateTimeLabel.config(text = f' Date: {Date}\nTime: {CurrentTime}')
    DateTimeLabel.after(1000, clock)

#GUI
root = ttkthemes.ThemedTk()

root.get_themes()
root.set_theme('breeze')

root.geometry('1280x700+50+50')
root.resizable(False, False)
root.title('Student Database System')

DateTimeLabel = Label(root, font = ('times new roman', 18, 'bold'))
DateTimeLabel.place(x = 5, y = 5)
clock()

SliderLabel = Label (root, text = 'Student Database System', font = ('times new roman', 40, 'italic bold'), width = 30)
SliderLabel.place(x = 200, y = 0)

ConnectButton = ttk.Button(root, text = 'Connect Database', command = connect_database)
ConnectButton.place(x = 1100, y = 30)

LeftFrame = Frame(root)
LeftFrame.place(x = 50, y = 80, width = 300, height = 600)

LogoImage = PhotoImage(file = 'students.png')
LogoLabel = Label(LeftFrame, image = LogoImage)
LogoLabel.grid(row = 0, column = 0)

AddStudentButton = ttk.Button(LeftFrame, text = 'Add Student', width = 25, state = DISABLED, command = lambda :field_data('Add Student', 'Add', Add_data))
AddStudentButton.grid(row = 1, column = 0, pady = 20)

SearchStudentButton = ttk.Button(LeftFrame, text = 'Search Student', width = 25, state = DISABLED, command = lambda :field_data('Search Student', 'Search', Search_data))
SearchStudentButton.grid(row = 2, column = 0, pady = 20)

DeleteStudentButton = ttk.Button(LeftFrame, text = 'Delete Student', width = 25, state = DISABLED, command = Delete_student)
DeleteStudentButton.grid(row = 3, column = 0, pady = 20)

UpdateStudentButton = ttk.Button(LeftFrame, text = 'Update Student', width = 25, state = DISABLED, command = lambda :field_data('Update Student', 'Update', Update_data))
UpdateStudentButton.grid(row = 4, column = 0, pady = 20)

ShowStudentButton = ttk.Button(LeftFrame, text = 'Show Student', width = 25, state = DISABLED, command = Show_student)
ShowStudentButton.grid(row = 5, column = 0, pady = 20)

ExportStudentButton = ttk.Button(LeftFrame, text = 'Export Student', width = 25, state = DISABLED, command = Export_data)
ExportStudentButton.grid(row = 6, column = 0, pady = 20)

ExitButton = ttk.Button(LeftFrame, text = 'Exit', width = 25, command = iexit)
ExitButton.grid(row = 7, column = 0, pady = 20)

RightFrame = Frame(root)
RightFrame.place(x = 350, y = 80, width = 900, height = 600)

ScrollbarX = Scrollbar(RightFrame, orient = HORIZONTAL)
ScrollbarY = Scrollbar(RightFrame, orient = VERTICAL)

StudentTable = ttk.Treeview(RightFrame, columns = ('Student ID', 'First Name', 'Last Name', 'Middle Initial', 'Age', 'Gender', 'Date of Birth',
                                    'Course', 'Year Level', 'Email', 'Address', 'Date Added'),
                            xscrollcommand = ScrollbarX.set, yscrollcommand = ScrollbarY.set)

ScrollbarX.config(command = StudentTable.xview)
ScrollbarY.config(command = StudentTable.yview)

ScrollbarX.pack(side = BOTTOM, fill = X)
ScrollbarY.pack(side = RIGHT, fill = Y)

StudentTable.pack(fill = BOTH, expand = 1)

StudentTable.heading('Student ID', text = 'Student ID')
StudentTable.heading('First Name', text = 'First Name')
StudentTable.heading('Last Name', text = 'Last Name')
StudentTable.heading('Middle Initial', text = 'Middle Initial')
StudentTable.heading('Age', text = 'Age')
StudentTable.heading('Gender', text = 'Gender')
StudentTable.heading('Date of Birth', text = 'Date of Birth')
StudentTable.heading('Course', text = 'Course')
StudentTable.heading('Year Level', text = 'Year Level')
StudentTable.heading('Email', text = 'Email')
StudentTable.heading('Address', text = 'Address')
StudentTable.heading('Date Added', text = 'Date Added')

StudentTable.column('Student ID', width = 100, anchor = CENTER)
StudentTable.column('First Name', width = 150, anchor = CENTER)
StudentTable.column('Last Name', width = 150, anchor = CENTER)
StudentTable.column('Middle Initial', width = 120, anchor = CENTER)
StudentTable.column('Age', width = 60, anchor = CENTER)
StudentTable.column('Gender', width = 100, anchor = CENTER)
StudentTable.column('Date of Birth', width = 110, anchor = CENTER)
StudentTable.column('Course', width = 100, anchor = CENTER)
StudentTable.column('Year Level', width = 100, anchor = CENTER)
StudentTable.column('Email', width = 250, anchor = CENTER)
StudentTable.column('Address', width = 200, anchor = CENTER)
StudentTable.column('Date Added', width = 110, anchor = CENTER)

Style = ttk.Style()
Style.configure('Treeview', rowheight = 40, foreground = 'blue4')
Style.configure('Treeview.Heading', font = ('bold'))

StudentTable.config(show = 'headings')

root.mainloop()