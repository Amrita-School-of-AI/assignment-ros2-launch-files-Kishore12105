#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import TextSubstitution


def generate_launch_description() -> LaunchDescription:
    # You can also use parameter dictionaries or YAML files
    talker_params = {
        'message_prefix': 'ROS2'
        # You could add more parameters here if needed
    }

    return LaunchDescription([
        Node(
            package='ros2_launch_demo',
            executable='talker',
            name='talker',
            namespace='',               # default global namespace
            output='screen',
            parameters=[talker_params],
            # remappings=[('/chatter', '/my_chatter')]  # ← only if you want to change topic
        ),

        Node(
            package='ros2_launch_demo',
            executable='listener',
            name='listener',
            output='screen',
            # remappings=[('/chatter', '/my_chatter')]  # must match talker if remapped
        )
    ])