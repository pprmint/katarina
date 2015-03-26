#!/usr/bin/python
"""
  Minimal example how to stream video to ffplay
  usage:
       ./video2stdout.py | ffplay -
"""
import sys

# http://stackoverflow.com/questions/10020325/make-python-stop-emitting-a-carriage-return-when-writing-newlines-to-sys-stdout
if sys.platform == "win32":
   import os, msvcrt
   msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY)

sys.path.append('..') # access to drone source without installation
from bebop import Bebop
from video import VideoFrames


g_vf = VideoFrames( onlyIFrames=False, verbose=False )
def videoCallback( data, robot=None, debug=False ):
    global g_vf
    g_vf.append( data )
    frame = g_vf.getFrame()
    if frame:
        sys.stdout.write( frame )
        sys.stdout.flush()


def video2stdout():
    drone = Bebop( metalog=None )
    drone.videoCbk = videoCallback
    drone.videoEnable()
    while True:
        drone.update()

if __name__ == "__main__":
    video2stdout()

# vim: expandtab sw=4 ts=4 

