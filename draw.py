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


#Drawing letter " q "

#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
Medium_motor = MediumMotor(OUTPUT_A)
Large_motor1 = LargeMotor(OUTPUT_B)
Large_motor2 = LargeMotor(OUTPUT_C)

steer_Pair = MoveSteering(OUTPUT_B, OUTPUT_C)
tank = MoveTank(OUTPUT_B, OUTPUT_C)

Medium_motor.on_for_degrees(50, 500)
steer_Pair.on_for_degrees(steering = 90, speed = 75, degrees = 1080)
tank.on_for_degrees(50, 50, 360)

#Drawing letter " F "

#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
Medium_motor = MediumMotor(OUTPUT_A)
Large_motor1 = LargeMotor(OUTPUT_B)
Large_motor2 = LargeMotor(OUTPUT_C)

steer_Pair = MoveSteering(OUTPUT_B, OUTPUT_C)
tank = MoveTank(OUTPUT_B, OUTPUT_C)

Medium_motor.on_for_degrees(50, 500)
tank.on_for_degrees(70, 70, 360)
steer_Pair.on_for_degrees(steering = 50, speed = 75, degrees = 180)
steer_Pair.on_for_degrees(steering = -90, speed = 85, degrees = 360)
steer_Pair.on_for_degrees(steering = 60, speed = 75, degrees = 180)


#Drawing letter " C "

#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
Medium_motor = MediumMotor(OUTPUT_A)
Large_motor1 = LargeMotor(OUTPUT_B)
Large_motor2 = LargeMotor(OUTPUT_C)

steer_Pair = MoveSteering(OUTPUT_B, OUTPUT_C)
tank = MoveTank(OUTPUT_B, OUTPUT_C)

tank.on_for_rotations(50, 10, 3)


#Drawing letter " P "

#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, MediumMotor, MoveTank, MoveSteering, OUTPUT_A, OUTPUT_B, OUTPUT_C
Medium_motor = MediumMotor(OUTPUT_A)
Large_motor1 = LargeMotor(OUTPUT_B)
Large_motor2 = LargeMotor(OUTPUT_C)

steer_Pair = MoveSteering(OUTPUT_B, OUTPUT_C)
tank = MoveTank(OUTPUT_B, OUTPUT_C)

Medium_motor.on_for_degrees(50, 500)
tank.on_for_degrees(70, 70, 360)
steer_Pair.on_for_degrees(steering = 90, speed = 75, degrees = 720)

