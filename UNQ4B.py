import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO3 (pin 5) set up as input. It is pulled up to stop false signals
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# wait for the pin to be sorted with GND and, if so, halt the system
GPIO.wait_for_edge(18, GPIO.FALLING)
subprocess.call(['shutdown -h now "System halted by power switch "'], shell=True)

# clean up GPIO on normal exit
GPIO.cleanup()  
