import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class estado(Node):
    def __init__(self):
        super().__init__('Nodo_sensores')
        self._subscription_vel = self.create_subscription(
            Float32MultiArray,
            'vel',
            self.listener_callback_vel,
            10)
        self._subscription_bat = self.create_subscription(
            Float32MultiArray,
            'bat',
            self.listener_callback_bat,
            10)
        self.velocidad = None
        self.bateria = None

    def listener_callback_vel(self, msg):
        self.velocidad = list(msg.data)
        self.get_logger().info(f'Velocidad actual: {self.velocidad}')

    def listener_callback_bat(self, msg):
        self.bateria = list(msg.data)
        self.get_logger().info(f'Batería actual: {self.bateria}')

def main(args=None):
    rclpy.init(args=args)
    estado_robot = estado()
    rclpy.spin(estado_robot)
    estado_robot.destroy_node()
    rclpy.shutdown()