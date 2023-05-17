from msilib.schema import SelfReg
from typing import Self
import rclpy
from rclpy.node import Node
#SetUP für RFID Modell RC522
#Dependecy-issues yet to be resolved
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

from std_msgs.msg import String
#Fähigkeit zu Erstellung von nodes ect.


class RfidPublisher(Node):

    def __init__(self):
        super().__init__('rfid_publisher')
        
        
        
        #timer_period = 0.5  # seconds
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        #self.i = 0

    #def timer_callback(self):
        #msg = String()
        #msg.data = 'Hello World: %d' % self.i
        #self.publisher_.publish(msg)
        #self.get_logger().info('Publishing: "%s"' % msg.data)
        #self.i += 1


def main(args=None):
    rclpy.init(args=args)

    node = RfidPublisher('rfid_publisher')

    pub = node.create_publisher(String, 'rfid_tag', 10)

    reader = SimpleMFRC522()

    #Repeat
    rclpy.spin(rfid_publisher)
    # when the garbage collector destroys the node object)
    rfid_publisher.destroy_node()
    rclpy.shutdown()

    try:
        while True:
            id, text = reader.read()
            msg = String()
            msg.data = str(id)
            pub.publisher_.publish(msg)
            node.get_logger().info('Publishing: "%s"' % msg.data)

if __name__ == '__main__':
    main()