from pytube import Playlist , YouTube
import os

def dowPlaylist(playlist_url, directory):
    urls = playlist_url.split(',')
    for url in urls:
        playlist = Playlist(url)
        print(f'Baixando playlist "{playlist.title}"...')
        for video in playlist.video_urls:
            try:
                print(video)
                video = str(video)
                yt = YouTube(video)
                video = yt.streams.filter(file_extension='mp4').first()
                video.download(output_path=directory)
                print(f'Baixado "{video.title}" de "{playlist.title}"')
            #except streamingData:
             
            except Exception as e:
                print(f'Error downloading "{video.title}" from playlist "{playlist.title}": {e}')
                pass

def downMp3(links, directory):
    urls = links.split(',')
    for url in urls:
        try:
            video = str(url)
            yt = YouTube(video)
            video = yt.streams.filter(file_extension='mp4').first()
            video.download(output_path=directory)
            print(f'Baixado {video.title}')
        except Exception as e:
            print(f'Error downloading "{video.title}" from playlist "{playlist.title}": {e}')
            pass