# image_transport_bridge

Small ROS 2 package for decoding image transport topics back to raw
`sensor_msgs/msg/Image` topics using `image_transport republish`.

## Prerequisites

For ROS 2 Humble, install:

```bash
sudo apt update
sudo apt install -y \
  ros-humble-image-transport \
  ros-humble-image-transport-plugins
```

## Build

From the workspace root:

```bash
cd /ros2_ws
export CMAKE_BUILD_PARALLEL_LEVEL=4
export MAKEFLAGS=-j4
export NINJAFLAGS=-j4
colcon build --symlink-install \
  --packages-select image_transport_bridge \
  --executor sequential --parallel-workers 1 \
  --cmake-args -DBUILD_TESTING=OFF \
  && . install/setup.bash
```

## Launch

### Color example

```bash
ros2 launch image_transport_bridge decompress_color_image.launch.py \
  input_compressed_topic:=/camera/image_raw/compressed \
  output_raw_topic:=/camera/image_raw_uncompressed
```

### Depth example

```bash
ros2 launch image_transport_bridge decompress_depth_image.launch.py \
  input_compressed_depth_topic:=/camera/depth/image_rect_raw/compressedDepth \
  output_raw_topic:=/camera/depth/image_rect_raw_uncompressed
```

## Notes

- Color transport name is `compressed`.
- Depth transport name is `compressedDepth`.
- The output topics are raw `sensor_msgs/msg/Image` topics.
