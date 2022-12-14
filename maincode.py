from itertools import count
from tkinter import *
from tkinter import messagebox

#Function for the button clicked
def b_click(b):
    global clicked, count
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkforwin()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkforwin()
    else:
        messagebox.showerror("Tic Tac Toe", "Box already chosen. Choose another box" )

def checkforwin():
    global win
    win = False

    #X wins the game
    if (b1["text"] == b2["text"] == b3["text"] == "X"):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b4["text"] == b5["text"] == b6["text"] == "X"):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b7["text"] == b8["text"] == b9["text"] == "X"):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b1["text"] == b5["text"] == b9["text"] == "X"):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b3["text"] == b5["text"] == b7["text"] == "X"):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b1["text"] == b4["text"] == b7["text"] == "X"):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b2["text"] == b5["text"] == b8["text"] == "X"):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    elif (b3["text"] == b6["text"] == b9["text"] == "X"):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "X wins the game!")
        disablebuttons()
    
    #O wins the game
    elif (b1["text"] == b2["text"] == b3["text"] == "O"):
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b4["text"] == b5["text"] == b6["text"] == "O"):
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b7["text"] == b8["text"] == b9["text"] == "O"):
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b1["text"] == b5["text"] == b9["text"] == "O"):
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b3["text"] == b5["text"] == b7["text"] == "O"):
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b1["text"] == b4["text"] == b7["text"] == "O"):
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b2["text"] == b5["text"] == b8["text"] == "O"):
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    elif (b3["text"] == b6["text"] == b9["text"] == "O"):
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        win = True
        messagebox.showinfo("Tic Tac Toe", "O wins the game!")
        disablebuttons()
    
    if count == 9  and win == False:
        messagebox.showinfo("Tic Tac Toe", "Tie in the game!")
        disablebuttons()

def disablebuttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    #Build buttons
    b1 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font="Calibri 20", height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))
    #Make a grid with the buttons
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

if __name__ == "__main__":
    root =Tk()
    root.title("Tic Tac Toe game")
    root.configure(background="black")
    #X is starting the game:
    clicked = True
    count = 0
    
    mymenu= Menu(root)
    root.config(menu=mymenu)

    #create options menu
    omenu= Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="Options", menu=omenu)
    omenu.add_command(label="New game", command=reset)
    reset()
    root.mainloop()