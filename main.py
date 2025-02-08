import argparse
from yt_dlp import YoutubeDL

def download_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  
        'merge_output_format': 'mkv',         
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_audio': True,         
        'audio_format': 'mp3',         
        'outtmpl': '%(title)s.%(ext)s', 
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    parser = argparse.ArgumentParser(description="YouTube Video/Audio Downloader")
    parser.add_argument('--link', required=True, help="YouTube video URL")
    parser.add_argument('--video', action='store_true', help="Download video")
    parser.add_argument('--audio', action='store_true', help="Download audio")
    
    args = parser.parse_args()
    
    if args.video:
        download_video(args.link)
    elif args.audio:
        download_audio(args.link)
    else:
        print("Please specify either --video or --audio.")

if __name__ == "__main__":
    main()