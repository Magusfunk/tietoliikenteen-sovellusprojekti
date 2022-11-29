import numpy as np
import matplotlib.pyplot as plt
class dataHandler:
    def __init__(s,file):
        s.file = file
        s.__data = ""
        s.loadData()
        
    def loadData(s):
        s.data = np.loadtxt(s.file)
        print(s.data)
        s.handleData()
        
    def handleData(s): 
        numberOfRows = int(len(s.data) / 3)       
        dataMatrix = np.zeros((numberOfRows,3))  
        dataMatrix[:,0] = s.data[0::3]
        dataMatrix[:,1] = s.data[1::3]
        dataMatrix[:,2] = s.data[2::3]
        return dataMatrix
        
    def dataShow(s):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(s.dataX, s.dataY, s.dataZ)
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()        
class kMeans:
    def __init__(s,data):
        s.data = data
        s.min = np.min(data)
        s.max = np.max(data)
        s.nodeMatrix = np.zeros((4,3))
    def randomNode(s):
        s.nodeMatrix = np.random.randint(s.min,s.max,(4,3))
        print("Node matrix len",len(s.nodeMatrix))
        
    def vectorLength(s):
        distance = np.zeros()
        for x in range(len(s.data)):
            print("Rivi :", x)
            for y in range(len(s.nodeMatrix)):
                print("Node :", y)  
                distance = np.abs(np.sqrt(np.power((s.data[x,0] - s.nodeMatrix[y,0]),2) + np.power((s.data[x,1] - s.nodeMatrix[y,1]),2) + np.power((s.data[x,2] - s.nodeMatrix[y,2]),2)))
                print(distance)
            
                
if __name__ == "__main__":
    df = dataHandler("python\putty.log")
    kMeans = kMeans(df.handleData())
    kMeans.randomNode()
    kMeans.vectorLength()