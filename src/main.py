from tkinter import *
import ctypes
from tkinter import filedialog
from tkinter import ttk
from pytubefix import YouTube
from moviepy import AudioFileClip
import threading
import os

root = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def center_window(width=0, height=0):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


center_window(800, 650)

# UI variables
url_var = StringVar()
download_path_var = StringVar()
resolution_var = StringVar()
resolution_var.set("Select a resolution:")
resolution_list = ["144p", "240p", "360p", "480p", "720p", "1080p"]

file_extension_var = StringVar()
file_extension_var.set("mp4")
file_extension_list = ["mp4", "mp3"]

status_message_var = StringVar()


def clear_status_message():
    status_message_var.set("")


def select_download_path():
    path = filedialog.askdirectory()
    if path:
        download_path_var.set(path)


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = int((bytes_downloaded / total_size) * 100)
    progressbar['value'] = percent
    root.update_idletasks()


def threaded_download():
    clear_status_message()
    url = url_var.get()
    download_path = download_path_var.get()
    resolution = resolution_var.get()
    file_ext = file_extension_var.get()

    progressbar['value'] = 0

    if len(url.strip()) < 1:
        status_message_var.set("URL is required!")
        return

    if len(download_path.strip()) < 1:
        status_message_var.set("Download path is required!")
        return

    if resolution not in resolution_list and file_ext == "mp4":
        status_message_var.set("Select a valid resolution!")
        return

    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        if file_ext == "mp4":
            stream = yt.streams.filter(
                progressive=True, file_extension='mp4', res=resolution).first()
        elif file_ext == "mp3":
            stream = yt.streams.filter(only_audio=True).first()

        if not stream:
            status_message_var.set("Selected option is not available!")
            return

        status_message_var.set("Downloading...")
        downloaded_file = stream.download(output_path=download_path)

        if file_ext == "mp3":
            mp3_path = os.path.splitext(downloaded_file)[0] + ".mp3"
            audio_clip = AudioFileClip(downloaded_file)
            audio_clip.write_audiofile(mp3_path)
            audio_clip.close()
            os.remove(downloaded_file)  # remove original .mp4

        status_message_var.set("Download complete!")
        progressbar['value'] = 100

    except Exception as ex:
        status_message_var.set("An error occurred: " + str(ex))


def download():
    threading.Thread(target=threaded_download).start()


# UI Layout
root.title("Fnafke's Youtube Video Downloader")

url_label = Label(root, text="Provide the url of the Youtube Video you would like to download!", font=(
    'calibre', 10, 'bold'))
url_entry = Entry(root, textvariable=url_var, font=(
    'calibre', 10, 'normal'), width=50)

download_path_label = Label(
    root, text="Select your download path!", font=('calibre', 10, 'bold'))
download_path_entry = Entry(root, textvariable=download_path_var, font=(
    'calibre', 10, 'normal'), width=50)
download_path_select_button = Button(
    root, text="Browse", command=select_download_path)

resolution_list_menu = OptionMenu(root, resolution_var, *resolution_list)
file_extension_menu = OptionMenu(
    root, file_extension_var, *file_extension_list)

url_submit_button = Button(root, text="Download", font=(
    'calibre', 10, 'normal'), command=download)
progressbar = ttk.Progressbar(orient=HORIZONTAL, length=200)
status_message = Label(root, textvariable=status_message_var)

# Grid placement
url_label.grid(row=0, column=0)
url_entry.grid(row=1, column=0)
download_path_label.grid(row=2, column=0)
download_path_entry.grid(row=3, column=0)
download_path_select_button.grid(row=4, column=0)
file_extension_menu.grid(row=5, column=0)
resolution_list_menu.grid(row=6, column=0)
url_submit_button.grid(row=7, column=0)
progressbar.grid(row=8, column=0)
status_message.grid(row=9, column=0)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
