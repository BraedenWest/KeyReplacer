import tkinter as tk
from tkinter import messagebox

class KeyboardWindow:
    """This class to display the keyboard window."""
    def __init__(self, master, orderCount, userInfo, keyPrices, infoSubmitted):
        # creates the window and ensures that data transferred between classes is accurate
        self.master = master
        self.orderCount = orderCount
        self.userInfo = userInfo
        self.keyPrices = keyPrices
        self.infoSubmitted = infoSubmitted
        self.master.title("Click a key!")
        self.master.geometry("1375x400")
        self.master.option_add("*Font", "Times")

        # sets the keyprices dictionary to have the accurate prices for the keys
        self.keyPrices = {
            '`': 2, '1': 2, '2': 2, '3': 2, '4': 2, '5': 2, '6': 2, '7': 2, '8': 2, '9': 2, '0': 2, '-': 2, '=': 2, 'Back': 3,
            'Tab': 3, 'Q': 1, 'W': 1, 'E': 1, 'R': 1, 'T': 1, 'Y': 1, 'U': 1, 'I': 1, 'O': 1, 'P': 1, '[': 2, ']': 2, '\\': 2,
            'Caps': 3, 'A': 1, 'S': 1, 'D': 1, 'F': 1, 'G': 1, 'H': 1, 'J': 1, 'K': 1, 'L': 1, ';': 2, "'": 2, 'Enter': 3,
            'L Shift': 3, 'Z': 1, 'X': 1, 'C': 1, 'V': 1, 'B': 1, 'N': 1, 'M': 1, ',': 2, '.': 2, '/': 2, 'R Shift': 3,
            'L Ctrl': 3, 'Win': 3, 'L Alt': 3, 'Space': 5, 'R Alt': 3, 'Fn': 3, 'R Ctrl': 3,
        }

        # frame to hold buttons
        self.btnFrame = tk.Frame(self.master, bg="#e0e0e0")
        self.btnFrame.pack(side=tk.TOP, fill=tk.X)

        # button to return the user to the main window
        self.rtnBtn = tk.Button(self.btnFrame, text="Return", width=1100, command=self.open_main_window)
        self.rtnBtn.pack(side=tk.LEFT, padx=10, pady=10)

        # frame to hold the keyboard arrangement
        self.keysFrame = tk.Frame(self.master, bg="white")
        self.keysFrame.pack(padx=10, pady=(0, 10), side=tk.LEFT)

        # list of lists to hold the keys in formatted arrangement
        self.keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Back'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'", 'Enter'],
            ['L Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'R Shift'],
            ['L Ctrl', 'Win', 'L Alt', 'Space', 'R Alt', 'Fn', 'R Ctrl']
        ]

        # list to hold each button that is created in the for loop below
        self.keyButtons = []
        # for loop that sets each of the keys in each row of the self.keys list of lists to a button in the order of the list
        for row in self.keys:
            # sets the button to each be in it's own row like in the self.keys list but instead of variables it is entire tk.Buttons
            buttonRow = []
            # for loop to check each key in the current row that buttons are being created for
            for key in row:
                # sets the price of the current key
                price = self.keyPrices.get(key, 0)
                # sets the text that will be displayed on each button created
                buttonText = f"{key}\n${price}" 
                # button to display the key and the price formatted in the keyboard arrangement
                button = tk.Button(self.keysFrame, text=buttonText, width=8, height=2, command=lambda k=key: self.add_to_order(k.capitalize()))
                # sets the location of the key in the grid
                button.grid(row=self.keys.index(row), column=row.index(key), padx=1, pady=1)
                # appends the button to the row that it is supposed to be within
                buttonRow.append(button)
            # appens each button row into the keyButtons list
            self.keyButtons.append(buttonRow)

        # frame to hold the order display
        self.orderFrame = tk.Frame(self.master)
        self.orderFrame.pack(padx=10, pady=(0, 10), side=tk.LEFT)

        # label to clarify to the user what information is being shown below, for this label it is the order
        self.orderLbl = tk.Label(self.orderFrame, text="Order:")
        self.orderLbl.pack()

        # label for the order to be displayed within
        self.orderDisplayLbl = tk.Label(self.orderFrame, text="")
        self.orderDisplayLbl.pack()

        # label to clarify to the user what information is being shown below, for this label it is the total
        self.totalLbl = tk.Label(self.orderFrame, text="Total:")
        self.totalLbl.pack()
        
        # label for the order total to be displayed in
        self.totalDisplayLbl = tk.Label(self.orderFrame, text="")
        self.totalDisplayLbl.pack()

    def add_to_order(self, key):
        """This is a function that adds the specified key pressed
        into the order so that the amount of that key can be
        tracked."""
        self.orderCount[key] = self.orderCount.get(key, 0) + 1
        self.update_order_display()

    def update_order_display(self):
        """This is a function that updates the display for the order."""
        totalPrice = 0 
        displayText = ""
        # for loop that checks each key and the count of that key in the order count dictionary
        for key, count in self.orderCount.items():
            # sets the price of the current key being checked
            price = self.keyPrices.get(key, 0)
            # if else statement to display whether there are multiple of the specified key in the order
            if count == 1:
                displayText += f"x{count} '{key}' Key (${price})\n"
            else:
                displayText += f"x{count} '{key}' Keys (${price * count})\n"
            # calculates the total price
            totalPrice += price * count
        # updates the displays to the current order information
        self.orderDisplayLbl.config(text=displayText.strip())
        self.totalDisplayLbl.config(text=f"${totalPrice}")

    def open_main_window(self):
        """This is a function that returns the user to the main window."""
        from MainWindow import MainWindow
        self.master.withdraw()
        mainwindow = MainWindow(tk.Toplevel(self.master), self.orderCount, self.userInfo, self.keyPrices, self.infoSubmitted)