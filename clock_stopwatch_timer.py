import datetime
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def date_time():
    """ Gets the date and time, send it to the label and updates itself every 200 ms """

    now = datetime.datetime.now()
    date = now.strftime("%d %b %Y")
    time1 = now.strftime("%H:%M:%S")
    calendar.config(text=date)
    clock.config(text=time1)
    clock.after(200, date_time)


class StopWatch:
    """
    A class used to create a stopwatch

    Attributes
    ----------
    label : Label
        widget to show the time
    running : Bolean
        a flag to signal if stop button is pressed or not
    hundredth_seconds : int
        the hundredth seconds
    seconds : int
        the seconds
    minutes: int
        the minutes
    str_time: StringVar
        a string to set the time format

    Methods
    -------
    start_stopwatch()
        Increments the hundredth_seconds, minutes and seconds
    stop()
        stops the stopwatch
    start()
        starts the stopwatch
    reset()
        resets the stopwatch
    set_time()
        sets the time format
    """

    def __init__(self, label):
        """
        Parameters
        ----------
        label : Label
            widget to show the time
        """
        self.label = label
        self.running = False
        self.hundredth_seconds = 0
        self.seconds = 0
        self.minutes = 0
        self.str_time = StringVar()

    def start_stopwatch(self):
        """
        Increments the hundredth seconds, seconds and minutes and send them to the label.
        If the stop is pressed, ignores
        """
        if self.running:
            self.hundredth_seconds += 1
            if self.hundredth_seconds >= 100:
                self.hundredth_seconds = 0
                self.seconds += 1
            if self.seconds >= 60:
                self.minutes += 1
                self.seconds = 0
            self.label.config(text=self.set_time(self.hundredth_seconds, self.seconds, self.minutes))
            if self.minutes == 59:
                self.reset()
        self.label.after(10, self.start_stopwatch)

    def start(self):
        """
        Sets the running flag to true and calls the start_stopwatch method
        if the stop is not pressed.
        """

        if not self.running:
            self.running = True
        self.start_stopwatch()

    def stop(self):
        """ Stops the stopwatch. """

        if self.running:
            self.running = False
        self.start_stopwatch()

    def reset(self):
        """ Resets the stopwatch to 00:00.00. """

        self.hundredth_seconds = 0
        self.seconds = 0
        self.minutes = 0
        self.label.config(text=self.set_time(self.hundredth_seconds, self.seconds, self.minutes))

    def set_time(self, hundredth_seconds, seconds, minutes):
        """ sets the format of the time string str_time.

        Parameters
        ----------
        hundredth_seconds : int
            the hundredth seconds
        seconds : int
            the seconds
        minutes: int
            the minutes

        Returns
        -------
        str_time
            a string variable containing the formatted time
        """

        self.hundredth_seconds = hundredth_seconds
        self.seconds = seconds
        self.minutes = minutes
        self.str_time = ("%02d:%02d.%02d" % (self.minutes, self.seconds, self.hundredth_seconds))
        return self.str_time


class CountDown:
    """
    A class used to create a timer

    Attributes
    ----------
    hours : int
        the hours
    minutes : int
        the minutes
    seconds : int
        the seconds
    label : Label
        widget to show the time
    str_time: StringVar
        a string to set the time format

    Methods
    -------
    get_input_time()
        gets the selections from the entry box
    start_countdown()
        starts the timer
    cancel_countdown()
        cancels the timer
    """

    def __init__(self, label):
        """
        Parameters
        ----------
        label : Label
            widget to show the time
        """

        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.label = label
        self.str_time = StringVar()

    def get_input_time(self):
        """Gets selected the values from the entry box."""
        invalid_entry = False
        try:
            self.hours = int(hours_.get())
            self.minutes = int(minutes_.get())
            self.seconds = int(seconds_.get())
        except ValueError:
            messagebox.showerror("Error", "ONLY INTEGERS ARE VALID!")
            self.cancel_countdown()

        try:
            if self.hours < 0 or self.hours > 23:
                invalid_entry = True
            if self.minutes < 0 or self.minutes > 59:
                invalid_entry = True
            if self.seconds < 0 or self.seconds > 59:
                invalid_entry = True

        except ValueError:
            messagebox.showerror("Error", "ONLY POSITIVES INTEGERS WITHIN THE RANGE (0-23) FOR HOURS AND "
                                          "(0-59) FOR MINUTES AND SECONDS ARE VALID!")
            self.cancel_countdown()

        if not invalid_entry:
            self.start_countdown()
        else:
            messagebox.showerror("Error", "ONLY POSITIVES INTEGERS WITHIN THE RANGE (0-23) FOR HOURS AND "
                                          "(0-59) FOR MINUTES AND SECONDS ARE VALID!")
            self.cancel_countdown()

    def start_countdown(self):
        """
        Starts the timer and decrements the hours, minutes and seconds.
        Formats and send the time string str_time to the label.
        """

        self.str_time = ("%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds))
        self.label.config(text=self.str_time)

        if self.hours > 0 or self.minutes > 0 or self.seconds > 0:

            self.label.after(1000, self.start_countdown)

            if self.seconds == 0 and self.minutes > 0 and self.hours > 0:

                self.seconds = 60
                self.minutes -= 1

            elif self.seconds == 0 and self.minutes > 0 and self.hours == 0:

                self.seconds = 60
                self.minutes -= 1

            elif self.seconds == 0 and self.minutes == 0 and self.hours > 0:

                self.seconds = 60
                self.minutes = 59
                self.hours -= 1

        elif self.hours == 0 and self.minutes == 0 and self.seconds == 0:

            self.cancel_countdown()

        self.seconds -= 1

    def cancel_countdown(self):
        """Cancels the timer, formats the time string srt_time and send it to the label"""

        self.seconds = 0
        self.minutes = 0
        self.hours = 0
        self.str_time = ("%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds))
        self.label.config(text=self.str_time)


'printing code documentation'
help(date_time)
help(StopWatch)
help(CountDown)

'''###############################################################################'''
'''##################################### GUI #####################################'''
'''###############################################################################'''
root = Tk()
root.geometry('500x400')
root.title("Special Clock")
Button(root, text='Exit', command=root.destroy).pack(side=BOTTOM)

s = ttk.Style()
s.theme_use('clam')

'''create tabs'''
note = ttk.Notebook(root)
tab1 = Frame(note)
tab2 = Frame(note)
tab3 = Frame(note)
note.add(tab1, text="Clock")
note.add(tab2, text="Stopwatch")
note.add(tab3, text="Countdown")
note.pack(anchor=CENTER, fill=BOTH, expand=TRUE)

'''displays current time and date on tab1'''
clock = ttk.Label(tab1, font=('times', 80, 'bold'), background='white')
calendar = ttk.Label(tab1, font=('times', 40, 'bold'), background='white')
clock.pack()
calendar.pack(pady=10)
date_time()

'''stopwatch on tab2'''
label0 = ttk.Label(tab2, text='00:00:00', font=('times', 70), background='white')
label0.pack()

sw = StopWatch(label0)

Button(tab2, width=10, text='Start', command=sw.start, fg="green", padx=10, pady=10).pack(pady=10)
Button(tab2, width=10, text='Stop', command=sw.stop, fg="red", padx=10, pady=10).pack(pady=10)
Button(tab2, width=10, text='Reset', command=sw.reset, fg="blue", padx=10, pady=10).pack(pady=10)

'''Countdown timer on tab3'''
label1 = ttk.Label(tab3, text='00:00:00', font=('times', 70), background='white')
label1.pack()
timer = CountDown(label1)

Button(tab3, command=timer.get_input_time, width=9, height=2, text='Start', fg="green").pack(anchor=CENTER, fill=X, pady=10)
Button(tab3, command=timer.cancel_countdown, width=9, height=2, text='Cancel', fg="green").pack(anchor=CENTER, fill=X, pady=10)

ttk.Label(tab3, text='Hours', font=('times', 10, ), background='white').pack(side=LEFT, anchor=CENTER, fill=X)
hours_ = Spinbox(tab3, width=3, from_=0, to=23)
hours_.pack(side=LEFT, ipadx=5, anchor=CENTER, expand=TRUE, fill=X)
ttk.Label(tab3, text='Minutes', font=('times', 10), background='white').pack(side=LEFT, anchor=CENTER, fill=X)
minutes_ = Spinbox(tab3, width=3, from_=0, to=59)
minutes_.pack(side=LEFT, ipadx=5, anchor=CENTER, expand=TRUE, fill=X)
ttk.Label(tab3, text='Seconds', font=('times', 10), background='white').pack(side=LEFT, anchor=CENTER, fill=X)
seconds_ = Spinbox(tab3, width=3, from_=0, to=59)
seconds_.pack(side=LEFT, ipadx=5, anchor=CENTER, expand=TRUE, fill=X)

root.mainloop()


