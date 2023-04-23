import os
from unidecode import unidecode

down = f'C:/Users/{os.getlogin()}/Music/'


def renameMp3(path):
    if os.path.exists(down) and os.path.isdir(down):
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.endswith('.mp3') or filename.endswith('.MP3'):
                    old_path = os.path.join(root, filename)
                    new_name = unidecode(filename).upper()
                    new_path = os.path.join(root, new_name)
                    os.rename(old_path, new_path)
    else:
        os.system('cls')
        print('===> ESSA PASTA NÃO EXISTE <===')
        print('===> DIGITE UM DIRETORIO EXISTENTE <===')
        return '21'
