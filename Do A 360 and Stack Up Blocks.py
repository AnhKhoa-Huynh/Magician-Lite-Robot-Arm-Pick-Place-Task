import time

# Replace these with the real Dobot API calls available on your machine.
# The function names below are written clearly so you can map them easily.

def set_end_effector_gripper():
    # Example: robot.set_end_effector("gripper")
    print("Set end effector: Gripper")

def home():
    # Example: robot.home()
    print("Home")

def go_to(x, y, z, r, motion_type="Straight Line"):
    # Example: robot.move_to(x, y, z, r, mode=motion_type)
    print(f"Go to X={x} Y={y} Z={z} R={r} motion type={motion_type}")

def gripper_close():
    # Example: robot.gripper_close()
    print("Gripper Close")

def gripper_open():
    # Example: robot.gripper_open()
    print("Gripper Open")

def set_r(r):
    # Example: robot.set_r(r)
    print(f"Set R = {r}")

def wait(seconds):
    print(f"Wait {seconds} second(s)")
    time.sleep(seconds)


def main():
    # Equivalent to: when flag is clicked

    set_end_effector_gripper()
    home()

    # Pick block 1
    go_to(200, 0, 80, 0, "Straight Line")
    go_to(200, 0, 20, 0, "Straight Line")
    gripper_close()
    wait(1)
    go_to(200, 0, 80, 0, "Straight Line")

    # 360 rotation
    set_r(90)
    set_r(180)
    set_r(270)
    set_r(0)

    # Place block 1
    go_to(200, 120, 80, 0, "Straight Line")
    go_to(200, 120, 20, 0, "Straight Line")
    gripper_open()
    wait(1)
    go_to(200, 120, 80, 0, "Straight Line")

    # Pick block 2
    go_to(150, 80, 80, 0, "Straight Line")
    go_to(150, 80, 20, 0, "Straight Line")
    gripper_close()
    wait(1)
    go_to(150, 80, 80, 0, "Straight Line")

    # Place block 2
    go_to(200, 120, 80, 0, "Straight Line")
    go_to(200, 120, 40, 0, "Straight Line")
    gripper_open()
    wait(1)
    go_to(200, 120, 80, 0, "Straight Line")

    # Pick block 3
    go_to(240, -80, 80, 0, "Straight Line")
    go_to(240, -80, 20, 0, "Straight Line")
    gripper_close()
    wait(1)
    go_to(240, -80, 80, 0, "Straight Line")

    # Place block 3
    go_to(200, 120, 80, 0, "Straight Line")
    go_to(200, 120, 60, 0, "Straight Line")
    gripper_open()
    wait(1)
    go_to(200, 120, 80, 0, "Straight Line")


if __name__ == "__main__":
    main()