# YouTube Video/Audio Downloader wiht High Quality

## Installation

Before running the script, ensure you have the required dependencies installed.

### Install FFmpeg
FFmpeg is needed for merging and processing media files. Install it using:
```sh
sudo apt install ffmpeg
```

### Install yt-dlp
`yt-dlp` is a powerful YouTube downloader. Install it using pip:
```sh
pip install yt_dlp
```

## Usage

Run the script with the following command:

### Download Video
```sh
python main.py --link "YOUTUBE_VIDEO_URL" --video
```

### Download Audio
```sh
python main.py --link "YOUTUBE_VIDEO_URL" --audio
```

Replace `YOUTUBE_VIDEO_URL` with the actual URL of the YouTube video you want to download.

