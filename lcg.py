"""Final implementation of LCG in Python. 4/13/19"""
import time
from RPIO import PWM

# Dictionary translating numbers to segments byte
num = {
    0:(1,1,1,1,1,1,0),
    1:(0,1,1,0,0,0,0),
    2:(1,1,0,1,1,0,1),
    3:(1,1,1,1,0,0,1),
    4:(0,1,1,0,0,1,1),
    5:(1,0,1,1,0,1,1),
    6:(1,0,1,1,1,1,1),
    7:(1,1,1,0,0,0,0),
    8:(1,1,1,1,1,1,1),
    9:(1,1,1,1,0,1,1),
    10:(0,0,0,0,0,0,1)}
err = "--"
# Pulse off and on (minimum of 4 for off state = 40 uS)
pulse = {
    0:4,    
    1:999}


def main():

    PWM.setup()
    PWM.init_channel(0)



    # Start alternating 10k uS pulses for the cathodes
    PWM.add_channel_pulse(0, 24, 0, 999)
    PWM.add_channel_pulse(0, 23, 1000, 999)

    rng.current=int(1*time.time())
    diceSize=0
    SetDual7Seg(diceSize)
    while True:
        try:
            while diceSize < 2 or diceSize > 100:
                diceSize=int(input("What size dice would you like to roll? "))
                if diceSize < 2 or diceSize > 100:
                    SetDual7Seg(err)
        except:
            print("Invalid input ")
            diceSize=0

        if(diceSize!=0):
            SetDual7Seg(dice(diceSize))
            diceSize=0
        else:
            SetDual7Seg(err)

    
    # Stop PWM for channel 0
    PWM.clear_channel(0)

    # Shutdown all PWM and DMA activity
    PWM.cleanup()

def SetDual7Seg( value ):
    if value==err:
        digits=(10,10)
    else: # Split passed value into separate digit integer list
        digits = list(map(int, "%02d" % value))
    # Set pulses for segments A-G (both digits) 
    #for i in range(7):
    print(value)
    PWM.add_channel_pulse(0, 2, 0, pulse[num[digits[0]][0]])
    PWM.add_channel_pulse(0, 3, 0, pulse[num[digits[0]][1]])
    PWM.add_channel_pulse(0, 4, 0, pulse[num[digits[0]][2]])
    PWM.add_channel_pulse(0, 7, 0, pulse[num[digits[0]][3]])
    PWM.add_channel_pulse(0, 8, 0, pulse[num[digits[0]][4]])
    PWM.add_channel_pulse(0, 9, 0, pulse[num[digits[0]][5]])
    PWM.add_channel_pulse(0, 10, 0, pulse[num[digits[0]][6]])

    PWM.add_channel_pulse(0, 2, 1000, pulse[num[digits[1]][0]])
    PWM.add_channel_pulse(0, 3, 1000, pulse[num[digits[1]][1]])
    PWM.add_channel_pulse(0, 4, 1000, pulse[num[digits[1]][2]])
    PWM.add_channel_pulse(0, 7, 1000, pulse[num[digits[1]][3]])
    PWM.add_channel_pulse(0, 8, 1000, pulse[num[digits[1]][4]])
    PWM.add_channel_pulse(0, 9, 1000, pulse[num[digits[1]][5]])
    PWM.add_channel_pulse(0, 10, 1000, pulse[num[digits[1]][6]])


def rng(m=2**32, a=1103515245, c=12345):
    rng.current = (a*rng.current + c) % m
    return rng.current

def dice(faceCount):
        rngRoll= rng()+1
        lowerBits = rngRoll%100
        upperBits = rngRoll>>8
        result = (lowerBits ^ upperBits)% faceCount + 1
        if (result == 100):
            result = 0
        return result
		

if __name__ == '__main__':
    main()

	
