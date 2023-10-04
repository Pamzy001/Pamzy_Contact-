from tkinter import *


window = Tk()
window.title('Contact Book')
window.geometry("320x500")
window.resizable(False, True)

contact = {}

def display_contact():
    if not contact:
        print("empty contact book")
    else: 
        contacts = ""
        for key,value in contact.items():
            contacts = f"{key}: {value}\n"
        return f"Name: Phone Number \n{contacts}"

 
def get_info():
    name = name_box.get()
    number = number_box.get()
    output = display_contact()
    contact_details.config(text=output)
    contact[name] = number
    print(contact)

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New Contact')
filemenu.add_command(label='Search Contact', command='')
filemenu.add_command(label='Display Contact', command=display_contact)
filemenu.add_command(label='Edit Contact', command='')
filemenu.add_command(label='Delete Contact', command='')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

name = Label(window, text='Name:')
name.place(x=12, y=10)
phone_num = Label(window, text='Phone number:')
phone_num.place(x=12, y=30)
name_box = Entry(window)
name_box.place(x=120, y=10)
number_box = Entry(window)
number_box.place(x=120, y=30)
submit_button = Button(window, text="Submit Info", width=18, command=get_info)
submit_button.place(x=120, y=60)
contact_details = Label(window, text="Name: Phone Number")
contact_details.place(x=12, y=100)

# while True:
#     choice = int(input("1.c Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact \n 6. Exit \n Enter your choice"))
#     if choice == 1:
#         name = input("enter the contact name: ")
#         phone = input("enter the mobile number: ")
#         contact[name] = phone
#     elif choice == 2:
#         search_name = input("enter the contact name: ")
#         if search_name in contact:
#             print(search_name," 's contact number is ", contact [search_name])
#         else:
#             print("Name is not found in contact book")
#     elif choice == 3:
#         if not contact:
#             print("empty contact book")
#         else: 
#             display_contact()
#     elif choice == 4:
#         edit_contact = input("Enter the contact to be edited ")
#         if edit_contact in contact :
#             phone = input(" enter mobile number: ")
#             contact[edit_contact] = phone
#             print(" contact updated")
#             display_contact()
#         else:
#             print("Name is not found in contact book")
#     elif choice == 5:
#         del_contact = input("Enter the contact to be deleted: ")
#         if del_contact in contact:
#             confirm = input("Do you want to delete this contact y/n? ")
#             if confirm == 'y' or confirm == 'Y' :
#                 contact. pop(del_contact)
#             display_contact()
#         else:
#             print("Name is not found in contact book")
#     elif choice == 6:
#         break
#     # else:




window.mainloop()