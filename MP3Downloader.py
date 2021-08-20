from tkinter import *
from youtube_dl import YoutubeDL
import time
import os
import sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

youtube_dl_opts = {}

audio_downloader = YoutubeDL({'format':'bestaudio'})

root = Tk(className=' YouTube MP3 Downloader ')

root.geometry("900x630")

singleMP3 = Label(root, text="Single MP3")
singleMP3.pack()

singleEntry = Entry(root, width=100)
singleEntry.pack(pady=10)

orText = Label(root, text="Or")
orText.pack()

multliMP3 = Label(root, text="Multiple MP3s (.txt)")
multliMP3.pack()

multiEntry = Entry(root, width=100)
multiEntry.pack(pady=10)

def CheckField():
    if len(singleEntry.get()) != 0:
        multiEntry.config(state='disabled')
    elif len(multiEntry.get()) != 0:
        singleEntry.config(state='disabled')
    else:
        singleEntry.config(state='normal')
        multiEntry.config(state='normal')

    root.after(10, lambda: CheckField())

def GetMP3():
    console.config(state="normal")
    if len(singleEntry.get()) != 0:
        
        try:

            console.insert(INSERT, singleEntry.get() + "\n")

            with YoutubeDL(youtube_dl_opts) as ydl:
                info_dict = ydl.extract_info(singleEntry.get(), download=False)
                video_title = info_dict.get('title', None)

            console.insert(INSERT, video_title + "\n")
            console.insert(INSERT, "Your MP3 has been downloaded!\n")
            audio_downloader.extract_info(singleEntry.get())

        except Exception:

            console.insert(INSERT, "Couldn\'t download the audio\n")

    elif len(multiEntry.get()) != 0:

        alist = []
        file = open(multiEntry.get(), 'r')
        lines = file.read().splitlines()

        for i in lines:
            alist.append(i)

        for i in range(len(alist)):
            try:

                console.insert(INSERT, alist[i] + "\n")

                with YoutubeDL(youtube_dl_opts) as ydl:
                    info_dict = ydl.extract_info(alist[i], download=False)
                    video_title = info_dict.get('title', None)

                console.insert(INSERT, video_title + "\n")
                console.insert(INSERT, "Your MP3 has been downloaded!\n\n")
                audio_downloader.extract_info(alist[i])

            except Exception:

                console.insert(INSERT, "Couldn\'t download the audio\n")

    else:
        pass
    
    console.config(state="disabled")

console = Text(root, width=90)
console.config(state="disabled")
console.pack(pady=10)

getMP3Btn = Button(root, text="Get MP3(s)", width=25, command=GetMP3)
getMP3Btn.pack(pady=10)

root.after(10, lambda: CheckField())
root.mainloop() 