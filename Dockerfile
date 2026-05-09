FROM ros:humble

# Install Python tools
RUN apt-get update && apt-get install -y \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create workspace inside container
WORKDIR /ros2_ws

# Copy your code into container
COPY ./src ./src

# Source ROS and build workspace
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"

# Default command when container starts
CMD ["/bin/bash"]
