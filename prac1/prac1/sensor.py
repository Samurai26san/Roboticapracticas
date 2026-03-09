import rclpy
from rclpy.node import Node
import random
from std_msgs.msg import Float32MultiArray

class sensoresvelbat(Node):

    def __init__ (self):
        super().__init__('Nodo_sensores')
        self.publisher_bat = self.create_publisher(Float32MultiArray, 'bat', 10)
        self.publisher_vel = self.create_publisher(Float32MultiArray, 'vel', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg_bat = Float32MultiArray()
        msg_vel = Float32MultiArray()
        bat = [random.randint(0,100)]
        vel = [random.uniform(0,100)]
        msg_bat.data = bat
        msg_vel.data = vel
        self.publisher_bat.publish(msg_bat)
        self.publisher_vel.publish(msg_vel)
        self.get_logger().info('Velocidad "%s"' % list(msg_vel.data))
        self.get_logger().info('Batería "%s"' % list(msg_bat.data))
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    nodo_sensores = sensoresvelbat()

    rclpy.spin(nodo_sensores)

    nodo_sensores.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()