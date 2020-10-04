import os
from pathvalidate import sanitize_filename
import sys
# 1 Criar pastas: imagens, audios, documentos, videos, outros
# 2 Pegar o nome dos arquivos
# 3 Pegar a extensão do arquivo para determinar o tipo
# 4 Mover arquivos para as pastas correspondentes

class Actions:
    
    extAudio = ['.mp3', '.wav']
    extVideo = ['.mp4', '.mov', '.avi']
    extImages = ['.jpg', '.jpeg', '.png']
    extDocuments = ['.txt', '.log', '.pdf']
    folders = ['Vídeos','Áudios','Imagens','Documentos','Outros']


    def __init__(self,path=''):
        self.path = path
        

    def __catchExtension(self,file):
        index = file.rfind('.')
        return file[index:]


    def __createFoldersFromList(self, folders):
        
        for folder in folders:
            folderName = os.path.join(self.path, folder)
            if not os.path.isdir(folderName):
                os.makedirs(folderName,True)


    def __organize(self, baseFolder=None):
        baseFolder = self.path
        files = os.listdir(baseFolder)
        newFolder = ''

        for file in files:

            if os.path.isfile(os.path.join(baseFolder, file)):
                ext = str.lower(self.__catchExtension(file))
                print(file,ext)
                if ext in Actions.extAudio:
                    newFolder = os.path.join(baseFolder,'Áudios')
                elif ext in Actions.extDocuments:
                    newFolder = os.path.join(baseFolder,'Documentos')
                elif ext in Actions.extImages:
                    newFolder = os.path.join(baseFolder,'Imagens')
                elif ext in Actions.extVideo:
                    newFolder = os.path.join(baseFolder,'Vídeos')
                elif ext == "desktop.ini":
                    pass
                else:
                    newFolder = os.path.join(baseFolder,'Outros')
                os.rename(os.path.join(baseFolder,file),os.path.join(newFolder,file))
                print("De:",os.path.join(baseFolder,file),"Para:",os.path.join(newFolder,file))


    def doActions(self):
        self.__createFoldersFromList(Actions.folders)
        self.__organize()


path = '.' if sys.argv else sys.argv[1]
actions = Actions(path)
actions.doActions()