#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String,Int32

class NodeSubscribe02(Node):
    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是%s!" % name)
        self.sub_microros_data=self.create_subscription(Int32,'cube_node',self.sub_callback,10)

    def sub_callback(self,msg):
        self.get_logger().info("i subed and data:%s" % msg.data)
def main(args=None):
    rclpy.init(args=args) # 初始化rclpy
    node = NodeSubscribe02("microros_sub")  # 新建一个节点

    rclpy.spin(node) # 保持节点运行，检测是否收到退出指令（Ctrl+C）
    node.destroy_node()
    rclpy.shutdown() # 关闭rclpy
