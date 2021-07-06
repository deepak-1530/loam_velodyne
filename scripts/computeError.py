# compare error between scan matcher and loam trajectories
# compute difference between values with same timestamps

import numpy as np
import matplotlib.pyplot as plt

def plotTrajectory(loamTraj, scanMatcherTraj):
    plt.plot(loamTraj[:,1], loamTraj[:,2])
    plt.plot(scanMatcherTraj[:,1], scanMatcherTraj[:,2])
    plt.legend(["LOAM","ScanMatcher"])
    plt.show()
    

def computeMSE(loamTraj, scanMatcherTraj):
    print(loamTraj[loamTraj.shape[0]-1,1:4], scanMatcherTraj[scanMatcherTraj.shape[0]-1, 1:4])
    posErr = 0
    orientErr = 0
    count = 0

    mXLOAM = np.mean(loamTraj[:,2])
    mXSM   = np.mean(scanMatcherTraj[:,2])
    print(f'Mean X values are {mXLOAM, mXSM}')

    tLoam = loamTraj[:,0]
    tScanMatcher = scanMatcherTraj[:,0]

    for t in tLoam:
        if t in tScanMatcher:
            tIndex = np.where(tScanMatcher == t)
            if tIndex[0] < tLoam.shape[0]:
                posLoam = loamTraj[tIndex, 1:7].reshape(6)
                posScanMatcher = scanMatcherTraj[tIndex, 1:7].reshape(6)
                posErr += abs(posLoam - posScanMatcher)
                count += 1
    
    print(f'Mean Absolute Error is : {posErr/count}')

    plotTrajectory(loamTraj, scanMatcherTraj)

    

if __name__=="__main__":
    
    loamTraj        = np.load('/home/deepak/IIITD/catkin_ws/src/loam_velodyne/data/posesLoam.npy')#input("Enter loam trajectory file (npy): ")
    scanMatcherTraj = np.load('/home/deepak/IIITD/catkin_ws/src/loam_velodyne/data/posesScanMatcher.npy')#input("Enter scan matcher trajectory file (npy): ")

    computeMSE(loamTraj, scanMatcherTraj)