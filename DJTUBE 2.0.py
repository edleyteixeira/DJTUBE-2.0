import os
import sys
import time
down = f'C:/Users/{os.getlogin()}/Music/'
func_path = os.path.join(os.path.dirname(__file__), 'func')
sys.path.append(func_path)
from BaixarPlaylist import dowPlaylist , downMp3
from ConverttoMp3 import convertMp3
from Rename import renameMp3


def Menu():
    while True:
        print("\n \n Escolha uma opção:\n")
        print("1 - BAIXE DO YOTUBE")
        print("2 - OPERAÇÕES DE ARQUIVO")
        print("3 - ")
        print("0 - SAIR \n")
        opcao = input("Opção escolhida: ")
        if opcao == "1":
            os.system('cls')
            print("\n \n O QUE DESEJA FAZER? \n")
            print("1 - BAIXE MUSICAS")
            print("2 - BAIXE PLAYLISTS")
            opcao = input("\n \n Opção escolhida: ")
            if opcao == "1":
                links = input("Adicione as url separadas por vírgula: \n")
                subpath = input("Deseja salvar em que pasta? \n")
                if links != '':
                    if subpath == '':
                        downMp3(links, down)
                        convertMp3(down)
                        renameMp3(down)
                    else:
                        downMp3(links, down+subpath)
                        convertMp3(down+subpath+'/')
                        renameMp3(down+subpath+'/')
                else:
                    os.system('cls')
                    print('Digite um opção válida')
                    time.sleep(2)
                    Menu()
            elif opcao == "2":
                Playlists = input("Adicione as url separadas por vírgula: \n")
                subpath = input("Deseja salvar em que pasta? \n")
                if Playlists != '':
                    if subpath == '':
                        dowPlaylist(Playlists, down)
                        convertMp3(down)
                        renameMp3(down)
                    else:
                        dowPlaylist(Playlists, down+subpath)
                        convertMp3(down+subpath+'/')
                        renameMp3(down+subpath+'/')
                else:
                    os.system('cls')
                    print('Digite um opção válida')
                    time.sleep(2)
                    Menu()
        elif opcao == "2":
            os.system('cls')
            print("\n \n O QUE DESEJA FAZER? \n")
            print("1 - CONVERTER MP4 PARA MP3")
            print("2 - ORGANIZAR NOME DOS ARQUIVOS")
            opcao = input("\n \n Opção escolhida: ")
            if opcao == "1":
                subpath = input("Converter arquivos de que pasta? ")
                print("Vamos converter todos os arquivos")
                convertMp3(down+subpath+'/')
            elif opcao == "2":
                subpath = input("Renomear arquivos em que pasta? ")
                if subpath == "":
                    renameMp3(down)
                else:
                    renameMp3(down+subpath+"/")
            else:
                os.system('cls')
                print("Opção inválida. Tente novamente.\n")
                time.sleep(2)
                Menu()                
        elif opcao == "3":
            print("Você escolheu a opção 3.")
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

Menu()


