from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_launch_demo',
            executable='talker',
            name='talker',
            output='screen',
            parameters=[{'message_prefix': 'ROS2'}]
        ),
        Node(
            package='ros2_launch_demo',
            executable='listener',
            name='listener',
            output='screen'
        ),
    ])