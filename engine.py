##############################################################################
from pydub import AudioSegment
from algoritmos import desordenPaulatino
import os, random, shutil
import ffmpeg
from pydub.utils import make_chunks
from utils import *

createFolders()
##############################################################################

#Corta el audio en pedazos y los guarda en \chunks
listaCanciones=[]
for file in os.listdir('audioFolders/Samples'):
    listaCanciones.append(file)

for file in listaCanciones:
    #lista de fragmentos
    cancion=openCancion(file)

    #variables de slicesong
    n = len(cancion) 
    counter = 1 
    interval = 100 # cuanto duran los fragmentos en ms
    overlap = 1 * 0
    
    print(file)
    createFolders()
    slicesong(overlap, interval, n, cancion)
    chunks = compilar()
    unsortedCancion = desordenPaulatino(chunks, 1, file)
    # test = appendSegment(cancion, unsortedCancion)
    # test.export(f"audioFolders/Hechos/desorden+inicio {file}", format="wav")



#### Guardado en caso de que haya que comparar con la lista ordenada
### agrega todos los fragmentos a chunks y los ordena de menor a mayor
#listaOrdenada = sorted(chunks,key=lambda x: int(os.path.splitext(x)[0]))

