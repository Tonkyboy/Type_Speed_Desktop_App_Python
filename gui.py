from tkinter import *
from tkinter import ttk
from typing_classes import TypeSpeedTrainer
from time import sleep
from tkinter import messagebox
from articles import articles

quote = "Start the Game. :)"

TIMER = 50

strokes_messagebox = 0
errors_messagebox = 0
timer = 0

root = Tk()

tst = TypeSpeedTrainer()

root.title("Typing Speed Trainer")

root.minsize(width=200, height=350)
root.config(padx=50, pady=50)

root.resizable(True, True)


def print_entry_text(a, b, c):
    """Handles the Text input to fill up to 25 char and the delete the first to see always 25 chars - also writtes
    the text a textfile"""
    text = entry_text.get()
    if len(text) == 25:
        # print(text[:1])
        entry_text.set(text[-24:])
        tst.written_text_to_csv(text[-1:])
    elif len(text) < 25:
        tst.written_text_to_csv(text[-1:])


def text_correction(a):
    """Delete the last input from written_text.txt by pressing the <BackSpace> in the input_text"""
    text = tst.read_written_txt()[0]
    # print(text)
    tst.clear_written_text()
    tst.written_text_to_csv(text[0:-2])

def start_timer():
    """ Starts the timer whit a message box with results when the timer hits 0 sec"""
    global timer
    if timer > 0:
        sleep(1)
        timer -= 1
        timer_label.config(text=f"{timer} sec")
        root.after(1000, start_timer)
        # print(timer)
    elif timer == 0:
        messagebox.showinfo("Finished", f"Time is out! \n You scored {strokes_messagebox} strokes in {timer} sec\n "
                                        f"with {errors_messagebox} errors.")

def restart():
    tst.restart()
    global timer
    timer = TIMER
    entry_text.set("")
    run_text_operation()
    start()

def run_text_operation():
    global quote
    written_text_count = tst.read_written_txt()[1]
    # print(written_text_count)
    if written_text_count < 25:
        text.delete(1.0, END)
        text.insert(END, quote[:75])
    else:
        quote_start = written_text_count - 25
        quote_end = written_text_count + 25
        text.delete(1.0, END)
        text.insert(END, quote[quote_start:quote_end])
    root.after(250, run_text_operation)

def compare():
    compared, errors, string_count = tst.compare_to_input()
    if not compared:
        input_text.config(foreground="red")
    if compared:
        input_text.config(foreground="black")
    errors_label.config(text=f"Errors: {errors}")
    score_label.config(text=f"{string_count} strokes/ min")
    global strokes_messagebox
    strokes_messagebox = string_count
    global errors_messagebox
    errors_messagebox = errors
    root.after(250, compare)

def start():
    # load inital article
    global quote
    quote = articles[0]

    global timer
    timer = TIMER

    # reset textfile
    tst.clear_written_text()

    start_timer()
    run_text_operation()
    input_text.focus()
    compare()



frm = ttk.Frame(root, width=80, height=80, padding=15)
frm.grid(column=1, row=1)

ttk.Button(frm, text="Start", command=start).grid(column=1, row=1)
ttk.Button(frm, text="Restart", command=restart).grid(column=2, row=1)

score_label = ttk.Label(frm, text="0 strokes/min", width=25, font=("Courier", 25))
score_label.grid(column=1, row=2, columnspan=1, padx=25, pady=10)

errors_label = ttk.Label(frm, text="0 errors", width=25, font=("Courier", 25))
errors_label.grid(column=1, row=3, columnspan=1, padx=25, pady=10)

timer_label = ttk.Label(frm, text=f"{timer} sec", width=10, font=("Courier", 25))
timer_label.grid(column=2, row=2, columnspan=1, padx=25, pady=25)

text = Text(frm, height=3, width=50, font=("Courier", 35))
text.grid(column=1, row=4, columnspan=2, padx=25, pady=25)
text.insert(END, quote)
# text.config(state=DISABLED)

# Full Text Entry Widget
entry_text = StringVar()
entry_text.set("")

input_text = ttk.Entry(frm, textvariable=entry_text, width=50, font=("Courier", 35))
# input_text.bind("<Return>", print_hello)
input_text.grid(column=1, row=5, columnspan=2, padx=25, pady=25)
entry_text.trace("w", print_entry_text)
input_text.bind("<BackSpace>", text_correction)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=6, columnspan=2)

root.mainloop()
