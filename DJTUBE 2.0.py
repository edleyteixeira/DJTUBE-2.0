import os
import sys
import time
from pytube.exceptions import PytubeError

#ADICIONA PASTAS AO PROJETO
down = f'C:/Users/{os.getlogin()}/Music/'
func_path = os.path.join(os.path.dirname(__file__), 'func')
sys.path.append(func_path)

#IMPORT DAS FUNCOES
from BaixarPlaylist import dowPlaylist , downMp3
from ConverttoMp3 import convertMp3
from Rename import renameMp3
from TagsMp3 import editTag

#SUBMENU
def SubMenu(opcao):
    #BAIXAR DO YOUTUBE
    if opcao == "11":
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
    elif opcao == "12":
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
            
    #OPERAÇAO COM ARQUIVOS
    if opcao == "21":
        subpath = input("Converter arquivos de que pasta? ")
        
        convertMp3(down+subpath+'/')
    elif opcao == "22":
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
      
              
        
#MENU PRINCIPAL
        
def Menu():
    while True:
        print("\n \n Escolha uma opção:\n")
        print("1 - BAIXE DO YOTUBE")
        print("2 - OPERAÇÕES DE ARQUIVO")
        print("3 - EDITAR TAGS MP3")
        print("0 - SAIR \n")
        opcao = input("Opção escolhida: ")
        
        if opcao == "1":
            os.system('cls')
            print("\n \n O QUE DESEJA FAZER? \n")
            print("1 - BAIXE MUSICAS")
            print("2 - BAIXE PLAYLISTS")
            op = input("\n \n Opção escolhida: ")
            SubMenu(opcao+op)
            
        elif opcao == "2":
            os.system('cls')
            print("\n \n O QUE DESEJA FAZER? \n")
            print("1 - CONVERTER MP4 PARA MP3")
            print("2 - ORGANIZAR NOME DOS ARQUIVOS")
            op = input("\n \n Opção escolhida: ")
            SubMenu(opcao+op)
                        
        elif opcao == "3":
            os.system('cls')
            print("\n \n EDITAR TAGS EM QUE PASTA? \n")
            subpath = input("\n \n Opção escolhida: ")
            print("\n \n QUAL CAPA VOCÊ QUER USAR? \n")
            print("1 - DJREIZINHO.PNG")
            print("2 - PLAYBACKS.PNG")
            capa = input("\n \n Opção escolhida: ")
            if capa == '1':
                img = 'djreizinho'
            elif capa == '2':
                img = 'playbacks'
            else:
                Menu()
            if subpath == '':
                editTag(down, img)
            else:
                editTag(down+subpath+'/', img)
            
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

Menu()


