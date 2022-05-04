import sys
from aubio import *

win_s = 512                 # fft size
hop_s = win_s // 2       # hop size
filename = "samples/petals/petals.wav" #sys.argv[1]
# if len(sys.argv) < 2:
#     print("Usage: %s <filename> [samplerate]" % sys.argv[0])
#     sys.exit(1)
samplerate = 44100
if len( sys.argv ) > 2: samplerate = int(sys.argv[2])
s = source(filename, samplerate, hop_s)
samplerate = s.samplerate
o = onset("default", win_s, hop_s, samplerate)

onsets = [] # list of onsets, in samples

total_frames = 0
while True:
    samples, read = s()
    if o(samples):
        #print("%f" % o.get_last_s())
        onsets.append(o.get_last())
    total_frames += read
    if read < hop_s: break


#print ("Onsets: ", onsets)
#slice_source_at_stamps("samples/crimson.mp4", onsets)

# aubio.slice_source_at_stamps(source_file, timestamps, timestamps_end=None, 
                             # output_dir=None, samplerate=0, hopsize=256, create_first=False)

    


    
