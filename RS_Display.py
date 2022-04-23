#Nearly all code from O3d example.

import sys
import json
import open3d as o3d
import datetime

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter a bag name.")
        exit()
    else:
        bag_name = sys.argv[1]


