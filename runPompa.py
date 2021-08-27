from gpiozero import LED
from signal import pause 
import sys
from commandi2c import rlyOn , rlyOff

pompa = LED(24)

# memastikan pompa off
rlyOn() 
pompa.on() 
print("pompa.on()")

while 1:
    toggle = sys.stdin.read(1)
    print(toggle)

    if toggle == "1":
        print("Pompa nyala")
        rlyOn() 
        pompa.on()
    else:
        print("Pompa mati")
        rlyOff() 
        pompa.off()
    
    sys.stdout.flush()