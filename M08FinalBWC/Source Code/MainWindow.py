import tkinter as tk
from tkinter import messagebox
from KeyboardWindow import KeyboardWindow
from PurchaseWindow import PurchaseWindow

class MainWindow:
    """This is a class for the MainWindow to be displayed."""
    def __init__(self, master, orderCount=None, userInfo=None, keyPrices=None, infoSubmited = False):
        # creates the window
        self.master = master
        self.master.title("Welcome to KeyReplacer.")
        self.master.geometry("1500x500")
        self.master.option_add("*Font", "Times")

        # frame to hold buttons
        self.btnFrame = tk.Frame(self.master, bg="#e0e0e0")
        self.btnFrame.pack(side=tk.TOP, fill=tk.X)

        # button to open keyboard window allowing the user to add keys to their order
        self.addBtn = tk.Button(self.btnFrame, text="Add to Order", command=self.open_keyboard_window)
        self.addBtn.pack(side=tk.LEFT, padx=(10, 5), pady=10, fill=tk.X, expand=True)

        # button to open purchase window allowing the user to view and finish their order
        self.buyBtn = tk.Button(self.btnFrame, text="Finish Order", command=self.open_purchase_window)
        self.buyBtn.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.X, expand=True)

        # button to exit the program entirely
        self.exitBtn = tk.Button(self.btnFrame, text="Exit", command=self.exit_program)
        self.exitBtn.pack(side=tk.LEFT, padx=(5, 10), pady=10, fill=tk.X, expand=True)

        # intializes the orderCount dictionary unless already intialized
        if orderCount is not None:
            self.orderCount = orderCount
        else:
            self.orderCount = {}

        # intializes the userInfo list unless already intialized
        if userInfo is not None:
            self.userInfo = userInfo
        else:
            self.userInfo = []

        # intializes the keyPrices dictionary unless already intialized
        if keyPrices is not None:
            self.keyPrices = keyPrices
        else:
            self.keyPrices = {}

        # intializes the infoSubmitted boolean to see if the user has already submitted their information
        if infoSubmited == False:
            self.infoSubmitted = False
        else:
            self.infoSubmitted = infoSubmited

        # frame to hold the labels and entries for the user information
        self.infoFrame = tk.Frame(self.master, bg="white")
        self.infoFrame.pack(side=tk.TOP, fill=tk.X)

        # label that explains what the user needs to put into the entries
        self.infoLbl = tk.Label(self.infoFrame, text="Welcome to KeyReplacer. Please fill in your information below:", bg="white")
        self.infoLbl.pack(pady=5)

        # label to describe what goes in the entry below, for this one it is the first name
        self.fNameLbl = tk.Label(self.infoFrame, text="First Name:", bg="white")
        self.fNameLbl.pack(anchor="w", padx=5)
        # entry for the first name
        self.fNameEntry = tk.Entry(self.infoFrame)
        self.fNameEntry.pack(pady=5, padx=5, fill=tk.X)

        # label to describe what goes in the entry below, for this one it is the last name
        self.lNameLbl = tk.Label(self.infoFrame, text="Last Name:", bg="white")
        self.lNameLbl.pack(anchor="w", padx=5)
        # entry for the last name
        self.lNameEntry = tk.Entry(self.infoFrame)
        self.lNameEntry.pack(pady=5, padx=5, fill=tk.X)

        # label to describe what goes in the entry below, for this one it is the address
        self.addressLbl = tk.Label(self.infoFrame, text="Address:", bg="white")
        self.addressLbl.pack(anchor="w", padx=5)
        # entry for the address
        self.addressEntry = tk.Entry(self.infoFrame)
        self.addressEntry.pack(pady=5, padx=5, fill=tk.X)

        # label to describe what goes in the entry below, for this one it is the city
        self.cityLbl = tk.Label(self.infoFrame, text="City:", bg="white")
        self.cityLbl.pack(anchor="w", padx=5)
        # entry for the city
        self.cityEntry = tk.Entry(self.infoFrame)
        self.cityEntry.pack(pady=5, padx=5, fill=tk.X)

        # label to describe what goes in the entry below, for this one it is the state
        self.stateLbl = tk.Label(self.infoFrame, text="State:", bg="white")
        self.stateLbl.pack(anchor="w", padx=5)
        # entry for the state
        self.stateEntry = tk.Entry(self.infoFrame)
        self.stateEntry.pack(pady=5, padx=5, fill=tk.X)

        # label to describe what goes in the entry below, for this one it is the zip code
        self.zipLbl = tk.Label(self.infoFrame, text="Zip Code:", bg="white")
        self.zipLbl.pack(anchor="w", padx=5)
        # entry for the zip code
        self.zipEntry = tk.Entry(self.infoFrame)
        self.zipEntry.pack(pady=5, padx=5, fill=tk.X)

        # button to run the function to submit the information into the entries
        self.submitBtn = tk.Button(self.infoFrame, text="Submit", command=self.submit_info)
        self.submitBtn.pack(pady=10)

        # if statement to make the window open with the entries and submit button disabled if the information is already submitted
        if self.infoSubmitted == True:
            self.fNameEntry.config(state='disabled')
            self.lNameEntry.config(state='disabled')
            self.addressEntry.config(state='disabled')
            self.cityEntry.config(state='disabled')
            self.stateEntry.config(state='disabled')
            self.zipEntry.config(state='disabled')
            self.submitBtn.config(state='disabled')

    def submit_info(self):
        """This is a function that submits the user information within the
        entries if they have the proper input."""
        fName = self.fNameEntry.get()
        lName = self.lNameEntry.get()
        address = self.addressEntry.get()
        city = self.cityEntry.get()
        state = self.stateEntry.get()
        zip = self.zipEntry.get()

        # if statment that shows an error and does not submit data if any data entries blank
        if fName == "" or lName == "" or address == "" or city == "" or state == "" or zip == "":
            messagebox.showerror("Error", "You cannot leave any entries blank.")
            return
        
        # if statement that shows an error and does not submit data if the first or last name entries are non-alphabetical
        if not fName.isalpha() or not lName.isalpha():
            messagebox.showerror("Error", "First and last names should contain only alphabetical characters.")
            return

        # if statement that shows an error and does not submit data if the zip code is non-numerical characters
        if not zip.isdigit():
            messagebox.showerror("Error", "Zip code should contain only numerical characters.")
            return

        # sets the userInfo list to contain the user information so that it can be transferred between classes
        self.userInfo = [fName, lName, address, city, state, zip]

        # messagebox to display if the user information is submitted successfully
        messagebox.showinfo("Success", "Information submitted successfully.")

        # changes boolean so that the entries stay disabled when the main window is reopened
        self.infoSubmitted = True

        # clears entries text
        self.fNameEntry.delete(0, tk.END)
        self.lNameEntry.delete(0, tk.END)
        self.addressEntry.delete(0, tk.END)
        self.cityEntry.delete(0, tk.END)
        self.stateEntry.delete(0, tk.END)
        self.zipEntry.delete(0, tk.END)

        # disables entries and submit buttons
        self.fNameEntry.config(state='disabled')
        self.lNameEntry.config(state='disabled')
        self.addressEntry.config(state='disabled')
        self.cityEntry.config(state='disabled')
        self.stateEntry.config(state='disabled')
        self.zipEntry.config(state='disabled')
        self.submitBtn.config(state='disabled')

    def open_keyboard_window(self):
        """This is a function that will open the keyboard window."""
        self.master.withdraw()
        keyboardwindow = KeyboardWindow(tk.Toplevel(self.master), self.orderCount, self.userInfo, self.keyPrices, self.infoSubmitted)

    def open_purchase_window(self):
        """This is a function that will open the purchase window."""
        self.master.withdraw()
        purchasewindow = PurchaseWindow(tk.Toplevel(self.master), self.orderCount, self.userInfo, self.keyPrices, self.infoSubmitted)

    def exit_program(self):
        """This is a function that will exit the program entirely."""
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.master.destroy()