# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:55:41 2021

@author: Kedar
"""

from numpy import \
    linspace,array, \
    zeros,log,exp,sin,cos,sqrt,pi,e, ones, \
    arange, shape, zeros, real, imag,nonzero
from matplotlib.pyplot import \
    plot,xlabel,ylabel,legend,show, \
    figure, subplot, title, tight_layout
from scipy.fftpack import fft
import scipy.io.wavfile as wav 
import sounddevice as sd
import os
from numpy import arange,linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e,real,imag
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot,title,xlim,tight_layout
from scipy.fftpack import fft,rfft,ifft


import time
#read each sound file 
folder = ["90s-Office-Phone.wav","Boom.wav",
          "Chirping-Birds.wav","NorthernCardinal.wav","Yamaha-CS2x-Flute-C5.wav"] 
n = 1
for file in folder:
    

    #to find the index where t=3 Then try
    
    Fs, fin =wav.read(file)
    
    istart=3000
    
    iend=4000
    
    f = fin[istart:iend]
    
    #An interval of 0.25 to 1 sec is reasonable.
    nt = len(f)
    sd.play(f,Fs)
    T =  nt/Fs# Time period of record
    dT =  1/Fs# sec   time between samples
    
    t=arange(0,T,dT)  #  time array in seconds using arange(start,stop,step)
                #   note that arange actually stops *before* stop time which
                #   is what we want (in a periodic function t=0 and t=T are the same)
                
    
    # frequency dimension
    
    freqf = 1/T# Hz   fundamental frequency (lowest frequency)
    nfmax = int(nt/2) # number of frequencies resolved by FFT
    
    freqmax = freqf*nfmax # Max frequency (Nyquist)
    
    freq = arange(0,freqmax,freqf) # frequency array using arange(start,stop,step)
    # Note:
    #     include freq=0 (constant term), so freq[0]=0
    #     end one term before the  Nyquist (max) frequency, so freq[-1]=freqmax-freqf
    
    print(freqmax-freqf)
    print(freq[-1])
    print('Fundamental period and Nyquist Freq',T, freqmax)
    F = fft(f)
    # get the coeffs
    a = 2*real(F[:nfmax])/nt # form the a coefficients
    a[0] = a[0]/2
    
    b = -2*imag(F[:nfmax])/nt # form the b coefficients
    
    p = sqrt(a**2 + b**2) # form power spectrum
    
    ## make some plots
    
    figure()
    
    subplot(2,1,1)
    plot(t,f)
    title('Signal')
    
    subplot(2,1,2)
    plot(freq, a, 'o', label='Cosine')
    plot(freq, b, '*', label='Sine')
    plot(freq, p, '-', label='Power')
    legend()
    
    title('FFT Fourier Coefficients')
    xmax = freqmax*1.15
    xlim(0, xmax)
    
    tight_layout() # prevent squished plot (matplotlib kludge)
    
    n+=1