from sqlite3.dbapi2 import SQLITE_DROP_TEMP_TABLE, Row, connect
from tkinter import *
import sqlite3

root = Tk()
root.title("Contact Book")
root.geometry("400x600")

# Connect to database or create one 
conn = sqlite3.connect("contact_book.db")

# create a cursor to execute SQL commands
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE contacts (
        f_name TEXT,
        l_name TEXT,
        city TEXT,
        phone INTEGER
        )""")

# create input_fields to add data
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=10, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
city = Entry(root, width=30)
city.grid(row=2, column=1)
phone = Entry(root, width=30)
phone.grid(row=3, column=1)

select = Entry(root, width=30) # select field to enter rowid (for update and delete)
select.grid(row=5, column=1, pady=(10,0))

# create labels for input_fields
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=10, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
city_label = Label(root, text="City")
city_label.grid(row=2, column=0)
phone_label = Label(root, text="Phone")
phone_label.grid(row=3, column=0)

select_label = Label(root, text="Enter ID")
select_label.grid(row=5, column=0, pady=(10,0))

# create function to take data from input_fields and add it to database
def submit():
    # conn = sqlite3.connect(":memory:")
    # c = conn.cursor()

    # # Create Table
    # c.execute("""CREATE TABLE contacts (
    #     f_name TEXT,
    #     l_name TEXT,
    #     city TEXT,
    #     phone INTEGER
    #     )""")

    c.execute("""INSERT INTO contacts VALUES (:f_name, :l_name, :city, :phone)""",
        {'f_name':f_name.get(), 'l_name':l_name.get(), 'city':city.get(), 'phone':phone.get()}
        )

    # conn.commit()
    # conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    city.delete(0, END)
    phone.delete(0, END)

# create button to add data into database
submit_btn = Button(root, text="Add data to Database!", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, padx=(12,0), pady=(10,0), ipadx=100, ipady=10)

# save function to save our changes in database
def save():
    c.execute("""UPDATE contacts
        SET f_name=:f_name,
        l_name=:l_name,
        city=:city,
        phone=:phone
        WHERE rowid=:id""",
        {
        'id':select.get(),
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'city':city.get(),
        'phone':phone.get()
        })
    
    edit_root.destroy()
    select.delete(0, END)

# create function to update contact from database
def update():
    global edit_root # global variable
    edit_root = Tk()
    edit_root.title("Update Contact")
    edit_root.geometry("400x400")

    # get data of particular row as placeholders
    rowid = select.get()
    c.execute("SELECT * FROM contacts WHERE rowid=:id", {'id':rowid})
    result = c.fetchall()

    # create input_fields to edit data
    global f_name, l_name, city, phone # declare as global variables

    f_name = Entry(edit_root, width=30)
    l_name = Entry(edit_root, width=30)
    city = Entry(edit_root, width=30)
    phone = Entry(edit_root, width=30)

    # insert placeholders
    for info in result:
        f_name.insert(0, info[0])
        l_name.insert(0, info[1])
        city.insert(0, info[2])
        phone.insert(0, info[3])

    # display input_fields
    f_name.grid(row=0, column=1, padx=10, pady=(10, 0))
    l_name.grid(row=1, column=1)
    city.grid(row=2, column=1)
    phone.grid(row=3, column=1)


    # create labels for input_fields
    f_name_label = Label(edit_root, text="First Name")
    f_name_label.grid(row=0, column=0, padx=10, pady=(10, 0))
    l_name_label = Label(edit_root, text="Last Name")
    l_name_label.grid(row=1, column=0)
    city_label = Label(edit_root, text="City")
    city_label.grid(row=2, column=0)
    phone_label = Label(edit_root, text="Phone")
    phone_label.grid(row=3, column=0)
    
    # create button to save contact info
    save_btn = Button(edit_root, text="Save Contact", command=save)
    save_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=120, ipady=10)

# create button to update contact
edit_btn = Button(root, text="Update Contact!", command=update)
edit_btn.grid(row=6, column=0, columnspan=2, padx=(12,0), pady=(10,0), ipadx=113, ipady=10)

# create function to delete record from database
def dlt():
    # get row we want to delete
    rowid = select.get() 
    
    c.execute("DELETE FROM contacts WHERE rowid = :id", {'id':rowid})

    select.delete(0, END)

# create button to delete record
delete_btn = Button(root, text="Delete Contact!", command=dlt)
delete_btn.grid(row=7, column=0, columnspan=2, padx=(12,0), pady=(5,0), ipadx=115, ipady=10)

# create function to show query
def query():
    # NEW WINDOW
    query_root = Tk()
    query_root.title("Contacts Information")
    query_root.geometry("400x400")

    # Headings for contact info
    id_head = Label(query_root, text="ID").grid(row=0, column=0, padx=10, pady=10)
    f_name_head = Label(query_root, text="FIRST_NAME").grid(row=0, column=1)
    l_name_head = Label(query_root, text="LAST_NAME").grid(row=0, column=2)
    city_head = Label(query_root, text="CITY").grid(row=0, column=3)
    phone_head = Label(query_root, text="PHONE").grid(row=0, column=4)

    # get data with rowid
    c.execute("SELECT rowid, * FROM contacts ")

    results = c.fetchall()

    # contacts information
    row_num = 1
    for result in results:
        contact_id = Label(query_root, text=result[0]).grid(row=row_num, column=0)
        contact_id = Label(query_root, text=result[1]).grid(row=row_num, column=1)
        contact_id = Label(query_root, text=result[2]).grid(row=row_num, column=2)
        contact_id = Label(query_root, text=result[3]).grid(row=row_num, column=3)
        contact_id = Label(query_root, text=result[4]).grid(row=row_num, column=4)

        row_num += 1

# create button to show query
query_btn = Button(root, text="Display Contacts!", command=query)
query_btn.grid(row=8, column=0, columnspan=2, padx=(12,0), pady=(10,0), ipadx=113, ipady=10)

# commit to our database 
conn.commit()

# close connection from database
# conn.close()

root.mainloop()