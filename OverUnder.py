#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
FrontLeft = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
FrontRight = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
controller_1 = Controller(PRIMARY)
BackLeft = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
BackRight = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
Catapult1 = Motor(Ports.PORT8, GearSetting.RATIO_18_1, True)
Catapult2 = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
LeftExpand = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
RightExpand = Motor(Ports.PORT20, GearSetting.RATIO_18_1, True)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration
global SpeedMult, Start_Calibrated, MatchLoad, Expand
SpeedMult = 0
Start_Calibrated = False
MatchLoad = False
Expand = False
LeftExpand.set_stopping(HOLD)
RightExpand.set_stopping(HOLD)

def Forward_Speed(Forward_Speed__Speed):
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    Set_all_wheel_velocities_Joystick(Forward_Speed__Speed)
    if math.fabs(controller_1.axis2.position()) <= 10:
        FrontRight.spin(FORWARD)
        FrontLeft.spin(REVERSE)
        BackRight.spin(FORWARD)
        BackLeft.spin(REVERSE)
    else:
        FrontRight.spin(FORWARD)
        FrontLeft.spin(FORWARD)
        BackRight.spin(FORWARD)
        BackLeft.spin(FORWARD)

def Set_all_wheel_velocities_Joystick(Set_all_wheel_velocities_Joystick__Joystick):
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    # Sets wheel velocities to the throttle multiplier of the joystick position
    if controller_1.axis1.position() > 20:
        if math.fabs(controller_1.axis2.position()) < 20:
            FrontRight.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
            FrontLeft.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
            BackRight.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
            BackLeft.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
        else:   
            FrontRight.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
            FrontLeft.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult / (controller_1.axis1.position()/10)), PERCENT)
            BackRight.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
            BackLeft.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult / (controller_1.axis1.position()/10)), PERCENT)
    elif controller_1.axis1.position() < -20:
        if math.fabs(controller_1.axis2.position()) < 20:
            FrontRight.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
            FrontLeft.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
            BackRight.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
            BackLeft.set_velocity((controller_1.axis1.position() * SpeedMult), PERCENT)
        else:
            FrontRight.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult / (controller_1.axis1.position()/-10)), PERCENT)
            FrontLeft.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
            BackRight.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult / (controller_1.axis1.position()/-10)), PERCENT)
            BackLeft.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
    else:
        FrontRight.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
        FrontLeft.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
        BackRight.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)
        BackLeft.set_velocity((Set_all_wheel_velocities_Joystick__Joystick * SpeedMult), PERCENT)

def Stop_motors():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    FrontRight.stop()
    FrontLeft.stop()
    BackRight.stop()
    BackLeft.stop()

def when_started1():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    # On startup set predefined variables
    Lock = 0
    SpeedMult = 1
    controller_1.screen.clear_screen()
    controller_1.screen.set_cursor(3, 1)
    controller_1.screen.print("LOCKED")
    while not Start_Calibrated:
        if controller_1.buttonDown.pressing():
            while controller_1.buttonDown.pressing():
                wait(5, MSEC)
            Lock = Lock + 1
        if controller_1.buttonLeft.pressing():
            while controller_1.buttonLeft.pressing():
                wait(5, MSEC)
            Lock = 0
            brain.timer.clear()
        wait(5, MSEC)
        if Lock >= 5 and brain.timer.time(SECONDS) < 2:
            controller_1.screen.clear_row(3)
            controller_1.screen.set_cursor(3, 1)
            controller_1.screen.print("UNLOCKED")
            Start_Calibrated = True
            wait(1, SECONDS)
            controller_1.screen.clear_row(3)
            controller_1.screen.set_cursor(1, 1)
            controller_1.screen.print("Throttle: ")
            controller_1.screen.print(SpeedMult * 10)

def onevent_controller_1buttonL1_pressed_0():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    # Throttle Decrease
    if SpeedMult > 0:
        SpeedMult = SpeedMult + -0.1
        controller_1.screen.clear_row(1)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        controller_1.screen.set_cursor(1, 1)
        controller_1.screen.print("Throttle: ")
        controller_1.screen.print(SpeedMult * 10)

def onevent_controller_1buttonR1_pressed_0():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    # Throttle Increase
    if SpeedMult < 1:
        SpeedMult = SpeedMult + 0.1
        controller_1.screen.clear_row(1)
        controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        controller_1.screen.set_cursor(1, 1)
        controller_1.screen.print("Throttle: ")
        controller_1.screen.print(SpeedMult * 10)

def when_started2():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    # Makes the catapult spin constantly for match loads
    while not Start_Calibrated:
        wait(5, MSEC)
    while True:
        if controller_1.buttonB.pressing():
            while controller_1.buttonB.pressing():
                wait(5, MSEC)
            # Starts the catapult
            MatchLoad = True
            Catapult1.set_velocity(50, PERCENT)
            Catapult2.set_velocity(50, PERCENT)
            Catapult1.spin(REVERSE)
            Catapult2.spin(REVERSE)
            controller_1.screen.set_cursor(3, 3)
            brain.screen.set_pen_color(Color.WHITE)
            controller_1.screen.print("MATCH LOADING")
            controller_1.rumble("-")
            while not controller_1.buttonB.pressing():
                wait(5, MSEC)
            while controller_1.buttonB.pressing():
                wait(5, MSEC)
            MatchLoad = False
            Catapult1.stop()
            Catapult2.stop()
            controller_1.screen.clear_row(3)
            controller_1.screen.set_cursor(controller_1.screen.row(), 1)
        wait(5, MSEC)

def when_started5():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    # Makes the Expansion Lock
    while not Start_Calibrated:
        wait(5, MSEC)
    while True:
        if controller_1.buttonY.pressing():
            while controller_1.buttonY.pressing():
                wait(5, MSEC)
            # Starts the Expansion
            Expand = True
            LeftExpand.set_velocity(10, PERCENT)
            RightExpand.set_velocity(10, PERCENT)
            LeftExpand.spin(FORWARD)
            RightExpand.spin(FORWARD)
            controller_1.screen.set_cursor(2, 1)
            controller_1.screen.print("EXPANDED")
            controller_1.rumble("..")
            while not controller_1.buttonY.pressing():
                wait(5, MSEC)
            while controller_1.buttonY.pressing():
                wait(5, MSEC)
            LeftExpand.set_velocity(10, PERCENT)
            RightExpand.set_velocity(10, PERCENT)
            LeftExpand.spin(REVERSE)
            RightExpand.spin(REVERSE)
            controller_1.screen.set_cursor(2,1)
            controller_1.screen.print("RETRACTING")
            controller_1.rumble("..")
            Expand = False
            wait(2, SECONDS)
            LeftExpand.stop()
            RightExpand.stop()
            controller_1.screen.clear_row(2)
        wait(5, MSEC)

def when_started3():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    while not Start_Calibrated:
        wait(5, MSEC)
    while True:
        if MatchLoad:
            brain.screen.set_font(FontType.PROP60)
            brain.screen.set_cursor(2, 2)
            brain.screen.print("MATCH LOADING")
            while MatchLoad:
                brain.screen.set_pen_color(Color.RED)
                brain.screen.clear_row(3)
                brain.screen.set_cursor(brain.screen.row(), 1)
                brain.screen.set_cursor(3, 9)
                brain.screen.print(".")
                if not MatchLoad:
                    break
                wait(1, SECONDS)
                brain.screen.clear_row(3)
                brain.screen.set_cursor(brain.screen.row(), 1)
                brain.screen.set_cursor(3, 7)
                brain.screen.print(".")
                brain.screen.set_cursor(3, 11)
                brain.screen.print(".")
                if not MatchLoad:
                    break
                wait(1, SECONDS)
                brain.screen.clear_row(3)
                brain.screen.set_cursor(3, 7)
                brain.screen.print(".")
                brain.screen.set_cursor(3, 9)
                brain.screen.print(".")
                brain.screen.set_cursor(3, 11)
                brain.screen.print(".")
                if not MatchLoad:
                    break
                wait(1, SECONDS)
                wait(5, MSEC)
        else:
            brain.screen.clear_row(2)
            brain.screen.set_cursor(brain.screen.row(), 1)
            brain.screen.clear_row(3)
            brain.screen.set_cursor(brain.screen.row(), 1)
        wait(5, MSEC)

def when_started4():
    global SpeedMult, Start_Calibrated, MatchLoad, Expand
    while not Start_Calibrated:
        wait(5, MSEC)
    while True:
        if math.fabs(controller_1.axis2.position()) > 10 or math.fabs(controller_1.axis1.position()) > 10:
            Forward_Speed(controller_1.axis2.position())
        if math.fabs(controller_1.axis1.position()) <= 10 and math.fabs(controller_1.axis2.position()) <= 10:
            Stop_motors()
        wait(5, MSEC)

# system event handlers
controller_1.buttonL1.pressed(onevent_controller_1buttonL1_pressed_0)
controller_1.buttonR1.pressed(onevent_controller_1buttonR1_pressed_0)
# add 15ms delay to make sure events are registered correctly.
wait(15, MSEC)

ws2 = Thread( when_started2 )
ws3 = Thread( when_started3 )
ws4 = Thread( when_started4 )
ws5 = Thread( when_started5 )
when_started1()
