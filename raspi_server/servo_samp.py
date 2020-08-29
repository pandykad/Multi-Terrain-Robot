import servomot
import RPi.GPIO as GPIO
import time

servomot.setup()
servomot.setangle_up()
servomot.setangle_down()
servomot.close()

GPIO.cleanup()