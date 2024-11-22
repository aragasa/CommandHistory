import inputs
from datetime import time

#controller = inputs.get_gamepad

time #input time held start difference with time released

fps = 60

frames = time / fps

while 1:
    events = inputs.get_gamepad()
    for event in events:
        print(event.ev_type, event.code,event.state)
#for device in devices:
 #   print(device)