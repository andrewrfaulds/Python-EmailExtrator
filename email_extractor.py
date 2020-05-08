from tkinter import *
from tkinter import messagebox
import re

#main window paramters

root = Tk()
root.title("Email Address Extractor")
root.geometry('1500x900+200+200')


# function to search input string for regex matches, store in list and then
# create unique set of matches in new list. It then inputs these to a textbox on the gui form.

def get_emails(s):
    ''' gets matches and inputs to textbox'''
    Emails = [re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+)", s)]
    for Email in Emails:
        email_set = set(Email)
        Txtbox_2.insert(1.0, email_set)

# event handler for the process button. clears output textbox on each run
# and takes input from input texbox and passes it to the get_emails function.
def button_click():
    '''button event handler for process button'''
    Txtbox_2.delete(1.0, END)
    line = Txtbox_1.get("1.0", END)
    get_emails(line)

# function to allow exporting to txt file with try/except checks. it will append or
# create file foo.txt in the current working directory and write each value in the output
# textbox to the file, opening a message box on completion or generating exception on fail.
def export_txt():
    '''export to txt file'''
    try:
        output_data = [Txtbox_2.get("1.0", 'end -1c')]
        with open("output.txt", "w+") as output_file:
            for val in output_data:
                output_file.write(val)
        messagebox.showinfo("Alert", "Export Complete")
    except:
        print('An error occurred.')




# basic form paramters
app = Frame(root)
app.grid(padx=40, pady=40)
Lbl_1 = Label(app, text="Enter text here: ")
Lbl_1.grid(row=7, column=2)
Lbl_2 = Label(app, text="Addresses Detected: ")
Lbl_2.grid(row=7, column=5)
Bttn_1 = Button(app, command=lambda: button_click(), text="Process Text")
Bttn_1.grid(row=9, column=2)
Bttn_2 = Button(app, command=lambda: export_txt(), text="Export")
Bttn_2.grid(row=9, column=5)
Txtbox_1 = Text(app, width=50, height=25, relief=RIDGE, borderwidth=2, bg='white')
Txtbox_1.grid(row=6, column=2)
Txtbox_2 = Text(app, width=50, height=25, relief=RIDGE, borderwidth=2, bg='white')
Txtbox_2.grid(row=6, column=5)

# initiate main loop
mainloop()
 