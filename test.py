import inputs
import time

#controller = inputs.get_gamepad()


while 1:
    events = inputs.get_gamepad()
    for event in events:
        #
        #startTime = time.perf_counter()
        currentState = event.state
        lastState = None

        if not event.code == 'SYN_REPORT' and not currentState == lastState:
            #stop getting time and post elapsed time then reset
            lastState = currentState
            currentState = event.state
            
            print('Button: ', event.code)
            print('State:', event.state)
            endTime = time.perf_counter()
            #elapsedTime = endTime - startTime
            #frames = int(elapsedTime / 60)
            #print('frames: ', elapsedTime)
            #print('start: ', startTime)
            #print('end: ', endTime)




#for device in devices:
 #   print(device)