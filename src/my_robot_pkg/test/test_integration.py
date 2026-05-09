import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import unittest


class TestROSCommunication(unittest.TestCase):

    def test_pub_sub_flow(self):
        rclpy.init()

        node = Node("test_node")

        received_messages = []

        def callback(msg):
            received_messages.append(msg.data)

        pub = node.create_publisher(String, "topic", 10)
        sub = node.create_subscription(String, "topic", callback, 10)

        msg = String()
        msg.data = "hello_test"

        pub.publish(msg)

        import time
        time.sleep(1.0)

        self.assertIn("hello_test", received_messages)

        node.destroy_node()
        rclpy.shutdown()
