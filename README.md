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

If you wish, you can change the song. Keep in mind that the ```wav``` file needs to be
in the same directory as this program or you can just fully qualify the path.


[build2.py] analyzes the timbre and pitches over segments in a movie file. The movie file
is hundreds of still frame ```png``` images at a certain point in the song. The amount of
segments there are is equivalent to the amount of images that are produced. 

Since, I do not incorporate the frame rate, the command line will do the trick:
```
ffmpeg -framerate 1.28/1 -start_number 00001 -i Scatter_%05d.png -i Treehome.wav TreehomeMovie.mp4
```
where the start number is the first ```png``` image in that directory.


*You need a full version of ffmpeg (or a version of ffmpeg capable of handling audio 
visual files in order to create the movie file). Also, create an empty directory for
the images to be uploaded so you do not run low on disk space.*

**Background**



Every point of the FFT describes the spectral density of the frequency band that is centered
on a frequency that is a fraction of the sampling rate. The spectral density is the amplitude
present for each bandwidth. 

[fftavgs] quotes, "Given a sample of 1024 samples with a sampling rate of 441100 Hz, a 1024 point FFT will give
us a freuqency spectrum of 513 points with a total bandwith of 22050 Hz. Each point ```i``` in the
FFT represents a frequency band centered on the frequency ```i/1024 * 44100``` whose bandwidth is 
```2/1024 * 22050 = 43.0664062 Hz```, with the exception of ```spectrum[0]``` and ```spectrum[512]```,
whose bandwidth is ```1/1024 * 22050 = 21.5332031 Hz```."

**Code Explanation**

We need to group the spectrums in a logarithmic average to span an octave. By grouping the f


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
