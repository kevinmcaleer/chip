from servo import Servo, servo2040
from time import sleep 
# from chip import Chip

# chip = Chip()

# chip.left_arm.wave(2) # Wave twice

neck = Servo(servo2040.SERVO_4)
left_shoulder = Servo(servo2040.SERVO_1)
left_hand = Servo(servo2040.SERVO_3)

for i in range(-70,10,1):
    neck.value(i)
    left_shoulder.value(i)
    left_hand.value(i)
    sleep(0.05)

