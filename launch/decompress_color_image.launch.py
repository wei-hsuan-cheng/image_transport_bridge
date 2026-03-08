from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    input_compressed_topic = LaunchConfiguration('input_compressed_topic')
    output_raw_topic = LaunchConfiguration('output_raw_topic')

    return LaunchDescription([
        DeclareLaunchArgument(
            'input_compressed_topic',
            default_value='/camera/image_raw/compressed',
            description='Compressed image topic to decode.',
        ),
        DeclareLaunchArgument(
            'output_raw_topic',
            default_value='/camera/image_raw_uncompressed',
            description='Output raw image topic.',
        ),
        Node(
            package='image_transport',
            executable='republish',
            name='image_decompressor',
            output='screen',
            arguments=['compressed', 'raw'],
            remappings=[
                ('in/compressed', input_compressed_topic),
                ('out', output_raw_topic),
            ],
        )
    ])
