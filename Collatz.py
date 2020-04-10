# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 18:34:21 2020

@author: snice
"""

from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from math import cos, sin
import numpy as np

RGB=[(255,0,0),(255,99,71),(255,127,80),(205,92,92),(240,128,128),
     (233,150,122),(250,128,114),(255,160,122),(255,69,0),
     (255,140,0),(255,165,0),(255,215,0),(184,134,11),
     (218,165,32),(238,232,170),(189,183,107),(240,230,140),
     (128,128,0),(255,255,0),(154,205,50),(85,107,47),
     (107,142,35),(124,252,0),(127,255,0),(173,255,47),
     (0,100,0),(0,128,0),(34,139,34),(0,255,0),(50,205,50),
     (144,238,144),(152,251,152),(143,188,143),(0,250,154),
     (0,255,127),(46,139,87),(102,205,170),(60,179,113),
     (32,178,170),(47,79,79),(0,128,128),(0,139,139),
     (0,255,255),(0,255,255),(224,255,255),(0,206,209),
     (64,224,208),(72,209,204),(175,238,238),(127,255,212),
     (176,224,230),(95,158,160),(70,130,180),(100,149,237),
     (0,191,255),(30,144,255),(173,216,230),(135,206,235),
     (135,206,250),(25,25,112),(0,0,128),(0,0,139),
     (0,0,205),(0,0,255),(65,105,225),(138,43,226),
     (75,0,130),(72,61,139),(106,90,205),(123,104,238),
     (147,112,219),(139,0,139),(148,0,211),(153,50,204),
     (186,85,211),(128,0,128),(216,191,216),(221,160,221),
     (238,130,238),(255,0,255),(218,112,214),(199,21,133),
     (219,112,147),(255,20,147)] 

def collatz(n):
    suite=[n]
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        #suite.append(n)    
        suite.insert(0,n)
    #print(suite)    
    return suite    
  
def nextpos(current,nextnb,pas,angle):
    (x,y)=current
    if nextnb%2==0:
        return(x+pas*cos(angle),y-pas*sin(angle))
    else:
        return(x+pas*cos(angle),y+pas*sin(angle))
    
def drawimage(pix,tot):
    image=Image.new('RGB',(pix,pix),'black')
    start=(pix//2,pix//2)
    plt.scatter(pix//2,pix//2,s=10,c='white')
    pas=8
    l=len(RGB)
    draw=ImageDraw.Draw(image)
    for n in range(1,tot+1):
        print(n)
        suite=collatz(n)
        ls=len(suite)
        current=start
        angle=np.pi-n*(2*np.pi/(tot+1))
        for i in range (ls-1):
            nextpoint=nextpos(current,suite[i+1],pas,angle)
            colour=RGB[int(i*l/ls)]
            draw.line((current[0],current[1],nextpoint[0],nextpoint[1]),fill=colour,width=2)
            current=nextpoint
    image.show()
    image.save(r'C:\Users\snice\OneDrive\Bureau\Computer Stuff\Python Projects\Collatz\Image_'+str(pix)+'_'+str(tot)+'_colours.png',"PNG")        

    