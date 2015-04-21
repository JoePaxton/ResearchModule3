# Look at README.md before use
__author__ = "Joe Paxton"
import echonest.remix.audio as audio
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
    filename = audio.LocalAudioFile("Treehome95.wav")
    duration = filename.duration
    print "\n\nDuration in seconds: " , duration
    segments = audio.AudioAnalysis("Treehome95.wav").segments  
    collect = audio.AudioQuantumList()
    collect_t = audio.AudioQuantumList()
    
    for seg in segments:
        collect.append(seg.pitches)
        collect_t.append(seg.timbre)
    x=0
    y=0    
    count=0
   
    print 'Length: ',len(segments)
    points = np.zeros((len(segments), 3),dtype=float)
    for i in range(len(segments)):        
        points[i] = ( (i, np.mean(collect[i]), np.mean(collect_t[i])) )    
        fig = plt.figure()
        ax = fig.gca(projection = '3d')
        ax.set_xlabel('Segments')
        ax.set_ylabel('Pitches')
        ax.set_zlabel('Timbre')
        ax.set_title('3D Timbre and Pitches')
        ax.scatter(points[:, 0], points[:, 1],  points[:, 2], zdir = 'z', c = '.5')
        count = count + 1
        fn = str('Scatter_%05d' % count) + '.png'
        print '\rIterating through segments...',i,fn,		
        plt.savefig(fn,dpi=75)
    
    return

if __name__ == '__main__':
    main()
