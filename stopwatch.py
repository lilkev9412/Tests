import mraa 
import time
import pyupm_i2clcd as lcd

LED_GPIO = 4                   # The LED pin
BUTTON_GPIO = 3                # The button GPIO
led = mraa.Gpio(LED_GPIO)      # Get the LED pin object
led.dir(mraa.DIR_OUT)          # Set the direction as output
btn = mraa.Gpio(BUTTON_GPIO)   # Get the button pin object
btn.dir(mraa.DIR_IN)           # Set the direction as input

lcdDisplay = lcd.Jhd1313m1(0, 0x3E, 0x62)

ledState = False               # LED is off to begin with
led.write(0)

def getButtonPress():
    """ This function blocks until it registers an valid key press """
    while 1:
        if (btn.read() != 0):
            # No button press detected
            continue
        else:
            # Detected a click
            time.sleep(0.05)   # The debounce delay
            # Wait for the button to settle down
            if (btn.read() == 1):
                # and read the button state, if it is still pressed,
                # register this as an valid click
                return
            else:
                # else, ignore this button press and wait for it to be pressed
                continue

if __name__ == '__main__':
    initValue = time.time()
    while 1:
        
        # wait until someone clicks the button
        
        
        timePassed = time.time()-initValue
        lcdDisplay.setCursor(0, 0)
        lcdDisplay.setColor(0,0,255)
        lcdDisplay.write(str(timePassed))
        getButtonPress()
        # Button click, detected, now toggle the LED

        if ledState == True:
            led.write(1)
            ledState = False

        else:
            led.write(0)
            ledState = True
        
        time.sleep(0.005)