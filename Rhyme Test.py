from tkinter import *
from tkinter import filedialog

class program:
    def __init__(self,master):
        master.title("Ομοιοκαταληξία")
        master.geometry("600x500+500+200")
        master.configure(background = "blue")
        self.label = Label(master, text = "Με ποια λέξη θες να κάνει ομοιοκαταληξεία")
        self.label.grid()
        global entry
        entry = self.entry = Entry()
        entry.grid()
        self.Two_Button = Button(master, text = "Ομοιοκαταληξία με 2 γράμματα", command = lambda: self.code(2))
        self.Two_Button.grid()
        self.Three_Button = Button(master, text = "Ομοιοκαταληξία με 3 γράμματα", command = lambda: self.code(3))
        self.Three_Button.grid()
        self.Four_Button = Button(master, text = "Ομοιοκαταληξία με 4 γράμματα", command = lambda: self.code(4))
        self.Four_Button.grid()
        self.Menubar = Menu(master)
        self.filemenu = Menu(self.Menubar,tearoff=0)
        self.filemenu.add_command(label = "Open...",command = self.Filename)
        self.Menubar.add_cascade(label = "File",menu = self.filemenu)
        master.config(menu=self.Menubar)

    def Filename(self):
        global File
        File = filedialog.askopenfilename(title = "Select Word List"    )
    
    def code(self,value):
        Word = entry.get()
        vowels = ["Α","Ε","Ι","Ο","Υ","Ω","Η","ΟΥ","ΕΙ","ΕΥ","ΑΙ","ΑΥ","ΟΙ"] 
        Num = 0
        Num1 = 0
        for i in Word:
            if i in vowels:
                Num += 1
        frame = self.frame = Frame(root)
        frame.grid(row = 5, sticky = W+E)
        rhyme = Word[-value:]
        File = open("greek.txt", encoding = "utf8")
        Words = File.readlines()
        scrollbar = self.scrollbar = Scrollbar(frame)
        scrollbar.pack(side = RIGHT, fill = BOTH)
        listbox = self.listbox = Listbox(frame)
        listbox.pack(fill = BOTH)
        listbox.insert(END,"Λέξεις που βρέθηκαν")
        for List_Word in Words:
            Word_Rhyme = List_Word[-value-1:-1]
            if Word_Rhyme == rhyme:
                for I in List_Word:
                    if I in vowels:
                        Num1 += 1

                if Num1 == Num:
                    listbox.insert(END, List_Word)
                Num1 = 0
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command=listbox.yview)        
        File.close()
        


root = Tk()
x = program(root)
root.mainloop()
