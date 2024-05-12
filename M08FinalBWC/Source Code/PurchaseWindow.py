import tkinter as tk
from tkinter import messagebox

class PurchaseWindow:
    """This is a class for the purchase window to be displayed."""
    def __init__(self, master, orderCount, userInfo, keyPrices, infoSubmitted):
        # creates the window and ensures that data transferred between classes is accurate
        self.master = master
        self.orderCount = orderCount
        self.userInfo = userInfo
        self.keyPrices = keyPrices
        self.infoSubmitted = infoSubmitted
        self.master.title("Finish Order")
        self.master.geometry("1500x500")
        self.master.option_add("*Font", "Times")

        # frame to hold buttons
        self.btnFrame = tk.Frame(self.master, bg="#e0e0e0")
        self.btnFrame.pack(side=tk.TOP, fill=tk.X)

        # button to return the user back to the main window
        self.returnBtn = tk.Button(self.btnFrame, text="Return", command=self.return_to_main)
        self.returnBtn.pack(side=tk.LEFT, padx=(10, 5), pady=10, fill=tk.X, expand=True)

        # button to delete the information stored within the order
        self.deleteOrderBtn = tk.Button(self.btnFrame, text="Delete Order Information", command=self.delete_order_information)
        self.deleteOrderBtn.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.X, expand=True)

        # button to complete the order and reset the program to allow for more orders to be made
        self.completeBtn = tk.Button(self.btnFrame, text="Complete Order", command=self.complete_order)
        self.completeBtn.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.X, expand=True)

        # frame to hold the user frame and order frame
        self.mainFrame = tk.Frame(self.master)
        self.mainFrame.pack(fill=tk.BOTH, expand=True)

        # frame for the user information to be displayed
        self.userFrame = tk.Frame(self.mainFrame)
        self.userFrame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

        # label to explain what information is being shown below, for this it is the user information
        self.userInfoLbl = tk.Label(self.userFrame, text="User Information:", font=("Times", 14, "bold"))
        self.userInfoLbl.pack()

        # if statement that will display a message to the user showing that the user information will appear there if user informaiton is not already established
        if userInfo == []:
            self.userInfoDisplayLbl = tk.Label(self.userFrame, text="[User information will appear here]", font=("Times", 12))
            self.userInfoDisplayLbl.pack(anchor="w")

        # list for the labels to show what information is being shown
        userInfoLbls = ["First Name: ", "Last Name: ", "Address: ", "City: ", "State: ", "Zip: "]
        # for loop to display the label for the information type of and the respective information that goes along with it
        for i in range(len(userInfo)):
            label = tk.Label(self.userFrame, text=userInfoLbls[i] + userInfo[i], font=("Times", 12))
            label.pack(anchor="w")

        # frame for the order information to be displayed
        self.orderFrame = tk.Frame(self.mainFrame)
        self.orderFrame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        # label to examplain what information is being shown below, for this it is the user's order
        self.orderLbl = tk.Label(self.orderFrame, text="Your Order:", font=("Times", 14, "bold"))
        self.orderLbl.pack()

        # label that displayed to the user where the informatin for their order will be held if the order is not already established
        self.orderDisplayLbl = tk.Label(self.orderFrame, text="[Order will appear here.]", font=("Times", 12), justify="left")
        self.orderDisplayLbl.pack(padx=10, fill=tk.BOTH)

        # label to explain what information is being shown below, for this it is the total price of the user's order 
        self.totalLbl = tk.Label(self.orderFrame, text="Total Price:", font=("Times", 14, "bold"))
        self.totalLbl.pack()

        # label to display the total price of the user's order
        self.totalDisplayLbl = tk.Label(self.orderFrame, text="", font=("Times", 12), justify="left")
        self.totalDisplayLbl.pack(pady=(5, 0))

        # if statement that will let the order be displayed if the order is not blank
        if orderCount != {}:
            self.update_order_display()

    def update_order_display(self):
        """This is a function that will display the order
        to the user."""
        orderText = ""
        totalPrice = 0
        # for loop to add each key within the order to the order display
        for key, count in self.orderCount.items():
            # sets the price for the key that is being set
            price = self.keyPrices.get(key, 0)
            totalPrice += price * count
            # if statement that checks if the key in the order needs to be displayed as one or multiple
            if count == 1:
                orderText += f"x{count} '{key}' Key (${price})\n"
            else:
                orderText += f"x{count} '{key}' Keys (${price * count})\n"
        # sets the display labels to display the order information
        self.orderDisplayLbl.config(text=orderText)
        self.totalDisplayLbl.config(text=f"${totalPrice}")

    def delete_order_information(self):
            """This is a function that deletes the information
            for the user and order information."""
            # if statement to not allow the order to be deleted if there is no order
            if self.infoSubmitted == False and self.orderCount == {}:
                messagebox.showerror("Error", "Cannot delete blank order.")
                return
            # message box to ask the user if they are sure they want to delete their user and order information
            confirmation = messagebox.askyesno("Delete Order Information", "Are you sure you want to delete the order information?")
            # if statement for if the user clicks yes that sets the order and user information to be blank and returns the user to the main window
            if confirmation:
                self.orderCount = {}
                self.userInfo = []
                self.infoSubmitted = False
                self.return_to_main()

    def complete_order(self):
        """This is a function that will submit the order
        as long criteria is met."""
        # if statement that will not allow order to be completed if blank
        if self.infoSubmitted == False and self.orderCount == {}:
            messagebox.showerror("Error", "Cannot complete blank order.")
            return
        
        # if statement that will not allow the order to be completed if no user information is provided
        if self.infoSubmitted == False:
            messagebox.showerror("Error", "User information needs to be provided.")
            return
        
        # if statement that will not allow the order to be completed if no order information is provided
        if self.orderCount == {}:
            messagebox.showerror("Error", "An order needs to be made to complete order.")
            return
        
        # message box to display that the order has been completed
        messagebox.showinfo("Order Completed", "Your order has been completed. Thank you!")

        # sets the order and user info to be blank and the infoSubmitted boolean to false so that the user information entries are no longer blank
        self.infoSubmitted = False
        self.orderCount = {}
        self.userInfo = []

        # returns the user to the main window to begin the program again
        self.return_to_main()

    def return_to_main(self):
        """This is a function that returns the user to the main window."""
        from MainWindow import MainWindow
        self.master.withdraw()
        main_window = MainWindow(tk.Toplevel(self.master), self.orderCount, self.userInfo, self.keyPrices, self.infoSubmitted)