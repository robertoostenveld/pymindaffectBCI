from utopia2output import *
from time import sleep
from pyb00st.movehub import MoveHub
from pyb00st.constants import *

mymovehub = MoveHub('00:16:53:a5:6f:8a', 'Auto', 'hci0')

try:
   mymovehub.start()
   mymovehub.subscribe_all()
   mymovehub.listen_angle_sensor(PORT_C)
   mymovehub.listen_angle_sensor(PORT_A)
   mymovehub.listen_angle_sensor(PORT_B)

except:
    print('Cannot connect to Boost.')


# define our action functions
def head (objID):
    start_angle_c = mymovehub.last_angle_C
    print('move head')
    try:
        mymovehub.run_motor_for_angle(MOTOR_C, 90, -20)
        sleep(1)
        mymovehub.run_motor_for_angle(MOTOR_C, 270, 20)
        sleep(2)
        mymovehub.run_motor_for_angle(MOTOR_C, 180, -50)
        sleep(2)
        mymovehub.run_motor_for_angle(MOTOR_C, 100, 10)
        sleep(2)
        mymovehub.run_motor_for_angle(MOTOR_C, 100, -10)
        sleep(2)
        mymovehub.return_to_start(MOTOR_C,start_angle_c,mymovehub.last_angle_C)
        sleep(1)
    except:
        print('Cannot connect to Boost.')
def tail (objID):
    print('wiggle tail')
    start_angle_a = mymovehub.last_angle_A
    try:
        mymovehub.run_motor_for_angle(MOTOR_A, 60,  5)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 120, -50)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 120, 50)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 120, -5)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 60, 5)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 60, -50)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 120, 50)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 120, -5)
        sleep(0.5)
        mymovehub.run_motor_for_angle(MOTOR_A, 60,  5)
        sleep(1)
        mymovehub.return_to_start(MOTOR_A, start_angle_a, mymovehub.last_angle_A)
        sleep(1)
    except:
        print('Cannot connect to Boost.')

def legs (objID):
    print('move legs')
    start_angle_c = mymovehub.last_angle_C
    try:
        mymovehub.run_motor_for_angle(MOTOR_B, 180, -20)
        sleep(2)
        mymovehub.run_motor_for_angle(MOTOR_B, 100, -20)
        sleep(1)
        mymovehub.run_motor_for_angle(MOTOR_B, 100, 50)
        sleep(2)
        mymovehub.run_motor_for_angle(MOTOR_B, 180, 20)
        sleep(2)
        mymovehub.return_to_start(MOTOR_B, start_angle_c, mymovehub.last_angle_C)
    except:
        print('Cannot connect to Boost.')


# IMPORTANT: Somewhere:
# mymovehub.stop()
#We then connect them to their trigger object identifiers
objectID2Action = { 50 :head, 52 :tail, 51 :legs}
# create the output object
utopia2output=Utopia2Output(outputPressThreshold=None)
# replace the default action dictionary with ours. N.B. be careful
utopia2output.objectID2Action=objectID2Action
# run the output module
utopia2output.run()