import numpy as np
import matplotlib.pyplot as plt
class kMeans:
    def __init__(s,file):
        s.data = ""
        s.min = 0
        s.max = 0        
        s.inputMatrix = np.zeros((4,4))
        s.outputMatrix = np.zeros((4,4))
        s.handleData(file)
               
    def handleData(s,file):
        s.data = np.loadtxt(file)
        s.numberOfRows = int(len(s.data) / 3) 
        dataMatrix = np.zeros((s.numberOfRows,3))
        s.kMeansCount = 4 
        s.dataX = s.data[0::3]
        s.dataY = s.data[1::3]
        s.dataZ = s.data[2::3] 
        dataMatrix[:,0] = s.data[0::3]
        dataMatrix[:,1] = s.data[1::3]
        dataMatrix[:,2] = s.data[2::3]
        s.min = np.min(s.data)
        s.max = np.max(s.data)
        s.measureData = dataMatrix

    def randomNode(s):
        randomMatrix = np.random.randint(s.min,s.max,(4,3))
        return randomMatrix
        
    def kMeans(s):
        
        avg = s.vectorLenghtCalculate()
        s.outputMatrix = avg
            
    def vectorLenghtCalculate(s):            
        avg = np.zeros((s.kMeansCount,4))
        distance = np.zeros(s.kMeansCount)
        s.inputMatrix = s.randomNode()
        while True:
            for x in range(len(s.measureData)):
                # print("Rivi :", x)
                for y in range(len(s.inputMatrix)):
                    # print("Node :", y)  
                    distance[y] = np.abs(np.sqrt(np.power((s.measureData[x,0] - s.inputMatrix[y,0]),2)+ np.power((s.measureData[x,1] - s.inputMatrix[y,1]),2) + np.power((s.measureData[x,2] - s.inputMatrix[y,2]),2)))
                i = np.argmin(distance)
                avg[i,3] += 1
                avg[i,0:3] += s.measureData[x,0:3]
            print(avg)
            if np.min(avg[:,3] == 0.0):
                print("Arvottu uusi")
                s.inputMatrix = s.randomNode()
            if not np.min(avg[:,3] == 0.0):
                print(np.min(avg[:,3]))
                print("Looppi katkaistu")
                break        
        for i in range(len(avg)):
            for j in range(4):
                avg[i] = avg[i,:] / avg[i,3] 
        return avg
    
    def dataShow(s):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(s.measureData[:,0], s.measureData[:,1], s.measureData[:,2])
        ax.scatter(s.outputMatrix[:,0], s.outputMatrix[:,1], s.outputMatrix[:,2], color="red", marker="*")
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()   
                
if __name__ == "__main__":
    kMeans = kMeans("python\putty.log")
    kMeans.kMeans()
    kMeans.dataShow()