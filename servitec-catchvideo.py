from pytube import YouTube

def download_youtube_video(url, save_path, resolution, file_type):
    yt = YouTube(url)
    stream = yt.streams.filter(resolution=resolution, file_extension=file_type).first()
    stream.download(save_path)

url = input("Enter the YouTube video URL: ")
save_path = input("Enter the save path: ")
resolution = input("Enter the resolution (e.g. 1080p, 720p, 480p): ")
file_type = input("Enter the file type (e.g. mp4, webm): ")

download_youtube_video(url, save_path, resolution, file_type)
