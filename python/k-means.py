import numpy as np
import matplotlib.pyplot as plt
from icecream import ic
from pandas import read_csv

class kMeans:
    def __init__(s,kMeans):
        s.kMeansCount = kMeans               

    def loadData(s,file):
        rawData = np.genfromtxt(file,delimiter=",")
        rawData = rawData[:,5:8]
        s.min,s.max = np.min(rawData),np.max(rawData)
        # s.numberOfRows = 10000                                      #Randomdata input
        # rawData = np.random.randint(s.min,s.max,(s.numberOfRows,3)) #Randomdata input
        s.numberOfRows = len(rawData) 
        ic(rawData)
        s.measureData = rawData                                        
        return s.numberOfRows
        
    def randomizePoints(s):
        randomPointMatrix = np.random.randint(s.min,s.max,(s.kMeansCount,3))
        return randomPointMatrix
    
    def calculateNodeWinner(s, kmeansMatrix):
        #Distanceen lasketaan mittausdatan pisteiden etäisyys kMeans pisteisiin
        #Output matriisin jokainen rivi vastaa yhtä pistettä ja sarakkeille 1-3 lasketaan summa voitettujen pisteiden koordinaateista ja sarakkeelle 4 lasketaan
        # voittojen määrä
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
        #Täällä lasketaan uusi keskipiste syötetystä datasta eli jaetaan sarakkeiden 1-3 arvot sarakkeen 4 arvolla
        output = np.zeros((s.kMeansCount,4))
        for rivi in range(len(input)):
            output[rivi,0:3] = input[rivi,0:3] / input[rivi,3]
        return output   
                
    def dataShow(s,input):
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(s.measureData[:,0], s.measureData[:,1], s.measureData[:,2])
        ax.scatter(input[:,0,0], input[:,1,0], input[:,2,0], color="red", marker="*")
        ax.scatter(input[:,0,-1], input[:,1,-1], input[:,2,-1], color="green", marker="*")
        for node in range(len(input)):
            ax.plot(input[node,0,:], input[node,1,:], input[node,2,:], color="black")
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.show()   
            
if __name__ == "__main__":
    kMeanCount = 6
    tarkkuus = 0.02
    kMeans = kMeans(kMeanCount)
    rows = kMeans.loadData("python\export.csv")
    #Arvotaan ensimmäiset pisteen randomilla niin kauan, että kaikki saavat pisteet tasaisesti
    randomCount = 0
    while True:
        randomCount += 1
        ic(randomCount)
        winner = kMeans.calculateNodeWinner(kMeans.randomizePoints())
        if np.min(winner[:,3]) > (rows / kMeanCount) * 0.1:
            print("Luuppi katkaistu")
            break
    oldCenterPoints = kMeans.calculateAverage(winner)    
    visualizationMatriz = oldCenterPoints[:,0:3,np.newaxis]    
        
    #Pyöräytetään laskenta uudestaan läpi 10 kertaa tai niin kauan, että keskipisteiden arvo ei enää muutu
    #Käyttäen aina syötteenä vanhaa keskipistettä ja tuloksena saada uudet keskipisteet        
    for batch in range(rows): 
        batchWinner = kMeans.calculateNodeWinner(oldCenterPoints)
        newCenterPoints = kMeans.calculateAverage(batchWinner)
        ic(batch,np.abs(np.average(oldCenterPoints[:,0:3] - newCenterPoints[:,0:3])))
        if np.abs(np.average(oldCenterPoints[:,0:3] - newCenterPoints[:,0:3])) < tarkkuus:
            break
        visualizationMatriz = np.append(visualizationMatriz,newCenterPoints[:,0:3].reshape(kMeanCount,3,1),axis=2) 
        oldCenterPoints = newCenterPoints  
    ic(kMeans.calculateNodeWinner(oldCenterPoints))
    ic(visualizationMatriz[:,:,-1])
    
    kMeans.dataShow(visualizationMatriz)          