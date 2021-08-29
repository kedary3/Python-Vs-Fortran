# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:25:29 2021

@author: Kedar
"""

from numpy import arange,linspace,array,zeros,log,exp,sin,cos,sqrt,pi,e,real,imag
from matplotlib.pyplot import plot,xlabel,ylabel,legend,show, figure, subplot,title,xlim,tight_layout
from scipy.fftpack import fft

# time dimension

Fs = 500 # Hz  sampling frequency: samples per second
nt  = 2000 #     number of samples in record
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

# select four frequencies 
f1=10*freqf
f2=40*freqf
f3=80*freqf
f4=24*freqf

print('Frequencies selected:', f1, f2, f3, f4)

A = 2
B = 3
C = -5
D = 7
E = -9


f=A*sin(f1*2*pi*t)+B*sin(f2*2*pi*t)+C*cos(f3*2*pi*t)+D*cos(f4*2*pi*t)+E

# take FFT of this function
F = fft(f)

# get the coeffs
a = 2*real(F[:nfmax])/nt # form the a coefficients
a[0] = a[0]/2

b = -2*imag(F[:nfmax])/nt # form the b coefficients

p = sqrt(a**2 + b**2) # form power spectrum

## make some plots

figure(1)

subplot(2,1,1)
plot(t,f)
title('Signal')

subplot(2,1,2)
plot(freq, a, 'o', label='Cosine')
plot(freq, b, '*', label='Sine')
plot(freq, p, '-', label='Power')
legend()

title('FFT Fourier Coefficients')
xmax = max([f1, f2, f3, f4])*1.15 # find max value and pad a bit (15%)
xlim(0, xmax)

tight_layout() # prevent squished plot (matplotlib kludge)