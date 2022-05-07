import os 
largo=0

filelist = os.listdir("audioFolders/chunks/")
filelist = sorted(filelist,key=lambda x: int(os.path.splitext(x)[0]))


for archivo in filelist:
    # temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
    # sorting += temporal
    print (archivo)
    largo += 1