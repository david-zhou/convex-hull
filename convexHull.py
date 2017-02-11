import random
import math, time
import matplotlib.pyplot as plt

numPoints = 100
maxCoord = 10000

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

def initializePoints(numPoints):
    pointList = []
    for i in range(numPoints):
        x = random.uniform(-maxCoord, maxCoord)
        y = random.uniform(-maxCoord, maxCoord)
        p = Point(x,y)
        pointList.append(p)
    return pointList

def addPoints(points):
    x = [p.x for p in points]
    y = [p.y for p in points]
    plt.plot(x, y, 'ko')
    plt.axis([-maxCoord*1.2, maxCoord*1.2, -maxCoord*1.2, maxCoord*1.2])
    
def addLines(points):
    l = len(points)
    for i in range(l - 1):
        plt.plot([points[i].x, points[i+1].x], [points[i].y, points[i+1].y], color='r', linestyle='-', linewidth=1)
    
    plt.plot([points[l - 1].x, points[0].x], [points[l - 1].y, points[0].y], color='r', linestyle='-', linewidth=1)
    
    for p in points:
        #note = "({0:.1f}".format(p.x) + ", {0:.1f})".format(p.y)
        #plt.annotate(note, xy = (p.x, p.y), textcoords = 'data', color = 'b')
        plt.plot(p.x, p.y, 'ro')

def turn(points, n):
    p1 = points[n-2]
    p2 = points[n-1]
    p3 = points[n]
    return (p2.x - p1.x)*(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x)

def convexUpper(pointList):
    solutionUpper = []
    solutionUpper.append(pointList[0])
    solutionUpper.append(pointList[1])
    n = 2
    
    for i in range(2, numPoints):
        solutionUpper.append(pointList[i])
        n += 1
        while n > 2 and turn(solutionUpper, n - 1) >= 0:
            solutionUpper.pop(n-2)
            n -= 1
    return solutionUpper

def convexLower(pointList):
    l = len(pointList)
    solutionLower = []
    solutionLower.append(pointList[l - 1])
    solutionLower.append(pointList[l - 2])
    n = 2
    
    for i in range(l - 2, -1, -1):
        solutionLower.append(pointList[i])
        n += 1
        while n > 2 and turn(solutionLower, n - 1) >= 0:
            solutionLower.pop(n-2)
            n -= 1
    return solutionLower

def convexHull(pointList):
    pointList.sort(key=lambda x: (x.x, x.y))
    
    solutionUpper = convexUpper(pointList)
    solutionLower = convexLower(pointList)
    
    solutionUpper.pop()
    solutionLower.pop()
    
    return solutionUpper+solutionLower

pointList = initializePoints(numPoints)
addPoints(pointList)
plt.show()

startTime = time.time()

solution = convexHull(pointList)

endTime = time.time()
finalTime = endTime - startTime
print("Tiempo total: {}".format(finalTime))

addPoints(pointList)
addLines(solution)
plt.show()