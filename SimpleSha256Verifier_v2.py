# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 15:24:25 2023

@author: Dimitris Rigas Papakonstantinou
Version: v2
"""

# import all functions from the tkinter   
from tkinter import *
 
  
# Function to verify the SHA-256
def check_sha() :
  
    
    sha1 = str(sha1Field.get())
    sha2 = str(sha2Field.get())
    
    result = sha1 == sha2
    resultField.insert(10, str(result))
      
# Function for clearing the boxes  
def Clear():
    sha1Field.delete(0, END)
      
    sha2Field.delete(0, END)
      
    resultField.delete(0, END)
      
  
# Main Code
if __name__ == "__main__" :
  

    gui = Tk()
    gui.configure(background = "light blue")
    gui.title("sha verifier by Dimitris Rigas Papakonstantinou")
    gui.geometry("600x300")
  
    # Create a sha1 label
    sha1 = Label(gui, text = "SHA1", bg = "red")
  
    # Create a sha2 label
    sha2 = Label(gui, text = "SHA2", bg = "red")
  
    #Create the check button, and specify which function to call
    check = Button(gui, text = "Check SHA",
                  fg = "Black", bg = "Red",
                  command = check_sha)
      
    result1 = Label(gui, text = "Verified??", bg = "red")
  
    # Create the Clear Button 
    clear = Button(gui, text = "Clear",
                   fg = "Black", bg = "Red",
                   command = Clear)
  
    #Properties of where to place each label   
    sha1.grid(row = 1, column = 1,padx = 10)
                      
    sha2.grid(row = 2, column = 1, padx = 10)
    
    result1.grid(row = 5, column = 1,padx = 10)
    
    #Properties of where to place each button  
    check.grid(row = 3, column = 2,pady = 10)
      
    clear.grid(row = 6, column = 2,pady = 10)
  
      
    #Create the text entry boxes
    sha1Field = Entry(gui, width = 80)
      
    sha2Field = Entry(gui, width = 80)
      
    resultField = Entry(gui)
  
    #Properties of where to place each entry box.  
    sha1Field.grid(row = 1, column = 2)
      
    sha2Field.grid(row = 2, column = 2)
      
    check.grid(row = 4, column = 2)
    
    resultField.grid(row = 5, column = 2)
    
    #Start of the window
    gui.mainloop()
