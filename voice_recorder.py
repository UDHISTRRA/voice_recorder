import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv
import os
import subprocess

root = Tk()
root.geometry("600x700+400+80")
root.resizable(False, False)
root.configure(background = "#F5E0C3")  # Soft cream background for vintage feel
root.title("Voice Recorder")

# Function to record audio
def Record():
    freq = 44100
    dur = int(duration.get())
    recording = sound.rec(dur * freq, samplerate=freq, channels=2)

    # Timer
    try:
        temp = int(duration.get())
    except:
        print("Enter a valid number for duration.")

    while temp > 0:
        root.update()
        time.sleep(1)
        temp -= 1

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Times Up")
        Label(text=f"{str(temp)}", font="Courier 30", width=4, background="#705D56", fg="#F5E0C3").place(x=240, y=590)

    sound.wait()
    write("recording.wav", freq, recording)

    # Open folder where recording is saved
    def open_folder(folder_path):
        try:
            if os.name == 'nt':  # For Windows
                subprocess.run(['explorer', folder_path])
        except OSError as e:
            messagebox.showerror("Error", f"Failed to open folder: {e}")

    folder_path = os.path.dirname(os.path.abspath("recording.wav"))
    open_folder(folder_path)

# Icon
icon_image = PhotoImage(file="vc.png")
root.iconphoto(False, icon_image)

# Logo with vintage microphone image
photo_image = PhotoImage(file="vc.png")  # Replace with a vintage microphone image
myimage = Label(image=photo_image, background="#705D56", height=250, width=170)
myimage.pack(padx=5, pady=5)

# App name label
Label(text="Vintage Voice Recorder", font="Courier 28 bold", background="#F5E0C3", fg="#705D56").pack()

# Entry box for duration input
duration = StringVar()
entry = Entry(root, textvariable=duration, font="Courier 25", width=15, background="#705D56", fg="white", borderwidth=2, relief="flat")
entry.pack(pady=10)
Label(text="Enter time in seconds", font="Courier 15", background="#F5E0C3", fg="#705D56").pack()

# Record button with vintage color and rounded edges
record = Button(root, text="Record", font="Courier 20", bg="#5F4B43", fg="white", border=0, command=Record, relief="flat", padx=10, pady=5)
record.pack(pady=30)

root.mainloop()
