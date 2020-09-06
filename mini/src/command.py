#!/usr/bin/env python
import rospy
from devlib import getkey,setlimit
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

j=JointState()
rospy.init_node('control_node',anonymous=True)
pub = rospy.Publisher('joint_states', JointState, queue_size=100)
global length,link,terminate_flag
change_flag,count,joint,link=0,1,0,0

upper = 	[78,12,39]
lower = 	[0,0,0]
increment = 	[0.08,0.05,0.08]
initial_length= [0,0,2.96]
length=		[0,0,0]

def control(n):
	global joint,key_1,count,change_flag
	key_1 = getkey(100)
	if key_1 == "w":
		joint = initial_length[n] + count*increment[n]
		count = count+1
		count = setlimit(count,upper[link],lower[link])
		change_flag = 0
	if key_1 == "s":
		joint = initial_length[n] + count*increment[n]
		count = count-1
		count = setlimit(count,upper[link],lower[link])
		change_flag = 0
	if key_1 == "c":
		change_flag = 1
		print"Select new joint"
	return joint


terminate_flag=0
while (terminate_flag == 0):

	current_time = rospy.Time.now()	
	j.header = Header()
        j.header.stamp = rospy.Time.now()
	j.header.frame_id = "base_link"
	j.name = ['joint_1','joint_2','joint_3']
	if (change_flag == 1): 
		link = int(getkey(100))
		if (link < 3 and link >=0):
			print("  >> you have selected " + str(link))
			change_flag = 0
		else:
			print("WARNING : Please select appropriate link")
	else : 
		length[link] = control(link)
	
	j.position = [length[0],length[1],length[2]]
	j.velocity = [0]
	j.effort = [0]	
	pub.publish(j)
	terminate = getkey(10)
	if (terminate == "t"):
		terminate_flag = 1
	else:
		terminate_flag = 0
