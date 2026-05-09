FROM ros:humble

# Install essential tools for CI + ROS build
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-colcon-common-extensions \
    && rm -rf /var/lib/apt/lists/*

# Create workspace inside container
WORKDIR /ros2_ws

# Copy only source code (important DevOps practice)
COPY ./src ./src

# Build ROS workspace inside container
RUN /bin/bash -c "source /opt/ros/humble/setup.bash && colcon build"

# Default shell
CMD ["/bin/bash"]
