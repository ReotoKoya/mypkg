#!/usr/bin/python3
import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

rclpy.init()
node = Node("talker")


def cb(request, response):
    if request.name == "小屋玲旺斗":
        response.age = 20
    else:
        response.age = 300
    return response



def main():
    srv =  node.create_service(Query, "query" , cb)
    rclpy.spin(node)
