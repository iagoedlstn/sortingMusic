##############################################################################
from pydub import AudioSegment
from modules.algoritmos import *
import os, random, shutil
import ffmpeg

#crear carpetas
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
##############################################################################

#### importar audio a fragmentar 
# 
def openCancion(filename):
    cancion = AudioSegment.from_wav(f"audioFolders/Samples/{filename}")
    return cancion


def slicesong(overlap, interval, n, audio):
    counter = 1 
    start = 0
    end = 0
    for i in range(0, n, interval):     
    # During first iteration, start is 0, end is the interval 
      if i == -1: 
          start = 0
          end = interval 

    # All other iterations, start is the previous end - overlap end becomes end + interval 
      else: 
          start = end - overlap 
          end = start + interval  

      # When end becomes greater than the file length, end is set to the file length 
      # flag is set to 1 to indicate break. 
      if end >= n: 
          end = n 

      # Storing audio file from the defined start to end 
      chunk = audio[start:end] 

      # Filename / Path to store the sliced audio 
      filename= "audioFolders/chunks/" + str(counter)+'.wav'
      #chunks/1.wav
      # Store the sliced audio file to the defined path 
      chunk.export(filename, format ="wav") 
      # Print information about the current chunk 
      if counter % 10 == 0:
        print("Processing chunk "+str(counter)+". Start = "
                        +str(start)+" end = "+str(end)) 
    
      # Increment counter for the next chunk 
      counter = counter + 1

def compilar ():
    for archivo in os.listdir("audioFolders/chunks/"): 
        chunks.append(archivo)
    #random.shuffle(chunks)

def appendSegment(sound1, sound2, crossfade=0):
    return sound1.append(sound2, crossfade)

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
    interval = 150 #cuanto duran los fragmentos
    overlap = 1 * 10

    slicesong(overlap, interval, n, cancion)
    compilar()
    unsortedCancion = desordenPaulatino(chunks, 5, file, cancion)
    test = appendSegment(cancion, unsortedCancion)
    test.export(f"audioFolders/Hechos/desorden+inicio {file}", format="wav")



#### Guardado en caso de que haya que comparar con la lista ordenada
### agrega todos los fragmentos a chunks y los ordena de menor a mayor
#listaOrdenada = sorted(chunks,key=lambda x: int(os.path.splitext(x)[0]))

