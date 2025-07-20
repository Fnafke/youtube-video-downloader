from tkinter import *
import ctypes
from tkinter import filedialog

root = Tk()
ctypes.windll.shcore.SetProcessDpiAwareness(1)


def center_window(width=0, height=0):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))


center_window(800, 650)

# declare url variable
url_var = StringVar()
download_path_var = StringVar()
status_message_var = StringVar()

# clear the status message variable


def clear_status_message():
    status_message_var.set("")

# select a path


def select_download_path():
    path = filedialog.askdirectory()
    if path:
        download_path_var.set(path)

# download function


def download():
    clear_status_message()

    url = url_var.get()
    download_path = download_path_var.get()

    if len(download_path.strip()) < 1:
        status_message_var.set("Download path is required!")

    try:
        ...
    except:
        ...


root.title("Fnafke's Youtube Video Downloader")

url_label = Label(
    root, text="Provide the url of the Youtube Video you would like to download!", font=('calibre', 10, 'bold'))
url_entry = Entry(root, textvariable=url_var, font=(
    'calibre', 10, 'normal'), width=50)
download_path_label = Label(
    root, text="Select your download path!", font=('calibre', 10, 'bold'))
download_path_entry = Entry(root, textvariable=download_path_var, font=(
    'calibre', 10, 'normal'), width=50)
download_path_select_button = Button(
    root, text="Browse", command=select_download_path)
url_submit_button = Button(root, text="Download", font=(
    'calibre', 10, 'normal'), command=download)
status_message = Label(root, textvariable=status_message_var)

# positioning of all elements
url_label.grid(row=0, column=0)
url_entry.grid(row=1, column=0)
download_path_label.grid(row=2, column=0)
download_path_entry.grid(row=3, column=0)
download_path_select_button.grid(row=4, column=0)
url_submit_button.grid(row=6, column=0)
status_message.grid(row=7, column=0)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
