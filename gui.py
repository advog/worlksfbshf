from tkinter import *

global count
global Xwin
global Owin

count = 0
Xwin = 0
Owin = 0

tk = Tk()
tk.title("Tic Tac Toe")

bclick = True



def reset():
    button1.config(text=" ")
    button2.config(text=" ")
    button3.config(text=" ")
    button4.config(text=" ")
    button5.config(text=" ")
    button6.config(text=" ")
    button7.config(text=" ")
    button8.config(text=" ")
    button9.config(text=" ")
    score.config(text=" ")
    f.config(text = 'XW: '+str(Xwin)+ ' OW:' + str(Owin))


def logic(buttons):
    global bclick

    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        count = count + 1
    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        count = count +1

    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
          button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
          button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
          score.config(text="X Wins")
          Xwin = Xwin+1

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
          score.config(text="O Wins")
          Owin = Owin+1

    elif count == 9:
        count = 0
        score.config(text="Tie")



buttons = StringVar()

button1 = Button(tk, text=" ", height=4, width=8,
                 command=lambda: logic(button1))
button1.grid(row=1, column=0)

button2 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button2))
button2.grid(row=1, column=1)

button3 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button3))
button3.grid(row=1, column=2)

button4 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button4))
button4.grid(row=2, column=0)

button5 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button5))
button5.grid(row=2, column=1)

button6 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button6))
button6.grid(row=2, column=2)

button7 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button7))
button7.grid(row=3, column=0)

button8 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button8))
button8.grid(row=3, column=1)

button9 = Button(tk, text=' ', height=4, width=8,
                 command=lambda: logic(button9))
button9.grid(row=3, column=2)

res = Button(tk, text='reset', height=4, width=8,
                 command= reset)
res.grid(row=4, column=2)

score = Button(tk, text='', height=4, width=8,
                 command= reset)
score.grid(row=4, column=0)

f = Button(tk, text = '', height=4, width=8,
                 command= reset)
f.grid(row=4, column=1)

tk.mainloop()



