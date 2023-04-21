import os
from moviepy.editor import *

def convertMp3(down):
    os.system('cls')
    for diretorio, subpastas, arquivos in os.walk(down):
        for arquivo in arquivos:
            extensao = arquivo.split('.')
            if extensao[1].lower() == 'mp4' :
                video_mp4 = f'{down}{extensao[0]}.mp4'
                clip = VideoFileClip(video_mp4) 
                audio = clip.audio
                print('CONVERTENDO MP4 PARA MP3')
                audio.write_audiofile(f'{down}{extensao[0]}.mp3')
                audio.close()
                clip.close()
                print('EXCLUIINDO VIDEO MP4 ' + arquivo)
                os.remove(f'{down}{extensao[0]}.mp4')
                os.system('cls')
            
    