import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
class kMeans:
    def __init__(s):
        s.kMeansCount = 4               

    def loadData(s,file):
        data = np.loadtxt(file)
        s.numberOfRows = int(len(data) / 3)            
        dataOut = np.reshape(data,(s.numberOfRows,3))         
        s.min,s.max = np.min(dataOut),np.max(dataOut)
        s.measureData = dataOut
        
    def randomizePoints(s):
        randomPointMatrix = np.random.randint(s.min,s.max,(4,3))
        return randomPointMatrix
    
    def calculateNodeWinner(s, kmeansMatrix):
        distance = np.zeros(s.kMeansCount)
        countWinner = np.zeros(s.kMeansCount)
        
        for riviDatassa in range(len(s.measureData)):
            for point in range(len(kmeansMatrix)):
                distance[point] = np.abs(np.sqrt(np.power((s.measureData[riviDatassa,0] - kmeansMatrix[point,0]),2) 
                                                     + np.power((s.measureData[riviDatassa,1] - kmeansMatrix[point,1]),2)
                                                     + np.power((s.measureData[riviDatassa,2] - kmeansMatrix[point,2]),2)))   
            index = np.argmin(distance)
            countWinner[index] += 1
        return countWinner
        
        
    def calculateAverage(s,input):
        output = np.zeros((s.kMeansCount,4))
        ic(input)
        
                
    def dataShow(s):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(s.measureData[:,0], s.measureData[:,1], s.measureData[:,2])
        # ax.scatter(s.outputMatrix[:,0], s.outputMatrix[:,1], s.outputMatrix[:,2], color="red", marker="*")
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()   
            
if __name__ == "__main__":
    kMeans = kMeans()
    kMeans.loadData("python\putty.log")
    while True:
        countWinner = kMeans.calculateNodeWinner(kMeans.randomizePoints())
        ic(countWinner)
        if not np.min(countWinner) == 0:
            break
    kMeans.calculateAverage(countWinner)
    
    
    # kMeans.dataShow()                    