from controller import Robot

TIME_STEP = 16
DRIVE_SPEED = 5.0
BLADE_SPEED = 15.0

robot = Robot()

# Wheel Setup
wheel_names = ['fm_left_motor', 'm_left_motor', 'r_left_motor', 'fm_right_motor', 'm_right_motor', 'r_right_motor']
wheels = []
for name in wheel_names:
    motor = robot.getDevice(name)
    if motor:
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
        wheels.append(motor)

# Blade Setup
blade_names = ['blade_left_motor', 'blade_right_motor']
blades = []
for name in blade_names:
    motor = robot.getDevice(name)
    if motor:
        motor.setPosition(float('inf'))
        motor.setVelocity(0.0)
        blades.append(motor)

time_elapsed = 0.0
print("Simulation Ready: Moving to target weed...")

while robot.step(TIME_STEP) != -1:
    time_elapsed += TIME_STEP / 1000.0
    
    if time_elapsed < 4.5:
        # Rover aage badh raha hai
        for wheel in wheels:
            wheel.setVelocity(DRIVE_SPEED)
        for blade in blades:
            blade.setVelocity(0.0)
    else:
        # Weed par ruk kar blades on
        for wheel in wheels:
            wheel.setVelocity(0.0)
        for blade in blades:
            blade.setVelocity(BLADE_SPEED)