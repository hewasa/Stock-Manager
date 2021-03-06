from tkinter import *
from tkinter import ttk
from generateNumber import *
from popupWindows import *
import json

jsonfile = "database.json"

def loadJson():
    with open(jsonfile) as json_data:
        return json.load(json_data)


def createNewProduct(name, category, price, stock, stock_alert, upc, windowAdd, tree):
    if name == "" or category == None or price == "" or stock == "" or stock_alert == "" or upc == "":
        printErrorWindow("empty input")

    elif isNumber(price) == False or isNumber(stock) == False or isNumber(stock_alert) == False:
        printErrorWindow("incorrect input: 'price', 'stock' and 'stock minimum' must be numbers")

    elif isCorrectUPC(upc) == False:
        printErrorWindow("incorrect UPC")

    elif isNumber(name) == True:
        printErrorWindow("name must not be a number")
    
    else:
        #creating the product object
        newProduct = {}
        newProduct["id"] = generateId()
        newProduct["name"] = name
        newProduct["category"] = category
        newProduct["price"] = price
        newProduct["stock"] = stock
        newProduct["stock_alert"] = stock_alert
        newProduct["UPC"] = str(upc)

        #insert the product in the treeview
        tree.insert("" , "end", text=newProduct["name"], values=(newProduct["name"], newProduct["category"], newProduct["price"], newProduct["stock"], newProduct["stock_alert"], str(newProduct["UPC"]), newProduct["id"]))

        windowAdd.destroy()
        printValidationWindow("Your product has been temporary added.\nClick on save to push the modifications to the database")
        
def fulfillEntryRandom(name, category, price, stock, stock_alert, upc):
    name.delete(0,END)
    price.delete(0,END)
    stock.delete(0,END)
    stock_alert.delete(0,END)
    upc.delete(0,END)
    name.insert(0, generateNameProduct())
    category.selection_set(0)
    price.insert(0, generatePrice())
    stk = generateStockandStockLimit()
    stock.insert(0, stk[0])
    stock_alert.insert(0, stk[1])
    upc.insert(0, generateUPC())

def addProduct(tree):
    windowAdd = Tk()
    windowAdd.title("Add a new product")
    categories = ["Vegetables", "Fruits", "Seafood", "Beverages", "Cheese", "Meat", "Snack"]

    
    #label
    txt1 = Label(windowAdd, text="Name:")
    txt2 = Label(windowAdd, text="Price:")
    txt3 = Label(windowAdd, text="Category:")
    txt4 = Label(windowAdd, text="Stock:")
    txt5 = Label(windowAdd, text="Stock minimum:")
    txt6 = Label(windowAdd, text="UPC:")

    #entry
    name = Entry(windowAdd)
    price = Entry(windowAdd)    
    stock = Entry(windowAdd)
    stock_alert = Entry(windowAdd)
    upc = Entry(windowAdd)
    
    #category listbox
    frame = Frame(windowAdd)
    scrollbar = Scrollbar(frame, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    category = Listbox(frame, yscrollcommand=scrollbar.set, height=3)
    category.pack()
    for cat in categories:
        category.insert(END, cat)
    scrollbar.config(command=category.yview)

    #grid
    txt1.grid(row=1, sticky=E, padx=10)
    txt2.grid(row=2, sticky=E, padx=10)
    txt3.grid(row=3, sticky=E, padx=10)
    txt4.grid(row=1, column=3, padx=40)
    txt5.grid(row=2, column=3, padx=40)
    txt6.grid(row=3, column=3, padx=40)
    name.grid(row=1, column=2, padx=10,pady=10)
    frame.grid(row=3, column=2, padx=10,pady=10)
    price.grid(row=2, column=2, padx=10,pady=10)
    stock.grid(row=1, column=4, padx=10,pady=10)
    stock_alert.grid(row=2, column=4, padx=10,pady=10)
    upc.grid(row=3, column=4, padx=10,pady=10)

    #button
    submit = Button(windowAdd, text="Submit", command=lambda: createNewProduct(name.get(), category.get(category.curselection()), price.get(), stock.get(), stock_alert.get(), upc.get(), windowAdd, tree))
    generate = Button(windowAdd, text="Generate random", command=lambda: fulfillEntryRandom(name, category, price, stock, stock_alert, upc))
    submit.grid(row=4, column=4, pady=20)
    generate.grid(row=4, column=2, padx=10)
