from tkinter import *

root = Tk()
root.geometry("900x600")
root.title("Classes")
root.configure(bg="blue")

class CreateElements:
    
    def __init__(self):
        print("This is CreateElements class")
        
    def createNewElements(self):
        label= Label(root,text="Click The Button Below",bg="yellow", fg="red", font="Algerian")
        label.pack()
        btn = Button(root, text="Click ME !",bg="yellow",fg="red",font="Algerian", command= self.message)
        btn.pack(padx=20, pady=10)
        
    def message(self):
        messagebox.showinfo("show info", "🍥🎂🍰 Happy Birthday To You",)
        
obj_of_CreateElements = CreateElements()

btn = Button(root, text ="Click for a surprise",bg="yellow",fg="red",font="Algerian", command=obj_of_CreateElements.createNewElements)
btn.pack(padx=20, pady=10)

root.mainloop()