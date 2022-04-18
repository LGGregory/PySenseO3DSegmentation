import sys
import json
import open3d as o3d
import datetime

if len(sys.argv) < 2:
    bag_name = "bag_"+datetime.now().strftime("%m-%d_%H-%M-%S")+".bag"    


with open("config.ini") as cf:
    rs_cfg = o3d.t.io.RealSenseSensorConfig(json.load(cf))

rs = o3d.t.io.RealSenseSensor()
rs.init_sensor(rs_cfg, 0, )
rs.start_capture(True)  # true: start recording with capture
for fid in range(150):
    im_rgbd = rs.capture_frame(True, True)  # wait for frames and align them
    # process im_rgbd.depth and im_rgbd.color

rs.stop_capture()