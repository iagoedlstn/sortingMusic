import os
from pydub import AudioSegment

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
    #   chunk = chunk.fade_in(duration=10)
    #   chunk = chunk.fade_out(duration=10)

      # Filename / Path to store the sliced audio 
      filename= "audioFolders/chunks/" + str(counter)+'.wav'
      #chunks/1.wav
      # Store the sliced audio file to the defined path 
      chunk.export(filename, format ="wav") 
      # Print information about the current chunk 
      if counter % 10 == 0:
        print("Processing chunk "+str(counter)+". Start = " + str(start)+ " end = "+str(end)) 
    
      # Increment counter for the next chunk 
      counter = counter + 1


def appendSegment(sound1, sound2, crossfade=5):
    return sound1.append(sound2, crossfade)

def compilar (chunks):
    path="audioFolders/chunks/"
    filelist = os.listdir(path)
    filelist = sorted(filelist, key=lambda x: int(os.path.splitext(x)[0]))

    for archivo in filelist: 
        chunks.append(archivo)
    return chunks
    #random.shuffle(chunks)

def testMakeChunks(audio):
    chunks = make_chunks(audio, 150)
    l = len(chunks)

    for i, ch in enumerate(chunks):
        if i == 0 or i == (l - 1):
            continue
        ch.export('./test' + str(i) + '.wav', format='wav')

def openCancion(filename):
    cancion = AudioSegment.from_wav(f"audioFolders/Samples/{filename}")
    return cancion
