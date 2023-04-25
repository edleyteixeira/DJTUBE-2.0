from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC
import os

def editTag(down, capa):
    
    if os.path.exists(down) and os.path.isdir(down):
        for root, dirs, files in os.walk(down):
            for filename in files:
                if filename.endswith('.mp3') or filename.endswith('.MP3'):
                    if '-' not in filename:
                        pass
                    else:
                        try:
                            print(filename)
                            audio = MP3(down+filename)
                        except HeaderNotFoundError:
                            print(f'O ARQUIVO {filename} ESTÁ CORROMPIDO')
                            pass
                            
                        info = filename.split('-')
                        # Adicionar/Editar tags
                        audio['TIT2'] = TIT2(encoding=3, text=info[1]) #TITULO
                        audio['TPE1'] = TPE1(encoding=3, text=info[0]) #ARTISTA
                        audio['TALB'] = TALB(encoding=3, text="SIGA NO INSTAGRAM @ODJREIZINHO")
                        # Adicionar imagem de capa
                        with open(f'img/{capa}.png', 'rb') as f:
                            audio.tags.add(APIC(
                                encoding=3,  # Tipo de codificação da imagem
                                mime='image/png',  # Tipo de arquivo da imagem
                                type=3,  # Tipo da imagem (3 significa capa frontal)
                                desc=u'Cover',  # Descrição da imagem
                                data=f.read()  # Conteúdo da imagem
                            ))

                        # Salvar alterações
                        audio.save()
    else:
        os.system('cls')
        print('===> ESSA PASTA NÃO EXISTE <===')
        print('===> DIGITE UM DIRETORIO EXISTENTE <===')
        
