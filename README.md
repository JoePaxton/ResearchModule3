##Animated Analysis of **Treehome by Tyler, the Creator**



**Purpose**




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
1. http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft.html
2. http://code.compartmental.net/2007/03/21/fft-averages/comment-page-1/
3. http://fas.org/man/dod-101/navy/docs/es310/FM.htm
4. http://www.vibrationworld.com/AppNotes%5CSampling.htm
