##############################################################################
from pydub import AudioSegment
from algoritmos import desordenPaulatino
import os, random, shutil
import ffmpeg
from pydub.utils import make_chunks
from utils import *

#crear carpetas
def createFolders():
    if os.path.exists("audioFolders/chunks"):
        shutil.rmtree('audioFolders/chunks')
        os.makedirs('audioFolders/chunks')
    else: 
        os.makedirs('audioFolders/chunks')
        
    if os.path.exists("audioFolders/capturas/"):
        shutil.rmtree("audioFolders/capturas/")
        os.makedirs("audioFolders/capturas/")
    else: 
        os.makedirs("audioFolders/capturas/")

if not os.path.exists("audioFolders/Hechos/"):
    os.makedirs("audioFolders/Samples/")

if not os.path.exists("audioFolders/Samples/"):
    os.makedirs("audioFolders/Samples/")

createFolders()
##############################################################################

#Corta el audio en pedazos y los guarda en \chunks
listaCanciones=[]
for file in os.listdir('audioFolders/Samples'):
    listaCanciones.append(file)

for file in listaCanciones:
    #lista de fragmentos
    cancion=openCancion(file)

    # Inicializa la lista vacia
    chunks=[]  

    #variables de slicesong
    n = len(cancion) 
    counter = 1 
    interval = 100 #cuanto duran los fragmentos
    overlap = 1 * 0
    
    print(file)
    createFolders()
    slicesong(overlap, interval, n, cancion)
    chunks=compilar(chunks)
    unsortedCancion = desordenPaulatino(chunks, 1, file)
    # test = appendSegment(cancion, unsortedCancion)
    # test.export(f"audioFolders/Hechos/desorden+inicio {file}", format="wav")



#### Guardado en caso de que haya que comparar con la lista ordenada
### agrega todos los fragmentos a chunks y los ordena de menor a mayor
#listaOrdenada = sorted(chunks,key=lambda x: int(os.path.splitext(x)[0]))

