################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap
import sys
import thread
import time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import os

#Arduino interaction code
import serial
connected = False

ser = serial.Serial('/dev/ttyACM0')


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"
        
    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"
    def on_focus_gained(self, controller):
        print "Focused"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        """
        print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
              frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
        """
        # Get hands
        
        for hand in frame.hands:

            #Testing out pinch
            
            #pinch = hand.punch_strength

            #print pinch


            choice = 0

            #ser = serial.Serial('/dev/ttyACM1')
            #ser0 = serial.Serial('/dev/ttyACM0')
            
            #ser2 = serial.Serial('/dev/ttyACM2')
            #ser3 = serial.Serial('/dev/ttyACM3')
            #ser4 = serial.Serial('/dev/ttyACM4')
            #ser5 = serial.Serial('/dev/ttyACM5')

            #if(ser.isOpen() == True):
                #choice = 1
            #elif(ser2.isOpen() == True):
                 #choice = 2
            #elif(ser3.isOpen() == True):
                #choice = 3
            #elif(ser4.isOpen() == True):
                #choice = 4
            #elif(ser5.isOpen() == True):
                #choice = 5
            #elif(ser0.isOpen() == True):
                #choice = 0
            
            handType = "Left hand" #if hand.is_left else "Right hand"

            
            if hand.is_left:
                print "Working with Left"

                #if(choice == 1):
                ser.write("1")
                #elif(choice == 2):
                    #ser2.write("1")
                #elif(choice == 3):
                    #ser3.write("1")
                #elif(choice == 4):
                    #ser4.write("1")
                #elif(choice == 5):
                    #ser5.write("1")
                #elif(choice == 0):
                    #ser0.write("1")
                
            else:
                ser.write("1")
                print "Working with Right"
            
            
                    
            
      
    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()
    
    #Connecting Leap Motion
    print "Connecting. . ."
    SampleListener.on_connect(listener, controller)

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    SampleListener.on_focus_gained(listener, controller)
    
    print "Ready to listen. . ."
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."

    i = 0
    while(True):
        
        controller.add_listener(listener)
        SampleListener.on_focus_gained(listener, controller)

        time.sleep(1000)

        
    try:
        
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
        


if __name__ == "__main__":
    main()
