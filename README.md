# 🎥 Fnafke's YouTube Video Downloader

A simple desktop app to download YouTube videos in your selected resolution using a graphical interface built with Tkinter.

## 🛠 Requirements

- Python 3.7+
- `pytubefix` library (for YouTube download support)

> Note: `tkinter` and `threading` are part of the Python Standard Library and require no additional installation.

## 📦 Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/Fnafke/youtube-video-downloader.git
   cd youtube-video-downloader/src
   ```

2. **Install the required packages:**

   ```bash
   pip install pytubefix
   pip install moviepy
   ```

## 🚀 Usage

### 🐍 Run from Source (Python)

1. Run the Python script:

   ```bash
   python main.py
   ```

2. Paste a YouTube video URL, select your download path and preferred resolution, then click **Download**.

### 💻 Use the Compiled EXE (Windows)

A precompiled executable is available in the `src/dist/` folder:

```
/src/dist/main.exe
```

You can double-click the `.exe` to run the app without installing Python or any libraries.

## ❗ Notes

- Some resolutions (e.g., `144p`) may not be available for all videos.
- Make sure the video is not private, a YouTube Short, or age-restricted.
- When downloading as MP3, audio will be extracted from the highest available audio stream.

## 📜 License

This project is licensed under the MIT License.
