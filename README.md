# 🎵 SpotTube-Downloader

**Spottube** is a Python-based automation tool that allows users to download their Spotify playlist songs locally in MP3 format — without requiring Spotify Premium.

It works by:

1. Fetching songs from a Spotify playlist using the Spotify Web API
2. Searching for each song on YouTube using the YouTube Data API v3
3. Downloading the best available audio using `yt-dlp`
4. Converting it to high-quality MP3 using **FFmpeg**
5. Using **multiprocessing** to significantly reduce total download time

---

## 🚀 Features

* 🔐 Spotify API Authentication (Client Credentials Flow)
* 📂 Fetch songs directly from a Spotify playlist
* 🔎 Automatic YouTube search for each track
* 🎧 High-quality MP3 extraction (192kbps)
* ⚡ Parallel downloads using `ProcessPoolExecutor`
* 🛠 FFmpeg audio conversion integration
* 🔑 Secure API key management using `.env`

---

## 🛠 Tech Stack

* **Python**
* Spotify Web API
* YouTube Data API v3
* `yt-dlp`
* `FFmpeg`
* `concurrent.futures` (Multiprocessing)
* `python-dotenv`
* `requests`

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/spottube.git
cd spottube
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file exists, install manually:

```bash
pip install google-api-python-client python-dotenv requests yt-dlp
```

---

## 🔑 API Setup

Create a `.env` file in the root directory:

```env
CLIENT_ID="Your Spotify Client ID"
CLIENT_SECRET="Your Spotify Client Secret"
YOUTUBE_KEY="Your YouTube API Key"
```

### 🔹 Spotify API

* Go to https://developer.spotify.com
* Create a new project
* Copy **Client ID** and **Client Secret**

### 🔹 YouTube API

* Go to https://console.cloud.google.com
* Enable **YouTube Data API v3**
* Generate an API key

---

## 🎬 FFmpeg Setup

Download FFmpeg from:

https://ffmpeg.org/download.html

Update this path in the code:

```python
'ffmpeg_location': 'C:\\path\\to\\ffmpeg\\bin'
```

Or add FFmpeg to your system PATH.

---

## ▶️ How It Works

1. Authenticate with Spotify API
2. Fetch playlist tracks
3. Search each track on YouTube
4. Extract video ID
5. Download best audio
6. Convert to MP3
7. Save locally
8. Use multiprocessing for faster execution

---

## ⚡ Performance Optimization

Spottube uses:

```python
concurrent.futures.ProcessPoolExecutor()
```

This allows multiple songs to download simultaneously, significantly reducing total runtime compared to sequential downloads.

---

## 📂 Project Structure

```
spottube/
│
├── main.py
├── .env
├── songs/
└── README.md
```

---

## ⚠️ Disclaimer

This project is for educational purposes only.
Please respect copyright laws and YouTube/Spotify Terms of Service when using this tool.

---

## 💡 Future Improvements

* Playlist selection via user input
* GUI version (Tkinter / Streamlit)
* Metadata tagging (artist, album, cover art)
* Error handling improvements
* Async implementation instead of multiprocessing
* Docker support

---

## 👨‍💻 Author

**Wasif Shah**
Backend Developer | AI Enthusiast | Computer Science Student

If you found this project useful, consider giving it a ⭐ on GitHub!
