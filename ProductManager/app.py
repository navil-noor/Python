import sqlite3
from tkinter import ttk
from tkinter import *


class Product:
    db = 'database/products.db'  # db variable to access the database route

    def __init__(self, root):
        self.window = root
        self.window.title("Product Manager App")  # Title of the window
        self.window.resizable(1, 1)  # Resize the window. To disable (0, 0)
        self.window.wm_iconbitmap("resources/icon.ico")

        # Create the main container Frame
        frame = LabelFrame(self.window, text="Register a new Product", font=('Calibri', 16, 'bold'))
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        # Name Label
        self.label_name = Label(frame, text="Name: ", font=('Calibri', 13))  # Text label in the frame
        self.label_name.grid(row=1, column=0)  # Positioning through grid
        # Entry name (text box that receives the name)
        self.name = Entry(frame, font=('Calibri', 13))  # Text box (text input) in the frame
        self.name.focus()  # For the mouse cursor to go straight to this Entry
        self.name.grid(row=1, column=1)

        # Price Label
        self.label_price = Label(frame, text="Price: ", font=('Calibri', 13))  # Text label in the frame
        self.label_price.grid(row=2, column=0)
        # Entry price (text box that receives the price)
        self.price = Entry(frame, font=('Calibri', 13))  # Text box (text input) in the frame
        self.price.grid(row=2, column=1)

        # Add Save Product button
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))  # Adding design to save product button
        self.button_add = ttk.Button(frame, text="Save Product", command=self.add_product, style='my.TButton')
        self.button_add.grid(row=3, columnspan=2, sticky=W + E)

        # Information message for the user
        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # Table of Products
        # Personalised style for the table
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 11))  # Modify the table's font
        style.configure("mystlye.Treeview.Heading", font=('Calibri', 13, "bold"))  # Modify the heading font
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea',
                                           {'sticky': 'nswe'})])  # Remove the borders

        # Structure of the table
        self.table = ttk.Treeview(height=20, columns=2, style="mystyle.Treeview")
        self.table.grid(row=4, column=0, columnspan=2)
        self.table.heading('#0', text='Name', anchor=CENTER)  # Heading 0
        self.table.heading('#1', text='Price', anchor=CENTER)  # Heading 1

        # Delete and Edit buttons
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        button_delete = ttk.Button(text='DELETE', command=self.del_product, style='my.TButton')
        button_delete.grid(row=5, column=0, sticky=W + E)
        button_edit = ttk.Button(text='EDIT', command=self.edit_product, style='my.TButton')
        button_edit.grid(row=5, column=1, sticky=W + E)

        # Call to get_products() method to get the list of products at the beginning of the app
        self.get_products()

    def db_query(self, query, parameters=()):
        with sqlite3.connect(self.db) as con:  # Start a connection with the database (con)
            cursor = con.cursor()  # Generate a cursor of the connection to be able to operate in the database
            result = cursor.execute(query, parameters)  # Prepare the SQL query (with parameters if any)
            con.commit()  # Run the prepared SQL query
        return result  # Return the result of the SQL query

    def get_products(self):
        # When starting the app, clean the table in case there is residual or old data
        records_table = self.table.get_children()  # Obtain all the data of the table
        for row in records_table:
            self.table.delete(row)

        # SQL query
        query = "SELECT * FROM product ORDER by name DESC"
        records_db = self.db_query(query)  # Call to method db_query

        # Write the data on the screen
        for row in records_db:
            print(row)  # print to check the data by console
            self.table.insert('', 0, text=row[1], values=row[2])

    def validate_name(self):
        name_inserted_by_user = self.name.get()
        return len(name_inserted_by_user) != 0

    def validate_price(self):
        name_inserted_by_user = self.price.get()
        return len(name_inserted_by_user) != 0

    def add_product(self):
        if self.validate_name() and self.validate_price():
            query = 'INSERT INTO product VALUES(NULL, ?, ?)'  # Query SQL (without data)
            parameters = (self.name.get(), self.price.get())  # Parameters of the SQL query
            self.db_query(query, parameters)
            self.message['text'] = 'Product {} added successfully'.format(self.name.get())  # Label located between
            # the button and the table
            self.name.delete(0, END)  # Clear the name field in the form
            self.price.delete(0, END)  # Clear the price field in the form

            # To debug
            # print(self.name.get())
            # print(self.price())
        elif self.validate_name() and self.validate_price() == False:
            self.message['text'] = "Price is mandatory"
        elif self.validate_name() == False and self.validate_price():
            self.message['text'] = "Name is mandatory"
        else:
            self.message['text'] = "Name and price are mandatory"

        self.get_products()  # When the data insertion is completed we invoke this method again to update the content
        # and see the changes

    def del_product(self):
        # For Debugging
        # print(self.table.item(self.table.selection()))
        # print(self.table.item(self.table.selection())['text'])
        # print(self.table.item(self.table.selection())['values'])
        # print(self.table.item(self.table.selection())['values'][0])

        self.message['text'] = ''  # Initial message is empty
        # Checking that a product is selected to remove it
        try:
            self.table.item(self.table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a product'
            return

        self.message['text'] = ''
        name = self.table.item(self.table.selection())['text']
        query = 'DELETE FROM product WHERE name = ?'  # SQL query
        self.db_query(query, (name,))  # Run query
        self.message['text'] = 'PRODUCT {} deleted successfully'.format(name)
        self.get_products()  # Update the products table

    def edit_product(self):
        self.message['text'] = ''  # Initial message is empty
        try:
            self.table.item(self.table.selection())['text'][0]
        except IndexError as e:
            self.message['text'] = 'Please select a product'
            return
        name = self.table.item(self.table.selection())['text']
        old_price = self.table.item(self.table.selection())['values'][0]  # The price is in a list

        # New window (edit product)
        self.window_edit = Toplevel()  # Create a window in front of the main one
        self.window_edit.title = "Edit Product"  # Title of the window
        self.window_edit.resizable(1, 1)  # Enable window resizing. (0,0) to disable.
        self.window_edit.wm_iconbitmap('resources/edit.ico')  # Edit window icon

        title = Label(self.window_edit, text='Edit Product', font=('Calibri', 50, 'bold'))
        title.grid(column=0, row=0)

        # Create the main container Frame of the Edit Product window
        # frame_ep: Edit Product Frame
        frame_ep = LabelFrame(self.window_edit, text="Edit the following product", font=('Calibri', 16, 'bold'))
        frame_ep.grid(row=1, column=0, columnspan=20, pady=20)

        # Old name Label
        self.label_name_old = Label(frame_ep, text="Old name: ", font=('Calibri', 13))  # Text label in the frame
        self.label_name_old.grid(row=2, column=0)  # Position with grid
        # Old name entry (cannot be edited)
        self.input_name_old = Entry(frame_ep, textvariable=StringVar(self.window_edit, value=name), state='readonly',
                                    font=('Calibri', 13))
        self.input_name_old.grid(row=2, column=1)

        # New name Label
        self.label_name_new = Label(frame_ep, text="New name: ", font=('Calibri', 13))
        self.label_name_new.grid(row=3, column=0)
        # New name entry (can be edited)
        self.input_name_new = Entry(frame_ep, font=('Calibri', 13))
        self.input_name_new.grid(row=3, column=1)
        self.input_name_new.focus()  # So the focus of the cursor goes to this Entry

        # Old price Label
        self.label_price_old = Label(frame_ep, text="Old price: ", font=('Calibri', 13))  # Text label in the frame
        self.label_price_old.grid(row=4, column=0)  # Grid positioning
        # Old price entry (cannot be edited)
        self.input_price_old = Entry(frame_ep, textvariable=StringVar(self.window_edit, value=old_price),
                                     state='readonly', font=('Calibri', 13))
        self.input_price_old.grid(row=4, column=1)

        # New price Label
        self.label_price_new = Label(frame_ep, text="New price: ", font=('Calibri', 13))
        self.label_price_new.grid(row=5, column=0)
        # New price entry (can be edited)
        self.input_price_new = Entry(frame_ep, font=('Calibri', 13))
        self.input_price_new.grid(row=5, column=1)

        # Update Product button
        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 14, 'bold'))
        self.button_update = ttk.Button(frame_ep, text="Update Product", style='my.TButton', command=lambda:
        self.update_products(self.input_name_new.get(),
                             self.input_name_old.get(),
                             self.input_price_new.get(),
                             self.input_price_old.get()))

        self.button_update.grid(row=6, columnspan=2, sticky=W+E)

    def update_products(self, new_name, old_name, new_price, old_price):
        product_modified = False
        query = 'UPDATE product SET name = ?, price = ? WHERE name = ? AND price = ?'
        if new_name != '' and new_price != '':
            # If user writes a new name and a new price, they will both change
            parameters = (new_name, new_price, old_name, old_price)
            product_modified = True
        elif new_name != '' and new_price == '':
            # If user leaves the new price empty, the old price is maintained
            product_modified = True
        elif new_name == '' and new_price != '':
            # If user leaves the new name empty, the old name is maintained
            product_modified = True

        if product_modified:
            self.db_query(query, (parameters))  # Run query
            self.window_edit.destroy()  # Close the edit products window
            self.message['text'] = 'The product {} has been updated successfully'.format(old_name)  # Show message
            self.get_products()  # Update the products table
        else:
            self.window_edit.destroy()  # Close the edit products window
            self.message['text'] = 'The product {} has NOT been updated'.format(old_name)  # Show message


if __name__ == '__main__':
    root = Tk()  # instance of the main window
    app = Product(root)  # Control over the root window is sent to the Product class
    root.mainloop()  # Start the main application loop, like a while True
