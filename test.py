#!/usr/bin/env python
#license removed for brevity
import rospy
from std_msgs.msg import String
import serial
from imu_publisher.msg import IMU_data

ser = serial.Serial("/dev/ttyUSB0", baudrate = 115200, timeout = None)

def talker():
    #declares that node is publishing to 'GPS_topic' topic
    pub = rospy.Publisher('IMU_topic', String, queue_size=10)
    #tells rospy that the name of the node is 'talker'
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(40) # 40hz (loops forty times per second)
    msg = IMU_data()
    while not rospy.is_shutdown():
	data = ser.readline()
	print data
	try:	
		imu = str(data).split(',')
		msg.yaw = imu[1]
		msg.pitch = imu[2]
		msg.roll = imu[3]
		msg.MagX = imu[4]
		msg.MagY = imu[5]
		msg.MagZ = imu[6]
		msg.AccelX = imu[7]
		msg.AccelY = imu[8]
		msg.AccelZ = imu[9]
		msg.GyroX = imu[10]
		msg.GyroY = imu[11]
		msg.GyroZ = imu[12]
		#return 0 if null and nothing is returned			
		#if gps_data[i] is None:
		#return 0
	except:
		pass
        rospy.loginfo(msg)
        #pub.publish(String(data))
	pub.publish(str(msg))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    # exception so you don't accidentally continue executing code after sleepy
