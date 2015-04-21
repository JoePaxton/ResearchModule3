# Look at README.md before use
__author__ = "Joe Paxton"
import echonest.remix.audio as audio
from pyechonest.track import track_from_file
import wave
import struct
import numpy as np
from math import sqrt
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
import matplotlib.pyplot as plt

 
if __name__ == '__main__':
    #filename = "yourfavoritesong.wav"
    filename = "Treehome95.wav"
    fileW = audio.LocalAudioFile(filename)
    trackTitle = open(filename)
    trackName = track_from_file(trackTitle, 'wav')
    sampleRate = fileW.sampleRate
    duration = fileW.duration
    processLen = int(duration) - 1
    fileW = wave.open(filename, 'r')
    dataSize = fileW.getnframes()
    read = fileW.readframes(dataSize)
    fileW.close()
                
    unpack = '%dh' % (dataSize)
    read = struct.unpack(unpack, read)
    
    fps = 24
    fwidth = 1.0 / fps
    sampleSize = fwidth * float(sampleRate)
    transforms = int(round(processLen * fps))
    fftavg = []
    
    """Returns the bandwidth"""
    def getBandWidth():
    	return (2.0 / sampleSize) * (sampleRate / 2.0)
 
    """Returns the index of where the frequency occurs"""
    def freqIndx(f):
        if f < getBandWidth()/2:
            return 0
	if f > (sampleRate / 2) - (getBandWidth() / 2):
	    return sampleSize -1
		
	fraction = float(f) / float(sampleRate)
	index = round(sampleSize * fraction)
	return index
    
    """Returns the average frequency for each of the twelve bands"""
    def avgfftbands(fftarray):
        numBands = 12
        del fftavg[:]
        for band in range(0, numBands):
            avg = 0.0
            if band == 0:
                lowFreq = 0
            else:
                lowFreq = int(int(sampleRate / 2) / float(2 ** (numBands - band)))		  
            hiFreq = int((sampleRate / 2) / float(2 ** ((numBands-1) - band)))
            lowBound = int(freqIndx(lowFreq))
            upperBound = int(freqIndx(hiFreq))
            for j in range(lowBound, upperBound):
                avg += fftarray[j]			
            avg /= (upperBound - lowBound + 1)
            fftavg.append(avg)

    """Places all of the samples into your directory"""
    x = range(0, 12)
    for offset in range(0, transforms):
	start = int(offset * sampleSize)
	end = int((offset * sampleSize) + sampleSize -1)
	print "\rProcessing sample %i of %i (%d seconds)" % (offset + 1, transforms, end/float(sampleRate)),
	sampleRange = read[start:end]
	fft = abs(np.fft.fft(sampleRange))
	fft *= ((2**.5)/sampleSize)
	plt.ylim(0, 1000)
	avgfftbands(fft)
	y = fftavg
	width = 0.35
	plt.title(trackName)
	p1 = plt.bar(x, y, width, color='r')
	filename = str('frame_%05d' % offset) + '.png'
	plt.savefig(filename, dpi=100)
	plt.close()
