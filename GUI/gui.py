import tkinter

root = tkinter.Tk()


hi_there = tkinter.Label(
    root, #the related object
    text='hi there', 
    bg='red', #background colour
    fg='white'  #foreground (font) colour
    )
hi_there.pack(fill=tkinter.BOTH, expand=True)  # fill=tkinter.X, fill = tkinter.Y

my_name = tkinter.Label(
    root,
    text='My name is Cristian',
)
my_name.pack()

root.mainloop()