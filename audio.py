pianoKeys={
"a0":27.5, 
"a-0":29.1, 
"b0":30.9, 
"c1":32.7, 
"c-1":34.6, 
"d1":36.7, 
"d-1":38.9, 
"e1":41.2, 
"f1":43.7, 
"f-1":46.2, 
"g1":49.0, 
"g-1":51.9, 
"a1":55.0, 
"a-1":58.3, 
"b1":61.7, 
"c2":65.4, 
"c-2":69.3, 
"d2":73.4, 
"d-2":77.8, 
"e2":82.4, 
"f2":87.3, 
"f-2":92.5, 
"g2":98.0, 
"g-2":103.8, 
"a2":110.0, 
"a-2":116.5, 
"b2":123.5, 
"c3":130.8, 
"c-3":138.6, 
"d3":146.8, 
"d-3":155.6, 
"e3":164.8, 
"f3":174.6, 
"f-3":185.0, 
"g3":196.0, 
"g-3":207.7, 
"a3":220.0, 
"a-3":233.1, 
"b3":246.9, 
"c4":261.6, 
"c-4":277.2, 
"d4":293.7, 
"d-4":311.1, 
"e4":329.6, 
"f4":349.2, 
"f-4":370.0, 
"g4":392.0, 
"g-4":415.3, 
"a4":440.0, 
"a-4":466.2, 
"b4":493.9, 
}
 #import tensorflow as tf
import numpy as np
import pandas as pd
import json

from pyAudioAnalysis import audioBasicIO 
from pyAudioAnalysis import audioFeatureExtraction 


from pydub import AudioSegment
from pydub.playback import play

from os.path import expanduser
def dunc():
    home=expanduser("~")
    song = AudioSegment.from_file("./converted.tta")
    song.export("converted_audio.wav", format="wav", bitrate="128k")

    [Fs,x]=audioBasicIO.readAudioFile('converted_audio.wav') 


    if( len( x.shape ) > 1 and  x.shape[1] == 2 ):
        x = np.mean( x, axis = 1, keepdims = True )
    else:
        x = x.reshape( x.shape[0], 1 )  

    l1=[]
    for i in range(x.shape[0]):
        l1.append(x[i][0])

    arr=np.array(l1)
    freqList=[]
    min=13000



    from scipy import signal
    f, t, Zxx = signal.stft(arr, Fs,nperseg=(2*Fs)/3)

    max=0
    prevMax=0
    index=0
    for j in range(t.shape[0]):
        for i in range(f.shape[0]):
            if Zxx[i][j]>max:
                prevMax=max
                max=Zxx[i][j]
                prevInd=index
                index=i
        # if max-prevMax<10:
        #     freqList.append(list(f[index],f[prevInd]))
        # else:
        freqList.append(f[index])




    keysList=[]
    for f in freqList:
        min=13000
        for key in pianoKeys:
            diff=abs(pianoKeys[key]-f)
            if(diff< min):
                min=diff
                keyNo=key
        keysList.append(keyNo)

    import json
    main_list=[]
    for i in keysList:
        l=[]
        l.append(i)
        main_list.append(l)
    # with open('./static/js/list.js', 'w') as f: 
    #         json.dump(main_list, f)
    return main_list