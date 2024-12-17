import time
import winsound

def beep_sound():
    # Play a beep sound at 1000 Hz for 100 ms
    winsound.Beep(1000, 100)

def countdown_timer(seconds, stop_event):
    stop_event.clear()
    for sec in range(seconds, 0, -1):
        if stop_event.is_set():
            print("Timer stopped.")
            return
        if sec <= 5:
            beep_sound()
        time.sleep(1)
    print("Timer finished.")
    stop_event.set()