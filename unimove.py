#!/usr/bin/env python3
#! -*- coding: utf-8

import cv2
import numpy as np
import sys
from PIL import Image
from argparse import ArgumentParser

def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('input', type=str, help='Absolute/relative path to input file')
    argparser.add_argument('-f', '--frame', type=int, default=3, help='Number of interval frame')
    argparser.add_argument('-s', '--start', type=int, default=0, help='Time of union start')
    args = argparser.parse_args()
    return args

def unimove(inputFile, frameNum, startTime):
    cap = cv2.VideoCapture(inputFile)
    bgs_gsoc = cv2.bgsegm.createBackgroundSubtractorGSOC()
    
    cap.set(0, startTime * 1000)
    i = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        maskIm = bgs_gsoc.apply(frame)
        bg = bgs_gsoc.getBackgroundImage()
        fg = cv2.bitwise_and(frame,frame, mask=maskIm)
        
        cv2.imshow('fg', fg)
        cv2.imshow('bg', bg)
        
        if i == 0:
            union = frame
        elif i % frameNum == 0:
            union = unionFgBg(maskIm, fg, union)
            cv2.imshow('union', union)

        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            cv2.destroyAllWindows()
            exit()
        elif k == ord('w'):
            fileName = '../' + str(i) + '.jpg'
            cv2.imwrite(fileName, union)
        i += 1

def unionFgBg(mask, fg, union):
    notMask = cv2.bitwise_not(mask)
    maskedBg = cv2.bitwise_and(union, union, mask=notMask)
    res = fg + maskedBg
    return res

if __name__ == '__main__':
    args = get_option()
    
    inputFile = args.input 
    frame = args.frame
    startTime = args.start
    unimove(inputFile, frame, startTime)
