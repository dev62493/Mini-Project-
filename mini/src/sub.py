import rospy
from std_msgs.msg import Int32

def call_my_function(dev):
	ans = dev.data
	print ans

while not rospy.is_shutdown():
	rospy.init_node('Node_recieve')	
	sub = rospy.Subscriber("topic",Int32,call_my_function)
	rospy.spin()
