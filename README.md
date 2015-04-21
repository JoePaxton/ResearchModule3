##Animated Analysis of Treehome by Tyler, the Creator

**Purpose**
[fft.py] plots the Fast Fourier Transform data for a mono ```wav``` file into hundreds
or thousands of ```png``` images into your current working directory. After all of the
images are uploaded, ```ffmpeg``` will be used to mix the audio with the images. 

The following command-line prompt will do the trick:
```
ffmpeg -start_number 00000 -i frame_%05d.png -i Treehome95.wav Treehome95.mpg
```
where **Treehome** is the song name in the same directory as the ```png``` images.

The movie file that is created from the snippet above is not truly the result of a 
real-time application; however, it can play the audio along with the associated png 
images, thus demonstrating the audio attributes displayed as the song is played back. 

**You need a full version of ffmpeg (or a version of ffmpeg capable of handling audio 
visual files in order to create the movie file).**



**Background**




**Code Explanation**


 ```python
def avgfftbands(fftarray):
    numBands = 12
    for band in range(0, numBands):
        avg = 0.0
        if band == 0:
            lowFreq = int(0)
        else:
            lowFreq = int(int(sampleRate / 2) / float(2 ** (numBands - band)))		  
        hiFreq = int((sampleRate / 2) / float(2 ** ((numBands-1) - band)))
        lowBound = int(freqToIndex(lowFreq))
        upperBound = int(freqToIndex(hiFreq))
        for j in range(lowBound, upperBound):
                avg += fftarray[j]			
        avg /= (upperBound - lowBound + 1)
        fftavg.append(avg)
 ```


**Resources**

1. [numpyfft]
2. [fftavgs]
3. [fftrelationship]
4. [fft.py]
5. [build2.py]


[numpyfft]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html
[fftavgs]: http://code.compartmental.net/2007/03/21/fft-averages/comment-page-1/
[fftrelationship]: http://www.vibrationworld.com/AppNotes%5CSampling.htm
[fft.py]: https://github.com/JoePaxton/ResearchModule3/blob/master/fft.py
[build2.py]: https://github.com/JoePaxton/ResearchModule3/blob/master/build2.py
