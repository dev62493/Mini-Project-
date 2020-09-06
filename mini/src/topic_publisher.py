import rospy
from std_msgs.msg import Int32

i= Int32()

def fibonaci(var):
	[i,j,k]=[0,1,0]
	while ( k < var ):	
		k=i+j
		i=j
		j=k
		pub.publish(k)
		rate.sleep()



while not rospy.is_shutdown():
	rospy.init_node('node_name')
	pub = rospy.Publisher("topic", Int32, queue_size=50)
	rate = rospy.Rate(1)
	limit = input(" Enter the limit ")
	fibonaci(limit)




