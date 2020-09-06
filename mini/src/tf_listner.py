#!/usr/bin/env python  
import roslib,rospy,tf,time
from math import sin, cos, pi  
from std_msgs.msg import Float32MultiArray,MultiArrayDimension
f=Float32MultiArray()


if __name__ == '__main__':
	rospy.init_node('End_point',anonymous=True)
	f.layout.data_offset = 0 
	f.layout.dim = [MultiArrayDimension()]
	f.layout.dim[0].label = "End_co-ordinates"
	f.layout.dim[0].size = 4
	f.layout.dim[0].stride = 4
	pub = rospy.Publisher('current_coordinates',Float32MultiArray,queue_size=100)        
	listener = tf.TransformListener()
	while not rospy.is_shutdown():
		try:       			
			(t0,r0)   = listener.lookupTransform('/link_1', '/base_link', rospy.Time(0))
			(t1,r1) = listener.lookupTransform('/link_2', '/link_1', rospy.Time(0))
			(t2,r2) = listener.lookupTransform('/link_3', '/link_2', rospy.Time(0))
			base_angle = tf.transformations.euler_from_quaternion(r0)
			r = base_angle[0]*(180/pi)
			p = base_angle[1]*(180/pi)
			y = base_angle[2]*(180/pi)
			height = t1[1]			
			global curr_co			
			curr_co=[r,p,y,height]
			print curr_co						
		except:
			continue  
		f.data=curr_co
		pub.publish(f)
           
