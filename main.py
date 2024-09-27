from tkinter import *
from tkinter import ttk
from views import *
from tkinter import messagebox

#colors
co0 = "#ffffff"
co1 = "#000000"
co2 = "#4456F0"

window = Tk()
window.title("")
window.geometry('485x450') 
window.configure(background = co0)
window.resizable(width=FALSE, height=False)

#frames
frame_up = Frame(window, width=500, height=50, bg=co2)
frame_up.grid(row=0, column=0, padx=0, pady=1)

frame_down = Frame(window, width=500, height=150, bg=co0)
frame_down.grid(row=1, column=0, padx=0, pady=1)

frame_table = Frame(window, width=500, height=100, bg=co0, relief="flat")
frame_table.grid(row=2, column=0, columnspan=2, padx=10, pady=1, sticky=NW)

#functions
def show():
    global tree
    list_header = ['Name', 'Phone No.', 'Email','Address']

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=list_header, show="headings")
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0,  sticky='ns')
    hsb.grid(column=0, row=1,  sticky='ew')

    #tree head
    tree.heading(0, text='Name', anchor=NW)
    tree.heading(1, text='Phone No.', anchor=NW)
    tree.heading(2, text='Email', anchor=NW)
    tree.heading(3, text='Address', anchor=NW)

    #tree columns
    tree.column(0, width=120, anchor='nw')
    tree.column(1, width=80, anchor='nw')
    tree.column(2, width=120, anchor='nw')
    tree.column(3, width=138, anchor='nw')

    for item in demo_list:
        tree.insert('', 'end', values=item)

show()

def insert():
    Name = e_name.get()
    Phone = e_phone.get()
    Email = e_email.get()
    Address = e_address.get()

    data = [Name, Phone, Email, Address]

    if Name == '' or Phone == '' or Email == '' or Address == '':
        messagebox.showwarning('data', 'Please fill in all fields')
    else:
        add(data)
        messagebox.showinfo('data', 'Contact added successfully')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_email.delete(0, 'end')
        e_address.delete(0, 'end')
        e_search.delete(0, 'end')
        
        show()

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Phone = str(tree_list[1])
        Email = str(tree_list[2])
        Address = str(tree_list[3])

        e_name.insert(0, Name)
        e_phone.insert(0, Phone)
        e_email.insert(0, Email)
        e_address.insert(0, Address)
        

        def confirm():
            new_name = e_name.get()
            new_phone = e_phone.get()
            new_email = e_email.get()
            new_address = e_address.get()


            data = [new_phone, new_name, new_phone, new_email, new_address]
            
            update(data)

            messagebox.showinfo('Success', 'Contact updated successfully')
            
            e_name.delete(0, 'end')
            e_phone.delete(0, 'end')
            e_email.delete(0, 'end')
            e_address.delete(0, 'end')
            e_search.delete(0, 'end')

            for widget in frame_table.winfo_children():
                widget.destroy()

            b_confirm.destroy()
            
            show()
        b_confirm = Button(frame_down, text="Confirm", width=10, bg=co2,fg = co0, font=('Ivy 8 bold'),command= confirm)
        b_confirm.place(x = 290, y=110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_phone = str(tree_list[2])

        remove(tree_phone)

        messagebox.showinfo('Success', 'Contact has been deleted successfully')

        for widget in frame_table.winfo_children():
            widget.destroy()

        show() 

    except IndexError:
            messagebox.showerror('Error', 'Select one of them from the table')


def to_search():
    phone = e_search.get()

    data = search(phone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values=item)
    e_name.delete(0, 'end')
    e_phone.delete(0, 'end')
    e_email.delete(0, 'end')
    e_address.delete(0, 'end')
    e_search.delete(0, 'end')

#frame_up widgets
app_name = Label(frame_up, text="Contact Book", height=1, font=('Verdana 17 bold'), bg=co2, fg=co0)
app_name.place(x=5, y=5)

#frame_down widgets
l_name = Label(frame_down, text="Name *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_name.place(x=10, y=20)
e_name = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_name.place(x=100 , y=20)

l_phone = Label(frame_down, text="Phone No. *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_phone.place(x=10, y=50)
e_phone = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_phone.place(x=100 , y=50)

l_email = Label(frame_down, text="Email *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_email.place(x=10, y=80)
e_email = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_email.place(x=100 , y=80)

l_address = Label(frame_down, text="Address *", width=20, height=1, font=('Ivy 10'), bg=co0, anchor=NW)
l_address.place(x=10, y=110)
e_address = Entry(frame_down, width=25, justify='left', highlightthickness=1, relief="solid")
e_address.place(x=100 , y=110)

b_search = Button(frame_down, text="Search", width=10, bg=co0,fg = co1, font=('Ivy 8 bold'), command= to_search)
b_search.place(x= 260, y=20)
e_search = Entry(frame_down, width=16, justify='left', font=('Ivy',11), highlightthickness=1, relief='solid')
e_search.place(x=347, y=20)

b_view = Button(frame_down, text="View", width=10, bg=co2,fg = co0, font=('Ivy 8 bold'), command= show)
b_view.place(x= 290, y=50)

b_add = Button(frame_down, text="Add", width=10, bg=co2,fg = co0, font=('Ivy 8 bold'), command=insert)
b_add.place(x= 400, y=50)

b_update = Button(frame_down, text="Update", width=10, bg=co2,fg = co0, font=('Ivy 8 bold'), command=to_update)
b_update.place(x= 400, y=80)

b_delete = Button(frame_down, text="Delete", width=10, bg=co2,fg = co0, font=('Ivy 8 bold'), command= to_remove)
b_delete.place(x= 400, y=110)



window.mainloop()