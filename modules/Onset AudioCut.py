from pydub import AudioSegment
from algoritmos import *
import os, random, shutil
from onset_detection import onsets


# onsets_segundos = [x / samplerate for x in onsets]
audiofile_input = AudioSegment.from_mp3("samples/petals/petals.wav")

def cortar(): #  Corta un video en base a la lista de onsets que se le pase
    contador = 0    
    for i in onsets :
        name = str(i)
        audiofile_output = 'samples/petals/'+name+".wav"
        fragmento = audiofile_input[contador:i]
        fragmento.export(audiofile_output, format ="wav")
        print ("Procesando " + audiofile_output)
        contador = i

cortar()

