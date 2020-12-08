try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("tkinter demo")
mainWindow.geometry('640x480+8+400')

label = tkinter.Label(mainWindow, text="Hello tkinter")
label.pack(side='bottom')

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=3)
canvas.pack(side='left', anchor='n')

canvas.create_text(100,100,fill="darkblue",font="Times 20 italic bold",
                   text="Click the bubbles that are multiples of two.")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side='right', anchor='n', expand=True)
button1 = tkinter.Button(rightFrame, text="button1")
button2 = tkinter.Button(rightFrame, text="button2")
button3 = tkinter.Button(rightFrame, text="button3")
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

bottomFrame = tkinter.Frame(mainWindow)
bottomFrame.pack(side='left', anchor='n', expand=True)
button4 = tkinter.Button(bottomFrame, text="buttonNew")
button4.pack(side='top')
mainWindow.mainloop()
