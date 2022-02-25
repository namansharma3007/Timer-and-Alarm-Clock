from tkinter import *
from time import *
from tkinter import ttk
import time
import datetime
from playsound import playsound

def setAlarm():
    alarmH = int(entry3.get())
    alarmM = int(entry4.get())
    amPm = str(entry5.get().lower())

    if (amPm == "pm"):
        alarmH += 12

    while True:

        if(alarmH == datetime.datetime.now().hour and alarmM == datetime.datetime.now().minute):

            time = f"{alarmH}"
            time2 = f"{alarmH-12}"
            min=f"{alarmM}"
            zone=f"{amPm}"
            if (amPm=="pm"):
                label7 = Label(tab2, font=("Nunito", 18), bg="#00ffbb")
                label7.grid(column=1, row=3, columnspan=2, padx=0, pady=0)
                label7.config(text="Its time for action!" + "\n"+time2+":"+min+" "+zone)
            else:
                label7 = Label(tab2, font=("Nunito", 18), bg="#00ffbb")
                label7.grid(column=1, row=3, columnspan=2, padx=0, pady=0)
                label7.config(text="Its time for action!" + "\n"+time+":"+min+" "+zone)
            window.update()
            playsound("alarm1.mp3")
            break


# def delete2():
#     entry3.delete(0, END)
#     entry4.delete(0, END)
#     entry5.delete(0, END)


def delete():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)


def start():

    mins = int(entry1.get())
    secs = int(entry2.get())
    min = mins*60
    tSecs = min+secs

    labelOutput = Label(tab1, font=("Nunito", 57), bg="#00ffbb")
    # labelOutput.pack(padx=0, pady=0)
    labelOutput.grid(column=0, row=3, columnspan=2, padx=0, pady=0)

    while tSecs:
        minsF = tSecs//60
        secsF = tSecs % 60
        timer = f'{minsF}:{secsF}'
        time.sleep(1)
        tSecs -= 1
        labelOutput.config(text=" "+timer+" ")
        window.update()

    playsound("timer.mp3")
    


window = Tk()
# window.geometry("300x500")
window.config(bg="#00ffbb")
window.title("Your Time Tracker!")

notebook = ttk.Notebook(window)

tab1 = Frame(notebook, bg="#00ffbb")
tab2 = Frame(notebook, bg="#00ffbb")

notebook.add(tab1, text="Timer")
notebook.add(tab2, text="Alarm")

notebook.pack(expand=True, fill="both")

label1 = Label(tab1, text="Mins", font=("Nunito", 16), bg="#00ffbb")
label1.grid(column=0, row=0)
entry1 = Entry(tab1,
               font=("Arial", 18),
               fg="black",
               bg="white", width=11)
entry1.grid(row=1, column=0, padx=3, pady=3)

label2 = Label(tab1, text="Secs", font=("Nunito", 16), bg="#00ffbb")
label2.grid(column=1, row=0)

entry2 = Entry(tab1,
               font=("Arial", 18),
               fg="black",
               bg="white", width=11)
entry2.grid(column=1, row=1, padx=3, pady=3)

startbt = Button(tab1,
                 text="Start",
                 command=start,
                 font=("Cosmic San", 16),
                 fg="black",
                 bg="#85e9ff",
                 activeforeground="black",
                 activebackground="#85e9ff",
                 state=ACTIVE,
                 compound="bottom")
startbt.grid(row=2, column=0)

delBt = Button(tab1, text="Clear",
               compound="bottom",
               font=("Cosmic San", 16),
               fg="black",
               bg="#85e9ff",
               activeforeground="black",
               activebackground="#85e9ff",
               command=delete)
delBt.grid(row=2, column=1)

label4 = Label(tab2, text="Hour", font=("Nunito", 16), bg="#00ffbb")
label4.grid(column=0, row=0)

entry3 = Entry(tab2,
               font=("Arial", 18),
               fg="black",
               bg="white", width=5)
entry3.grid(column=0, row=1, padx=2, pady=2)

label5 = Label(tab2, text="Mins", font=("Nunito", 16), bg="#00ffbb")
label5.grid(column=1, row=0)

entry4 = Entry(tab2,
               font=("Arial", 18),
               fg="black",
               bg="white", width=5)
entry4.grid(column=1, row=1, padx=2, pady=2)

label6 = Label(tab2, text="AM / PM", font=("Nunito", 16), bg="#00ffbb")
label6.grid(column=3, row=0)

entry5 = Entry(tab2,
               font=("Arial", 18),
               fg="black",
               bg="white", width=5)
entry5.grid(column=3, row=1, padx=2, pady=2)

setAlarm = Button(tab2, text="Set Alarm",
                  compound="bottom",
                  font=("Cosmic San", 16),
                  fg="black",
                  bg="#85e9ff",
                  activeforeground="black",
                  activebackground="#85e9ff",
                  command=setAlarm)
setAlarm.grid(column=0, row=2, padx=1, pady=1)

delBt2 = Button(tab2, text="Clear",
                compound="bottom",
                font=("Cosmic San", 16),
                fg="black",
                bg="#85e9ff", width=8,
                activeforeground="black",
                activebackground="#85e9ff",
                command=delete)
delBt2.grid(column=3, row=2, padx=1, pady=1)

window.mainloop()
