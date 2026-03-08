from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    input_compressed_depth_topic = LaunchConfiguration('input_compressed_depth_topic')
    output_raw_topic = LaunchConfiguration('output_raw_topic')
    use_sim_time = LaunchConfiguration('use_sim_time')

    return LaunchDescription([
        DeclareLaunchArgument(
            'input_compressed_depth_topic',
            default_value='/camera/depth/image_raw/compressedDepth',
            description='Compressed depth image topic to decode.',
        ),
        DeclareLaunchArgument(
            'output_raw_topic',
            default_value='/camera/depth/image_raw_uncompressed',
            description='Output raw depth image topic.',
        ),
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use /clock from rosbag or simulation.',
        ),
        Node(
            package='image_transport',
            executable='republish',
            name='depth_image_decompressor',
            output='screen',
            arguments=['compressedDepth', 'raw'],
            parameters=[{'use_sim_time': use_sim_time}],
            remappings=[
                ('in/compressedDepth', input_compressed_depth_topic),
                ('out', output_raw_topic),
            ],
        )
    ])
