"""
Example of how to send MANUAL_CONTROL messages to the autopilot using
pymavlink.
This message is able to fully replace the joystick inputs.
"""
# Import mavutil
from pymavlink import mavutil

# Create the connection
the_connection = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

def test_control_rover():
    # Wait a heartbeat before sending commands
    the_connection.wait_heartbeat()
    

    # Send a positive x value, negative y, negative z,
    # positive rotation and no button.
    # https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
    # Warning: Because of some legacy workaround, z will work between [0-1000]
    # where 0 is full reverse, 500 is no output and 1000 is full throttle.
    # x,y and r will be between [-1000 and 1000].
    the_connection.mav.manual_control_send(
        the_connection.target_system,
        500,
        -500,
        250,
        500,
        0)

    # To active button 0 (first button), 3 (fourth button) and 7 (eighth button)
    # It's possible to check and configure this buttons in the Joystick menu of QGC
    buttons = 1 + 1 << 3 + 1 << 7
    the_connection.mav.manual_control_send(
        the_connection.target_system,
        0,
        0,
        500, # 500 means neutral throttle
        0,
        buttons)