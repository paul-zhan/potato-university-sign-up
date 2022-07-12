import tkinter as tk
from system import *

def main():

    window = tk.Tk()
    window.geometry('400x400')

   
    # display_front is the object for the class Front_page 
    display_front = Front_page(window)
    display_front.drawing()


if __name__ == "__main__":
    main()
