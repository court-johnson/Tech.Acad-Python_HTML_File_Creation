from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import webbrowser
import os.path
#------------------------------------------------------------------------------------------
#html script to be created 
script = """<html>
<body>
%s
</body>
</html>"""

#------------------------------------------------------------------------------------------
class Feedback():

    def __init__(self, master):
   
        master.title('Create HTML Document')
        master.resizable(False, False)

        #styling of the label, frame, button
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#85adad')
        self.style.configure('TButton', background = '#527a7a')
        self.style.configure('TLabel', background = '#85adad', font = ('Arial', 11))
        
        #creating the frame of the window
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        #label indicating to use the text box to enter in what should be entered into the html script
        ttk.Label(self.frame_content, text = "Please enter the text to be inserted:", style = 'TLabel').grid(row = 0, column = 0, padx = 10, pady = 10, sticky = 'w')
        self.enteredText = Text(self.frame_content, width = 30, height = 10, borderwidth = 3)
        self.enteredText.grid(row=1,column=0, padx = 10, sticky = 'w')
        
        #button that binds to the create html file function
        self.createFile = ttk.Button(self.frame_content, text='Create to Web Browser', style='TButton')
        self.createFile.grid(row = 2, column = 0, padx = 7, pady = 10, sticky = 'e')
        self.createFile.bind("<Button-1>", self.createButtonClicked)

#------------------------------------------------------------------------------------------
    def createButtonClicked(self, event):
        #indicating to create a file under a particular name
        file = open("test.html", 'w')
        
        #writing the file with the text entered in from the text box by the user
        file.write(script % self.enteredText.get('1.0', END))
        file.close()

        #opening the file to the default web browser automatically
        webbrowser.open(os.path.abspath("test.html"))
        file.close()
#------------------------------------------------------------------------------------------

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()

if __name__ == '__main__':
    main()

