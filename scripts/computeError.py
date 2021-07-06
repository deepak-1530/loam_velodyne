# compare error between scan matcher and loam trajectories
# compute difference between values with same timestamps

import numpy as np
import math

def computeMSE(loamTraj, scanMatcherTraj):
    print(loamTraj.shape, scanMatcherTraj.shape)
    posErr = 0
    orientErr = 0
    count = 0

    tLoam = loamTraj[:,0]
    tScanMatcher = scanMatcherTraj[:,0]

    for t in tLoam:
        if(t in tScanMatcher):
            tIndex = np.where(tScanMatcher == t)
            if tIndex[0] < tLoam.shape[0]:
                posLoam = loamTraj[tIndex, 1:7].reshape(6)
                posScanMatcher = scanMatcherTraj[tIndex, 1:7].reshape(6)
                posErr += abs(posLoam - posScanMatcher)
                count += 1
    
    print(posErr/count)

                
if __name__=="__main__":
    
    loamTraj        = np.load('/home/deepak/IIITD/catkin_ws/src/loam_velodyne/data/posesLoam.npy')#input("Enter loam trajectory file (npy): ")
    scanMatcherTraj = np.load('/home/deepak/IIITD/catkin_ws/src/loam_velodyne/data/posesScanMatcher.npy')#input("Enter scan matcher trajectory file (npy): ")

    computeMSE(loamTraj, scanMatcherTraj)