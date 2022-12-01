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
        output = np.zeros((s.kMeansCount,4))        
        for riviDatassa in range(len(s.measureData)):
            for point in range(len(kmeansMatrix)):
                distance[point] = np.abs(np.sqrt(np.power((s.measureData[riviDatassa,0] - kmeansMatrix[point,0]),2) 
                                               + np.power((s.measureData[riviDatassa,1] - kmeansMatrix[point,1]),2)
                                               + np.power((s.measureData[riviDatassa,2] - kmeansMatrix[point,2]),2)))   
            index = np.argmin(distance)
            output[index,3] += 1
            output[index,0:3] += s.measureData[riviDatassa]
        return output
        
        
    def calculateAverage(s,input):
        output = np.zeros((s.kMeansCount,4))
        for rivi in range(len(input)):
            output[rivi,0:3] = input[rivi,0:3] / input[rivi,3]
        return output   
                
    def dataShow(s,input):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(s.measureData[:,0], s.measureData[:,1], s.measureData[:,2])
        ax.scatter(input[:,0], input[:,1], input[:,2], color="red", marker="*")
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()   
            
if __name__ == "__main__":
    kMeans = kMeans()
    kMeans.loadData("python\putty.log")   
    
    #Arvotaan ensimmäiset pisteen randomilla 
    while True:
        winner = kMeans.calculateNodeWinner(kMeans.randomizePoints())
        if not np.min(winner[:,3]) == 0:
            print("Luuppi katkaistu")
            break
    oldCenterPoints = kMeans.calculateAverage(winner)
            
    for i in range(10):        
        batchWinner = kMeans.calculateNodeWinner(oldCenterPoints)
        newCenterPoints = kMeans.calculateAverage(batchWinner)
        ic(np.average(oldCenterPoints[:,0:3] - newCenterPoints[:,0:3]))
        if np.average(oldCenterPoints[:,0:3] - newCenterPoints[:,0:3]) == 0:
            break
        oldCenterPoints = newCenterPoints   
        
    kMeans.dataShow(newCenterPoints)                    