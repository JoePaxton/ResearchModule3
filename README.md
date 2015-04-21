##Animated Analysis of Treehome95 by Tyler, the Creator

**Purpose**

[fft.py] plots the Fast Fourier Transform data for a mono ```wav``` file into hundreds
```png``` images into your current working directory. After all of the images are created,
```ffmpeg``` is used to mix the audio with the images. 

The following command-line prompt will do the trick:
```
ffmpeg -start_number 00000 -i frame_%05d.png -i Treehome95.wav Treehome95.mpg
```
where **Treehome95** is the song name in the same directory as the ```png``` images.

The movie file that is created from the snippet above is not truly the result of a 
real-time application; however, it can play the audio along with the associated png 
images, thus demonstrating some audio attributes displayed as the song is played back. 

If you wish, you can change the song. Keep in mind that the ```wav``` file needs to be
in the same directory as this program or you can just fully qualify the path.


[build2.py] analyzes the timbre and pitches over segments in a movie file. The movie file is again hundreds 
of still frame ```png``` images by segments in the song. The program will create one image per second.

Since, I do not incorporate the frame rate, the command line will do the trick:
```
ffmpeg -framerate 4.27/1 -start_number 00001 -i Scatter_%05d.png -i Treehome95.wav Treehome95Movie.avi
```
The ```-framerate``` takes a parameter that is determined by the duration of the song and the number
of images you need to extend over the playback. Once you know the number of images you divide it by
the duration and invert it to get the parameter. The parameter of the ```-framerate``` is ```(numImages / duration) / 1 ```. Also the ```start number```is the first ```png``` image in that directory. 

You should only use [build2.py] for shorter songs (or songs with fewer segments) because there is a limit to the number of images you can create in a single run. Once you exceed that number, the program will abort with a Python memory error.

If you wish to learn more on creating video slideshows from images, then go to [framerate]. 

*You need the full version of ffmpeg (or a version of ffmpeg capable of creating video 
files in order to create the movie file). Also, create an empty directory for
the images to be uploaded so you do not run low on disk space.*

**Background**

When the [FFT] has a bunch of bins (equally divided strips in a window that describes the spectrum sample and frequency of the window), every signal is in the center of all the bins. The [FFT] simply takes a chunk of time (samples) and considers that chunk to be a single period of a repeating waveform. Most sounds are constant. Over any short period of time, the sound usually look like a regularly repeating function.

Every point of the [FFT] describes the spectral density of the frequency band that is centered on a frequency that is a fraction of the sampling rate. The spectral density is the amplitude present for each bandwidth. 

[fftavgs] quotes, "Given a sample of 1024 samples with a sampling rate of 441100 Hz, a 1024 point [FFT] will give
us a frequency spectrum of 513 points with a total bandwidth of 22050 Hz. Each point ```i``` in the
[FFT] represents a frequency band centered on the frequency ```i/1024 * 44100``` whose bandwidth is 
```2/1024 * 22050 = 43.0664062 Hz```, with the exception of ```spectrum[0]``` and ```spectrum[512]```,
whose bandwidth is ```1/1024 * 22050 = 21.5332031 Hz```." If you use this information in a linear algorithm,
you lose some of the audio information in the lower frequency domains; therefore, we need to implement
this in a logarithmic fashion.

**Code Explanation**

We need to group the spectrums in a logarithmic average to span an octave. By grouping the frequencies
into 12 bandwidths, the detection of an attack during the song is easily read. Knowing what frequency 
each point in the [FFT] corresponds to and the bandwidth at the point in ```band``` allows
us to compute the logarithmically spaced averages. This maps the frequencies to the [FFT] spectrum.

This computes only 12 averages, which determines the number of octaves based on the sample rate and the 
smallest bandwidth needed for a single octave. The code from [fftavgs] below explains how to get the averages:

```python
for (int i = 0; i < 12; i++)
{
  float avg = 0;
  int lowFreq;
  if ( i == 0 ) 
    lowFreq = 0;
  else
    lowFreq = (int)((sampleRate/2) / (float)Math.pow(2, 12 - i));
  int hiFreq = (int)((sampleRate/2) / (float)Math.pow(2, 11 - i));
  int lowBound = freqToIndex(lowFreq);
  int hiBound = freqToIndex(hiFreq);
  for (int j = lowBound; j <= hiBound; j++)
  {
    avg += spectrum[j];
  }
  avg = avg / (hiBound - lowBound + 1);
  averages[i] = avg;
}
```

My implementation:
 ```python
def avgfftbands(fftarray):
    fftavg = []
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

1. [fftavgs]
2. [FFT]
3. [framerate]
4. [numpyfft]

[numpyfft]: http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html
[fftavgs]: http://code.compartmental.net/2007/03/21/fft-averages/comment-page-1/
[FFT]: https://www.youtube.com/watch?v=tqcZrPMi4nk
[framerate]: https://trac.ffmpeg.org/wiki/Create%20a%20video%20slideshow%20from%20images
[fft.py]: https://github.com/JoePaxton/ResearchModule3/blob/master/fft.py
[build2.py]: https://github.com/JoePaxton/ResearchModule3/blob/master/build2.py
