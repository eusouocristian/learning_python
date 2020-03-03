import tkinter
from tkinter import messagebox

DEFALUT_GAP = 60 * 25   # 25 min to sec
DEFALUT_GAP = 10

class Pymodoro:
    def __init__(self, master):
        self.master = master
        #set de main frame as a white window for the master objetct (root)
        self.mainframe = tkinter.Frame(self.master, bg='white')
        self.mainframe.pack(fill=tkinter.BOTH, expand=True)

        # create a string variable tu be used inside the Label of build_timer()
        self.time_text = tkinter.StringVar()

        #reconstroi o timer na janela sempre que a variavel for alterada
        self.time_text.trace('w', self.build_timer)

        # create a int variable to handle the time left
        self.time_left = tkinter.IntVar()

        #reconstroi o timer na janela sempre que a variavel for alterada
        self.time_left.trace('w', self.alert)

        # set the value of the variable
        self.time_left.set(DEFALUT_GAP)

        # create a flag to check if the clock is running or not, default is False
        self.running = False

        # calling the methods created below
        self.build_grid()
        self.build_banner()
        self.build_buttons()
        self.build_timer()
        self.update()

    def build_grid(self):
        #build 1 column and 3 lines (top, middle, bottom)
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=0) # top line
        self.mainframe.rowconfigure(1, weight=1) # middle line
        self.mainframe.rowconfigure(2, weight=0) # bottom line
    
    def build_banner(self):
        # build a banner in the mainframe
        banner = tkinter.Label(
            self.mainframe,
            bg='red',
            fg='white',
            text='Pymodoro',
            font=('Helvetica', 24)
        )
        # put the banner on the grid
        banner.grid(
            row=0, column=0, # set the position on the created grid 
            sticky='we', # 'we' -> west-east, or 'ns' -> north-south, 'nsew' -> north-shouth/east-west
            padx=10, pady=10
        )
    
    def build_buttons(self):
        #build a new frame inside de mainframe:
        buttuns_frame = tkinter.Frame(self.mainframe)
        # put the buttuns frame into the original grid, line 2
        buttuns_frame.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)
        # create two columns to put each button
        buttuns_frame.columnconfigure(0, weight=1)
        buttuns_frame.columnconfigure(1, weight=1)

        # create buttons itself
        self.start_button = tkinter.Button(
            buttuns_frame, text='Start',
            command=self.start_timer
        )
        self.stop_button = tkinter.Button(
            buttuns_frame, text='Stop',
            command=self.stop_timer
        )

        # set the buttons position 
        self.start_button.grid(row=0, column=0, sticky='ew')
        self.stop_button.grid(row=0, column=1, sticky='ew')
        #set the inicial condicion for stop button as DISABLED
        self.stop_button.config(state=tkinter.DISABLED)

    def build_timer(self, *args):
        timer = tkinter.Label(
            self.mainframe,
            text=self.time_text.get(),
            font=('Helvetica', 36),
        )
        timer.grid(row=1, column=0, sticky='nsew')
    
    def start_timer(self):
        self.time_left.set(DEFALUT_GAP)
        self.running = True
        #turn able the stop button and disable the start button
        self.stop_button.config(state=tkinter.NORMAL)
        self.start_button.config(state=tkinter.DISABLED)

    
    def stop_timer(self):
        self.running = False
        #turn DISABLED the stop button and abled the start button
        self.stop_button.config(state=tkinter.DISABLED)
        self.start_button.config(state=tkinter.NORMAL)
    
    def minutes_seconds(self, seconds): #takes the number of seconds 
        return (int(seconds/60), int(seconds%60)) #returns a tuple (min, sec)
    
    def update(self):
        # add a new variable to simplify this part
        time_left = self.time_left.get()

        #if the flag self.running is True and there is time left:
        if self.running and time_left:
            # extract the tuple to minuts, seconds from time_left
            minutes, seconds = self.minutes_seconds(time_left)
            # set the time_text (to be printed)
            self.time_text.set('{:0>2}:{:0>2}'.format(minutes, seconds))
            # set the new time_left
            self.time_left.set(time_left-1)
        else: # else, set the time_text as the default time and stop timer
            minutes, seconds = self.minutes_seconds(DEFALUT_GAP)
            self.time_text.set('{:0>2}:{:0>2}'.format(minutes, seconds))
            self.stop_timer()

        # method to run self.update after 1000ms
        self.master.after(1000, self.update)

    def alert(self, *args):
        if not self.time_left.get():
            messagebox.showinfo('Timer Done!', 'Your time is done!')


if __name__ == '__main__':
    root = tkinter.Tk()
    Pymodoro(root)
    root.mainloop()
