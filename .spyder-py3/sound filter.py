# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:13:35 2021

@author: Kedar
"""

from numpy import \
    linspace,array, \
    zeros,log,exp,sin,cos,sqrt,pi,e, ones, \
    arange, shape, zeros, real, imag, sign
from matplotlib.pyplot import \
    plot,xlabel,ylabel,legend,show, \
    figure, subplot, title, tight_layout
from scipy.fftpack import fft
import scipy.io.wavfile as wav 
import sounddevice as sd

# time dimension

file_name='NorthernCardinal_noise.wav'
Fs, f =wav.read(file_name)
f = f/max(f)

dT =  1/Fs # sec   time betfreqeen samples
nt  = len(f) #   number of samples in record
T =  nt*dT # Time period of record

t=arange(0,T,dT)  #  time array in seconds using arange(start,stop,step)
            #   note that arange actually stops *before* stop which
            #   is what we want (in a periodic function t=0 ant t=T are the same)

# frequency dimension

freqf =  1/T # Hz   fundamental frequency (lowest frequency)
nfmax = int(nt/2) # number of frequencies resolved by FFT

freqmax = freqf*nfmax # Max frequency (Nyquist)

freq = arange(0,freqmax,freqf) # frequency array using arange(start,stop,step)
 # Note that since we are including freq=0 (constant term), this actually truncates before one
 # term before the term at the Nyquist (max) frequency. 

print('Fundamental period and Nyquist Freq',T, freqmax)


# take FFT
F = fft(f)

# get the coeffs
a = 2*real(F[:nfmax])/nt # form the a coefficients
a[0] = a[0]/2

b = -2*imag(F[:nfmax])/nt # form the b coefficients

p = sqrt(a**2 + b**2) # form power spectrum


# Reconstruct the time series by suming fourier series and excluding low-power terms
# use your code from square wave problem here
# One option for filtering: exclude terms where power is less than 40% of the peak power
#   using an if statement in the for loop

#*********** Fill in here 
p_threshold_max = max(p/2)
p_threshold_min = 0.005
print(p_threshold_max, p_threshold_min)
Nrecon = nfmax
fclean = ones(nt)*a[0] # fill time series with constant term
# 4 Use a for loop to do the Fourier Sum above, for n=1...Nrecon
for n in range(1,Nrecon):
    if  p[n] < 0.015 and p[n]> 0.005 and n>7000:
        fclean += a[n]*cos(n/T*2*pi*t)+b[n]*sin(n/T*2*pi*t)
     
## make some plots



# write out the clean time series  
wav.write('Clean.wav', Fs, fclean)

# make some plots
figure(1)

subplot(2,1,1)
plot(t,f, label='Original')
plot(t,fclean, label='Clean')
title('Signal')
legend()

subplot(2,1,2)

plot(freq, p,'-', label='Power')
legend() 

title('FFT Fourier Coefficients')

tight_layout() # prevent squished plot (matplotlib kludge)

from scipy.fft import fft, fftshift

