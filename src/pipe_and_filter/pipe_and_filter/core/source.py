from rclpy.node import Node
from std_msgs.msg import Int64

import time

class Source(Node):

    def __init__(self, name='source', timer_period=1.0, output='output', **args):
        super().__init__(name, **args)

        self.output_publisher = self.create_publisher(Int64, output, 10)
        self.time_publisher = self.create_publisher(Int64, 'source_time', 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def generate_number(self):
        pass

    def timer_callback(self):
        out = Int64()
        out.data = self.generate_number()
        self.output_publisher.publish(out)

        out.data = time.time_ns()
        self.time_publisher.publish(out)

