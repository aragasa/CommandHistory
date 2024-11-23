import inputs
import time

#controller = inputs.get_gamepad()

def getCommandHistory():
    
    while 1:
        # Issue!This is getting frames from last input
        start = time.time()
        events = inputs.get_gamepad()
    
        for event in events:
        
            if not event.code == 'SYN_REPORT':
            
            #if the state is zero it's neutral anything else something is being pressed including negative numbers
                currentState = event.stat
                
                end = time.time()
                elapsed = int((end - start) * 60)

                if elapsed >= 999:
                    print('frames: 999+')
                else:
                    print('frames: ', elapsed)

                print('Button: ', event.code)
                print('State:', currentState)

getCommandHistory()           

#for device in devices:
 #   print(device)