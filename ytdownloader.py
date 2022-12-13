
# half polish-english comments are for me ;D
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
# shutil for moving file
import shutil

# functions
def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()  
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # move file to selected directory
    shutil.move(mp4_video, user_path)

    screen.title("Download complete! Download another file: ")
def select_path():
    # allows user to select path
    path = filedialog.askdirectory()
    path_label.config(text=path)

# tworzenie okna, tytuł okna
screen = Tk()
title = screen.title("Youtube Downloader")

# rozmiar okna
canvas = Canvas(screen, width=500, height=600)
canvas.pack()

# logo yt, nie działała mi ścieżka bezpośrednia do zdjęcia
logo = PhotoImage(file="ytl.png")

# resize, im wieksze argumenty tym mniejszy obrazek
logo = logo.subsample(5,5)

# pozycjonowanie, argumenty:x, y, zmienna ze ścieżką do obrazka
canvas.create_image(250,100,image=logo)

# tworzenie pola do wklejenia linku
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download link:",font=("Arial", 15))

# add widgets to window
canvas.create_window(250,220,window=link_label)
canvas.create_window(250,260,window=link_field)

# ścieżka gdzie ma zostać zapisany plik
path_label = Label(screen,text="Select Path for Download",font=("Arial", 15))
select_btn = Button(screen,text="Select",command=select_path)
canvas.create_window(250,310,window=path_label)
canvas.create_window(250,360,window=select_btn)
# download buttons
download_btn = Button(screen, text="Download File",command=download_file)
canvas.create_window(250,440,window=download_btn)

# uruchamianie okna
screen.mainloop()