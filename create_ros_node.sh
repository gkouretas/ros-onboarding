#!/bin/sh

if pgrep -x roscore 
then 
    echo "ROS node already exists, exiting"
else
    echo "Creating ROS node";
    roscore
fi