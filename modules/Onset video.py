### Toma la lista de transientes de onset detection y corta un video en base al timestamp.
### El timestamp está en base a samples, así que hay que dividir el onset/samplerate


from moviepy.video.io.VideoFileClip import VideoFileClip
from onset_detection import onsets
import os 
import moviepy.editor as mp # Para convertir a audio

# Seteos
myclip = VideoFileClip("samples/crimson.mp4")
input_video_path = 'samples/crimson.mp4'
samplerate = 44100
onsets_segundos = [x / samplerate for x in onsets]
contador = 0

def cortar(): #  Corta un video en base a la lista de onsets que se le pase
    for i in onsets_segundos :
        name = str(i)
        output_video_path = 'video/'+name+".mp4"
        with VideoFileClip(input_video_path) as video:
            new = video.subclip(contador, i)
            contador = i
            new.write_videofile(output_video_path) #audio_codec='aac'


# for file in os.listdir("video/"):
#     print (file)
#     # clip = mp.VideoFileClip(str(file)).subclip(0,20)
#     # clip.audio.write_audiofile(file + ".mp3")


# cortar()

