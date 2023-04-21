import os
import sys
down = f'C:/Users/{os.getlogin()}/Music/'
func_path = os.path.join(os.path.dirname(__file__), 'func')
sys.path.append(func_path)
from BaixarPlaylist import dowPlaylist
from ConverttoMp3 import convertMp3


def Menu():
    while True:
        print("\n \n Escolha uma opção:\n")
        print("1 - BAIXE UMA PLAYLIST DO YOUTUBE ")
        print("2 - Converter MP4 em MP3")
        print("3 - Opção 3")
        print("0 - Sair \n")
        opcao = input("Opção escolhida: ")
        if opcao == "1":
            os.system('cls')
            Playlists = input("Adicione as url separadas por vírgula: \n")
            subpath = input("Deseja salvar em que pasta? \n")
            if Playlists != '':
                if subpath == '':
                    dowPlaylist(Playlists, down)
                    convertMp3(down+'/')
                else:
                    dowPlaylist(Playlists, down+subpath)
                    convertMp3(down+subpath+'/')
            else:
                os.system('cls')
                print('Digite um opção válida')
                Menu()
        elif opcao == "2":
            subpath = input("Converter arquivos de que pasta ? ")
            print("Vamos converter todos os arquivos")
            convertMp3(down+subpath+'/')
        elif opcao == "3":
            print("Você escolheu a opção 3.")
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

Menu()


