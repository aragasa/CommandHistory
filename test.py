import inputs
import time

#controller = inputs.get_gamepad()


while 1:
     # Issue!This is getting frames from last input
    start = time.time()
    events = inputs.get_gamepad()
   
    for event in events:
       
        if not event.code == 'SYN_REPORT':
           
            currentState = event.state
            
            end = time.time()
            elapsed = int((end - start) * 60)

            if elapsed >= 999:
                print('frames: 999+')
            else:
                print('frames: ', elapsed)

            print('Button: ', event.code)
            print('State:', currentState)
            

#for device in devices:
 #   print(device)