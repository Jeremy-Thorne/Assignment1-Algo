import random
random.seed(10)

with open(r'C:\Users\Jeremy\Documents\Assignment1-Algo\Assignment1-Algo\testData.txt', 'w') as f:
    for i in range(50000):
        for j in range(10):
            string = str(i) + " " + str(j) + " " + str(round(random.random(), 2)) + "\n"
            f.write(string)