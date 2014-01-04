import Leap, sys, socket, time, random
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

IP = "192.168.1.101"
PORT = 56700

r = '31000034000000000000000000000000d073d500a1bf0000000000000000000066000000000000ffffe803000000000000'.decode('hex')
w = '31000034000000000000000000000000d073d500a1bf000000000000000000006600000000000000000080f00a13050000'.decode('hex')


lighton = '26000034000000000000000000000000d073d500a1bf00000000000000000000150000000001'.decode('hex')
lightoff = '26000034000000000000000000000000d073d500a1bf00000000000000000000150000000000'.decode('hex')


class LifxListener(Leap.Listener):
    isLoading = False
    light_flag = False
    LOCK_TIME = 1;

    def lightSwitch(self, lightState):
        if not(self.isLoading):
            sock = socket.socket()
            sock.connect((IP,PORT))
            print "Light turning " + str(lightState)
            if lightState == True:
                sock.send(lighton)
            else:
                sock.send(lightoff)
            sock.close()
            self.isLoading = True
            print "Info: Light is LOCKED"
            time.sleep(self.LOCK_TIME);
            self.isLoading = False
            self.light_flag = lightState
            print "Info: Light is UNLOCKED"

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"
        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        if not frame.hands.is_empty:
            # Gestures
            for gesture in frame.gestures():

                if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                    print "disco is starting"
                    disco()

                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    self.lightSwitch(not self.light_flag)
                   

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def disco():
    mysock = socket.socket()
    mysock.connect((IP,PORT))
    randomColor = random.randint(0,65537)
    #print hex(randomColor).strip('0x').zfill(4)
    temp1 = str(hex(randomColor).strip('0x').zfill(4))
    temp2 = str(hex(randomColor).strip('0x').zfill(4))
    temp3 = str(hex(randomColor).strip('0x').zfill(4))
    intensity = str(hex(randomColor).strip('0x').zfill(4))
    dcolor = ('31000034000000000000000000000000d073d500a1bf00000000000000000000660000' + temp1 + temp2  + temp3 + intensity +'000000000000').decode('hex')
    #print dcolor
    mysock.send(dcolor);
    #time.sleep(0.5)
    mysock.close();
        

def main():
    # Create the istener and controller
    listener = LifxListener()
    controller = Leap.Controller()

    # Have the listener receive events from the controller
    controller.add_listener(listener)

    
    #disco()



    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()
