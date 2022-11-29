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
        s.dataX = s.data[0::3]
        s.dataY = s.data[1::3]
        s.dataZ = s.data[2::3] 
        dataMatrix[:,0] = s.data[0::3]
        dataMatrix[:,1] = s.data[1::3]
        dataMatrix[:,2] = s.data[2::3]
        return dataMatrix
        
    def dataShow(s,node):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(s.dataX, s.dataY, s.dataZ)
        ax.scatter(node[0], node[1], node[2], color="red", marker="*")
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()        
class kMeans:
    def __init__(s,data):
        s.measureData = data
        s.min = np.min(data)
        s.max = np.max(data)
        s.node = np.zeros((4,4))
    def randomNode(s):
        s.node = np.random.randint(s.min,s.max,(4,3))
        print("Nodet arvottu")
        
    def vectorLength(s):
        while(True):
            s.randomNode()
            distance = np.zeros(len(s.node))
            avg = np.zeros((len(s.node),4))
            for x in range(len(s.measureData)):
                # print("Rivi :", x)
                for y in range(len(s.node)):
                    # print("Node :", y)  
                    distance[y] = np.abs(np.sqrt(np.power((s.measureData[x,0] - s.node[y,0]),2)+ np.power((s.measureData[x,1] - s.node[y,1]),2) + np.power((s.measureData[x,2] - s.node[y,2]),2)))
                i = np.argmin(distance)
                avg[i,3] += 1
                avg[i,0:3] += s.measureData[x,0:3]
            if not np.min(avg[:,3]) == 0:
                break   
        for i in range(len(avg)):
            for j in range(4):
                avg[i] = avg[i,:] / avg[i,3] 
        s.node = avg
    def getValues(s):
        s.node = s.node[:,0:3]
        return s.node

            
                
if __name__ == "__main__":
    df = dataHandler("python\putty.log")
    kMeans = kMeans(df.handleData())
    kMeans.vectorLength()
    nodes = kMeans.getValues()
    df.dataShow(nodes)