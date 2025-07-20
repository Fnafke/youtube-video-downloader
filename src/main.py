from tkinter import *
import ctypes

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

# download function


def download():
    url = url_var.get()


root.title("Fnafke's Youtube Video Downloader")
url_label = Label(
    root, text="Provide the url of the Youtube Video you would like to download!", font=('calibre', 10, 'bold'))
url_entry = Entry(root, textvariable=url_var, font=('calibre', 10, 'normal'))


# positioning of all elements
url_label.grid(row=0, column=0)
url_entry.grid(row=0, column=1)

root.mainloop()
