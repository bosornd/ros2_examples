from rclpy.node import Node
from std_msgs.msg import Int64

import time

class Sink(Node):

    def __init__(self, name='sink', input='input', **args):
        super().__init__(name, **args)

        self.time_publisher = self.create_publisher(Int64, 'sink_time', 10)
        self.subscription = self.create_subscription(Int64, input, self.callback, 10)

    def process_number(self, number):
        pass

    def callback(self, msg):
        self.process_number(msg.data)

        out = Int64()
        out.data = time.time_ns()
        self.time_publisher.publish(out)
