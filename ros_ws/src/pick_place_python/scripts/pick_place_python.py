#!/usr/bin/env python3

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import rospy
import tkinter as tk
from tkinter import messagebox
import math

from typing import List, Dict
from tf.transformations import quaternion_from_euler

def tkinterPopUp(msg):

    # console alert
    print("Opening pop-up message. If not visible, check for off-screen pop-up message.")

    # open and suppress initial tkinter window
    window = tk.Tk()
    # window.overrideredirect(True)
    # window.attributes("-alpha", 0)

    window.withdraw()

    messagebox.showinfo(title=None, message=msg)

    window.destroy()

class ConfigScreen:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.text_inputs: Dict[str, tk.Text] = {}
        print("Opening select screen. If not visible, check for it off-screen.")
        pass

    def run_pose_config(self, pose: geometry_msgs.msg.Pose = None, rpy: List[float] = None) -> geometry_msgs.msg.Pose:
        self.text_inputs.clear()

        if not pose:
            self.pose: geometry_msgs.msg.Pose = geometry_msgs.msg.Pose()
        else:
            self.pose: geometry_msgs.msg.Pose = pose

        if not rpy:
            self.rpy: List[float] = [0.0] * 3 
        else:
            self.rpy: List[float] = rpy

        position_header = tk.Frame(self.root)
        position_header.grid(row = 0, column = 0)
        tk.Label(position_header, text = "Position [m]", anchor = "center").pack()

        orientation_header = tk.Frame(self.root)
        orientation_header.grid(row = 0, column = 1)
        tk.Label(orientation_header, text = "Orientation [deg]", anchor = "center").pack()

        position_frame = tk.Frame(self.root)
        position_frame.grid(row = 1, column = 0)

        for ii, key in enumerate(["x", "y", "z"]):
            tk.Label(position_frame, text = f"{key}:").grid(row = ii, column = 0)
            
            self.text_inputs[key] = tk.Text(position_frame, height = 1, width = 5)
            self.text_inputs[key].insert(1.0, chars = f"{self.get_default_value(key):.3f}")
            self.text_inputs[key].grid(row = ii, column = 1)

        orientation_frame = tk.Frame(self.root)
        orientation_frame.grid(row = 1, column = 1)

        for ii, key in enumerate(["roll", "pitch", "yaw"]):
            tk.Label(orientation_frame, text = f"{key}:").grid(row = ii, column = 0)
            
            self.text_inputs[key] = tk.Text(orientation_frame, height = 1, width = 5)
            self.text_inputs[key].insert(1.0, chars = f"{self.get_default_value(key):.3f}")
            self.text_inputs[key].grid(row = ii, column = 1)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row = 2, column = 0, columnspan = 2)
        tk.Button(button_frame, height=2, width=10, text="Set pose", command=self.pose_button_callback).pack()

        self.root.mainloop()

        return self.pose

    def get_default_value(self, key):
        if key == "x":
            return self.pose.position.x
        elif key == "y":
            return self.pose.position.y
        elif key == "z":
            return self.pose.position.z
        elif key == "roll":
            return math.degrees(self.rpy[0])
        elif key == "pitch":
            return math.degrees(self.rpy[1])
        elif key == "yaw":
            return math.degrees(self.rpy[2])
        else:
            return ""

    def run_joint_config(self, joint_config: List[float] = None) -> List[float]:
        self.text_inputs.clear()

        if not joint_config:
            self.joint_config: List[float] = [0.0] * 7
        else:
            self.joint_config = joint_config

        header = tk.Frame(self.root)
        header.grid(row = 0, column = 0)
        tk.Label(header, text = "Robot arm joint config [deg]", anchor = "center").pack()

        body = tk.Frame(self.root)
        body.grid(row = 1, column = 0)

        for ii in range(7):
            tk.Label(body, text = f"J{ii+1}:").grid(row = ii, column = 0)
            
            self.text_inputs[ii] = tk.Text(body, height = 1, width = 5)
            self.text_inputs[ii].insert(1.0, chars=f"{math.degrees(self.joint_config[ii]):.3f}")
            self.text_inputs[ii].grid(row = ii, column = 1)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row = 2, column = 0, columnspan = 2)
        tk.Button(button_frame, height=2, width=10, text="Set pose", command=self.regular_button_callback).pack()

        self.root.mainloop()

        return self.joint_config

    def set_trajectory(self, pose: geometry_msgs.msg.Pose):
        self.text_inputs.clear()

        self.current_pose = pose

        self.pose: geometry_msgs.msg.Pose = self.current_pose

        position_header = tk.Frame(self.root)
        position_header.grid(row = 0, column = 0)
        tk.Label(position_header, text = "Current Position [m]", anchor = "center").pack()

        position_header = tk.Frame(self.root)
        position_header.grid(row = 0, column = 1)
        tk.Label(position_header, text = "Target Position [m]", anchor = "center").pack()

        position_frame = tk.Frame(self.root)
        position_frame.grid(row = 1, column = 0, columnspan = 2)

        for ii, key in enumerate(["x", "y", "z"]):
            tk.Label(position_frame, text = f"{key}: {self.get_default_value(key):.3f}").grid(row = ii, column = 0)
            tk.Label(position_frame, text = "Target: ").grid(row = ii, column = 1)
            self.text_inputs[key] = tk.Text(position_frame, height = 1, width = 5)
            self.text_inputs[key].insert(1.0, chars = f"{self.get_default_value(key):.3f}")
            self.text_inputs[key].grid(row = ii, column = 1)

        button_frame = tk.Frame(self.root)
        button_frame.grid(row = 2, column = 0, columnspan = 2)
        tk.Button(button_frame, height=2, width=10, text="Set pose", command=self.regular_button_callback).pack()

        self.root.mainloop()

        return self.pose

    def check_inputs(self):
        for key in self.text_inputs.keys():
            _output = self.text_inputs[key].get(1.0, "end-1c")
            if not _output:
                tkinterPopUp(msg="Incomplete input")
                return False
            else:
                self.set_input(key, float(_output))

        return True

    def pose_button_callback(self):
        if self.check_inputs():
    
            self.pose.orientation.x, self.pose.orientation.y, self.pose.orientation.z, self.pose.orientation.w = quaternion_from_euler(
                *self.rpy,
                axes = 'sxyz'
            )

            self.root.destroy()

    def regular_button_callback(self):
        if self.check_inputs():
            self.root.destroy()

    def set_input(self, key, val):
        if key == "x":
            self.pose.position.x = val
        elif key == "y":
            self.pose.position.y = val
        elif key == "z":
            self.pose.position.z = val
        elif key == "roll":
            self.rpy[0] = math.radians(val)
        elif key == "pitch":
            self.rpy[1] = math.radians(val)
        elif key == "yaw":
            self.rpy[2] = math.radians(val)
        elif key in [i for i in range(7)]:
            self.joint_config[key] = math.radians(val)

def create_node(name = "node"):
    if not rospy.get_node_uri():
        rospy.init_node(name, anonymous = True)
    else:
        return

if __name__ == "__main__":
    # Create ROS node
    create_node(name = "pick_place_node")

    # Create robot/scene objects
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()

    # Set the move group to the arm
    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    
    # Trajectory publisher
    display_trajectory_publisher = rospy.Publisher(
        "/move_group/display_planned_path",
        moveit_msgs.msg.DisplayTrajectory,
        queue_size=20,
    )

    # Initialize success flag
    success = False

    tkinterPopUp(msg = "Select joint config for panda arm")
    while not success:
        # Set joint config from select screen
        joint_config: List[float] = ConfigScreen().run_joint_config(move_group.get_current_joint_values())
        
        # Apply joint config to the move group and wait for the motion to finish
        success = move_group.go(joint_config, wait=True)

        if not success:
            tkinterPopUp(msg = "Trajectory unsuccessful, try again")

        # Calling ``stop()`` ensures that there is no residual movement
        move_group.stop()

    # Reset success flag
    success = False

    tkinterPopUp(msg = "Select target eef pose for panda arm")
    # Loop until a successful trajectory is completed
    while not success:
        # Set the target pose
        pose: geometry_msgs.msg.Pose = ConfigScreen().run_pose_config(move_group.get_current_pose().pose, move_group.get_current_rpy())
        
        # Move to target pose
        move_group.set_pose_target(pose)

        # `go()` returns a boolean indicating whether the planning and execution was successful.
        success = move_group.go(wait=True)

        if not success:
            tkinterPopUp(msg = "Trajectory unsuccessful, try again")

        # Calling `stop()` ensures that there is no residual movement
        move_group.stop()

    # It is always good to clear your targets after planning with poses.
    # Note: there is no equivalent function for clear_joint_value_targets().
    move_group.clear_pose_targets()

    tkinterPopUp(msg = "Select trajectory via three sequential waypoints for the arm where you will pick up a box")

    # Create cartesian path
    waypoints: List[geometry_msgs.msg.Pose] = []

    for _ in range(3):
        if len(waypoints) == 0:
            waypoints.append(ConfigScreen().set_trajectory(move_group.get_current_pose().pose))
        else:
            waypoints.append(ConfigScreen().set_trajectory(waypoints[-1]))

    plan, _ = move_group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
    )

    # Create object for `DisplayTrajectory` topic
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)

    # Publish
    display_trajectory_publisher.publish(display_trajectory)

    # wait 1 second
    rospy.sleep(1)

    move_group.execute(plan, wait=True)

    # Add box to scene
    box_pose = geometry_msgs.msg.PoseStamped()
    box_pose.header.frame_id = "panda_hand"
    box_pose.pose.orientation.w = 1.0
    box_pose.pose.position.z = 0.11  # above the panda_hand frame
    box_name = "box"
    scene.add_box(box_name, box_pose, size=(0.075, 0.075, 0.075))

    # Attach box to robot hand
    grasping_group = "panda_hand"
    touch_links = robot.get_link_names(group=grasping_group)
    scene.attach_box(move_group.get_end_effector_link(), box_name, touch_links=touch_links)

    tkinterPopUp(msg = "Select trajectory via three sequential waypoints for the arm to where the box will be placed")

    # Create cartesian path w/ collisions
    waypoints: List[geometry_msgs.msg.Pose] = []

    for _ in range(3):
        if len(waypoints) == 0:
            waypoints.append(ConfigScreen().set_trajectory(move_group.get_current_pose().pose))
        else:
            waypoints.append(ConfigScreen().set_trajectory(waypoints[-1]))

    plan, _ = move_group.compute_cartesian_path(
        waypoints, 0.01, 0.0  # waypoints to follow  # eef_step
    )

    # reset DisplayTrajectory topic
    display_trajectory = moveit_msgs.msg.DisplayTrajectory()
    display_trajectory.trajectory_start = robot.get_current_state()
    display_trajectory.trajectory.append(plan)

    # Publish
    display_trajectory_publisher.publish(display_trajectory)

    # wait 1 second
    rospy.sleep(1)

    move_group.execute(plan, wait=True)

    # Remove box from scene
    scene.remove_attached_object(move_group.get_end_effector_link(), name=box_name)
    scene.remove_world_object(box_name)

    tkinterPopUp("Pick and place successful, ending program")