import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import unittest
import time


class TestROSCommunication(unittest.TestCase):

    def test_pub_sub_flow(self):
        rclpy.init()

        node = Node("test_node")

        received = []

        def callback(msg):
            received.append(msg.data)

        pub = node.create_publisher(String, "topic", 10)
        node.create_subscription(String, "topic", callback, 10)

        msg = String()
        msg.data = "hello_test"

        # give ROS time to register subscription
        time.sleep(0.5)

        pub.publish(msg)

        # IMPORTANT: allow ROS to process callback
        end_time = time.time() + 2.0
        while time.time() < end_time:
            rclpy.spin_once(node, timeout_sec=0.1)

        node.destroy_node()
        rclpy.shutdown()

        self.assertIn("hello_test", received)
