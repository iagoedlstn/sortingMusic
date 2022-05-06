from pydub import AudioSegment, effects
import os
import random


def appendSegment(sound1, sound2, crossfade=0):
    return sound1.append(sound2, crossfade)


############################ BUBBLE SORT #####################################
def bubbleSort( arr): 
    todoEntero = AudioSegment.silent(duration=1000)
    contador=0
    captura=0
    contadorCapturas=0

    n = len(arr)
    contador = 0
    # Traverse through all array elements
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            a = int(os.path.splitext(arr[j])[0])
            b = int(os.path.splitext(arr[j+1])[0])
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if a > b :
                
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
            #print (arr)
#        contador += 1
        print (arr)
    #if (contador % 10 == 0):
        
        sorting = AudioSegment.empty()
        largo=0
        for archivo in os.listdir("audioFolders/chunks/"):
        
            temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
            sorting += temporal
            largo += 1
        sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
        
        captura += 1
        contador += 1
        print(contador)
    for archivo in os.listdir("audioFolders/capturas/"):
        cacho = AudioSegment.from_wav("audioFolders/capturas/%s.wav" %contadorCapturas)
        todoEntero += cacho
        contadorCapturas += 1
    todoEntero.export("bubblesort.wav", format="wav")
#        
#        for archivo in os.listdir("audioFolders/chunks/"):
#            temporal = AudioSegment.from_wav("audioFolders/chunks/%s" %chunks[contador])
#            sorting += temporal
#            contador += 1
  
    return arr
#int(os.path.splitext(arr[index])[0])
##################################################################################################################
def bubbleSortAperghis( arr): 
    todoEntero = AudioSegment.empty()
    #contador=0
    #captura=0
    contadorCapturas=0

    n = len(arr)
    #contador = 0
    # Traverse through all array elements
    largo=0
    for i in range(n):
        captura = AudioSegment.empty()#abro archivo de audio llamado
        #contador
        for t in range (0, n-i-1):
            temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[t])
            captura += temporal#appendeas a a sorting
        captura.export(f"audioFolders/capturas/{largo}.wav", format = "wav")
        # Last i elements are already in place
        for j in range(0, n-i-1):
            a = int(os.path.splitext(arr[j])[0])
            b = int(os.path.splitext(arr[j+1])[0])
         
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if a > b :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        largo+=1
        print(largo)
    print("acabose")
    for archivo in os.listdir("audioFolders/capturas/"):
        if contadorCapturas <94:
            cacho = AudioSegment.from_file(f"audioFolders/capturas/{contadorCapturas}.wav" )
            print("importando cacho")
            todoEntero += cacho
            print("añadiendo cacho")
            contadorCapturas += 1
            print(contadorCapturas)
    print("stop")
    todoEntero.export("Aperghis.wav", format="wav")
        #export sorting nombre contador
            #print (arr)
#        contador += 1
   
    #if (contador % 10 == 0):
        
        # sorting = AudioSegment.empty()
        # largo=0
        # for archivo in os.listdir("audioFolders/chunks/"):
        
        #     temporal = AudioSegment.from_wav("audioFolders/chunks/%s" %arr[largo])
        #     sorting += temporal
        #     largo += 1
        #     sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
        
    #     captura += 1
    #     contador += 1
    #     print(contador)
    # for archivo in os.listdir("audioFolders/capturas/"):
    #     cacho = AudioSegment.from_wav("audioFolders/capturas/%s.wav" %contadorCapturas)
    #     todoEntero += cacho
    #     contadorCapturas += 1
    # todoEntero.export("bubblesort.wav", format="wav")
#        
#        for archivo in os.listdir("audioFolders/chunks/"):
#            temporal = AudioSegment.from_wav("audioFolders/chunks/%s" %chunks[contador])
#            sorting += temporal
#            contador += 1
  

##############################################################################
    
def bubbleSortAperghisReverse( arr): 
    todoEntero = AudioSegment.empty()
    #contador=0
    #captura=0
    
    resto=1
    n = len(arr)
    contadorCapturas=n-2
    largo=0
    for i in range(n):
        captura = AudioSegment.empty()#abro archivo de audio llamado
        #contador
        for t in range (0, n-i-1):
            
            temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[t])
            captura += temporal#appendeas a a sorting
        captura.export(f"audioFolders/capturas/{largo}.wav", format = "wav")
        # Last i elements are already in place
        for j in range(0, n-i-1):
            a = int(os.path.splitext(arr[j])[0])
            b = int(os.path.splitext(arr[j+1])[0])
         
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if a > b :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
        largo+=1
        print(largo)
    print("acabose")
    curva=[]
    for archivo in os.listdir("audioFolders/capturas/"):
        while True:
            try:
                if contadorCapturas >=0:
                    cacho = AudioSegment.from_file(f"audioFolders/capturas/{contadorCapturas}.wav" )
                    print("importando cacho")
                    todoEntero += cacho
                    print("añadiendo cacho")
                    contadorCapturas -= int(((1/resto)*40)+5)
                    resto+=0.8
                    print(resto)
                    print(contadorCapturas)
                    curva.append(contadorCapturas)
                else:
                    break
            except:
               
                break
    todoEntero.export("Aperghis.wav", format="wav")
    print (curva)
    print("stop")
#    todoEntero.export("Aperghis.wav", format="wav")
################################################################################################################
def countingSort(arr, exp1, captura): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) #crea una lista vacia con la cant de numeros
  
    # initialize count array as 0 
    count = [0] * (10) # crea las baskets (para poner la cant de veces que aparece ese digito)
    # Store count of occurrences in count[] 
    for i in range(0, n): #pasa por cada index de la lista
        index = int((int(os.path.splitext(arr[i])[0])/exp1)) 
        count[ (index)%10 ] += 1 #se fija el numero de el digito (al principio serian los 1) y
                                #lo appendea a el basket
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] #a cada casilla le suma las casillas anteriores
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = int((int(os.path.splitext(arr[i])[0])/exp1))
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
#        if i%10==0:

        sorting = AudioSegment.empty()
        largo=0
        for archivo in os.listdir("audioFolders/chunks/"):
            if largo>=10:
        
                temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
                sorting += temporal
            largo += 1
        sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
        captura+=1
#            elif exp1==100:
#                sorting = AudioSegment.empty()
#                largo=0
#                for archivo in os.listdir("audioFolders/chunks/"):
#                    if largo>=1000:
#                        temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
#                        sorting += temporal
#                    largo += 1
#                sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
#                captura+=1
            
            
    print(captura)
    return captura

# Method to do Radix Sort 
def radixSort(arr): 
    captura=0
    contadorCapturas=0
    todoEntero = AudioSegment.empty()
    # Find the maximum number to know number of digits
    forMax=[]
    for t in range (len (arr)):
        forMax.append(int(os.path.splitext(arr[t])[0]))
    max1 = max(forMax)#se fija el numero mas grande
    print(max1)
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    
    #usa conting sort hasta que el numero mas grande dividido exp sea menor a cero 
    #(si es de 3 digitos lo va a hacer 3 veces, desde exp=1 a exp=300)
    exp = 1
    print(captura)
    
    
    sorting = AudioSegment.empty()
    largo=0
    for archivo in os.listdir("audioFolders/chunks/"):
        temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
        sorting += temporal
        largo += 1
    sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
    captura+=1
    
    
    while int(max1/exp) > 0:
        captura=countingSort(arr,exp, captura) #los ordena en base al digito
        print("sort")
        exp *= 10
#        sorting = AudioSegment.empty()
#        largo=0
#        for archivo in os.listdir("audioFolders/chunks/"):
#        
#            temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
#            sorting += temporal
#            largo += 1
#        sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
#        print(exp)
#        captura+=1
    for archivo in os.listdir("audioFolders/capturas/"):
        print(contadorCapturas)
        cacho = AudioSegment.from_wav("audioFolders/capturas/%s.wav" %contadorCapturas)
        todoEntero += cacho
        contadorCapturas += 1
    todoEntero.export("bubblesort.wav", format="wav")
##############################################################################################################

def desordenPaulatino(arr, veces, file, cancion):
    n=len(arr)
    todoEntero = AudioSegment.silent(duration=10)
    captura=0
    contadorCapturas=0
    limiteInmobilidad=1
    limiteMuycerca=1
    limiteCerca=1
    sorting=AudioSegment.silent(duration=10)
    largo=0
    
    for archivo in os.listdir("audioFolders/chunks/"):
        temporal = AudioSegment.from_file("audioFolders/chunks/%s" %arr[largo])
        sorting += temporal
        largo += 1
    sorting.export("audioFolders/capturas/%s.wav"%captura, format="wav")
    captura+=1
    for i in range(int(veces)+1):
        print(captura)
        for i in range (len(arr)):
            p=[1]*n #crea mapa de probabilidades vacio
            
            #definde los rangos que van a tener distintas prob.
            a=int((len(arr))*0.15)
            b=int((len(arr))*0.30)
    
            #cea el mapa de probabilidades
            for t in range (-b,b+1):
                try:
                    if i+t>=0:
                        p[i+t]="cerca"
                except IndexError:
                    break
            for t in range (-a,a+1):
                try:
                    if i+t>=0:
                        p[i+t]="muy cerca"
                except IndexError:
                    break
            p[i]="index"
            
            
            #ordena los index en base a que probabilidad tienen
            muycerca=[]
            cerca=[]
            lejos=[]
    
            for index in range(len(p)):
                
                if p[index]==1:
                    lejos.append(index)
                elif p[index]=="cerca":
                    cerca.append(index)
                elif p[index]=="muy cerca":
                    muycerca.append(index)
    
            tirada=random.random() #define en que rango de p se mueve(o no)
            if i % 10 == 0:
                print("index",i,tirada)
            
    
    #        print(muycerca)
    #        print(cerca)
    #        print(lejos)
               
            
            #define a que casilla se cambia dentro de la lista de p iguales y los cambia
            if tirada>limiteInmobilidad and tirada<limiteMuycerca:
                aDondeVa=random.choice(muycerca)
                # print("muy cerca")
                chunkAMover=arr[i]
                if aDondeVa<i:
                    for j in range(i,aDondeVa,-1):
                        arr[j]=arr[j-1]
                    arr[aDondeVa]=chunkAMover
                    
                elif aDondeVa>i:
                    for j in range(i+1, aDondeVa+1):
                        arr[j-1]=arr[j]
                    arr[aDondeVa]=chunkAMover
                    
            
            
            elif tirada>=limiteMuycerca and tirada<limiteCerca:
                aDondeVa=random.choice(cerca)
                # print("cerca")
                chunkAMover=arr[i]
                if aDondeVa<i:
                    for j in range(i,aDondeVa,-1):
                        arr[j]=arr[j-1]
                    arr[aDondeVa]=chunkAMover
                    
                elif aDondeVa>i:
                    for j in range(i+1, aDondeVa+1):
                        arr[j-1]=arr[j]
                    arr[aDondeVa]=chunkAMover
                    
                    
            elif tirada>=limiteCerca and tirada<=1:
                aDondeVa=random.choice(lejos)
                # print("lejos")
                chunkAMover=arr[i]
                if aDondeVa<i:
                    for j in range(i,aDondeVa,-1):
                        arr[j]=arr[j-1]
                    arr[aDondeVa]=chunkAMover
                    #print(arr)
                elif aDondeVa>i:
                    for j in range(i+1, aDondeVa+1):
                        arr[j-1]=arr[j]
                    arr[aDondeVa]=chunkAMover
        limiteInmobilidad-=0.05
        limiteMuycerca-=0.04
        limiteCerca-=0.01
        listaSeguidillas=[]
        seguidilla=0
        for l in range (len(arr)-1):
            if int(os.path.splitext(arr[l])[0])+1== int(os.path.splitext(arr[l+1])[0]):
                seguidilla+=1
            else:
                listaSeguidillas.append(seguidilla)
                seguidilla=0
        print("la secuencia mas larga es de ", max(listaSeguidillas))
                     
        sorting = AudioSegment.silent(duration=10)
        silence = AudioSegment.silent(duration=10)
        largo=0
        for archivo in os.listdir("audioFolders/chunks/"):
            temporal = AudioSegment.from_file(f"audioFolders/chunks/{arr[largo]}")
            # temporal = temporal.fade_in(duration=20000)#.fade_out(duration=2) ### Borrar
            # temporal = temporal.fade_out(duration=2000)
            # temporal=appendSegment(temporal, silence) 

            sorting = appendSegment(sorting, temporal) 
            largo += 1
        sorting.export(f"audioFolders/capturas/{captura}.wav", format="wav")
        captura+=1
        
    for archivo in os.listdir("audioFolders/capturas/"):
        cacho = AudioSegment.from_wav("audioFolders/capturas/%s.wav" %contadorCapturas)
        # cacho = cacho.fade_in(duration=2).fade_out(duration=2) ### Borrar

        todoEntero = appendSegment(todoEntero, cacho) 
        contadorCapturas += 1
    todoEntero.export(f"audioFolders/Hechos/desorden {file} ", format="wav")
    return todoEntero

    
    
    
    

    
            



        
                
                
        
    