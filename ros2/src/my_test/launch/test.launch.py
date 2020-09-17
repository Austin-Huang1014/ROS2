from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_test',
            node_namespace='',
            node_executable='test',
            node_name='test_launch',
            output='screen',
        ),
    ])