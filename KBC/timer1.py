import time
import KBC.sound1 as sound1

def countdown_timer(seconds, stop_event):
    for sec in range(seconds,0, -1):
        if stop_event.is_set():
            return
        if sec<10:
            sound1.beep_sound()
        # if sec == seconds:  
        #     print(f"Time remaining: {sec} seconds", end='\r')
        # else:
        #     print(f"{sec} seconds", end='\r')  
        time.sleep(1)
    print("\nTime's Up!!")
    stop_event.set()
