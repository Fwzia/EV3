#Drawing letter " O "

#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
Medium_motor = MediumMotor(OUTPUT_A)
Large_motor1 = LargeMotor(OUTPUT_B)
Large_motor2 = LargeMotor(OUTPUT_C)

steer_Pair = MoveSteering(OUTPUT_B, OUTPUT_C)
tank = MoveTank(OUTPUT_B, OUTPUT_C)

Medium_motor.on_for_degrees(50, 500)
tank.on_for_rotations(50, 10, 6)
