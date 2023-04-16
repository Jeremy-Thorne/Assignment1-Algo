import random
random.seed(10)

with open(r'C:\Users\Jeremy\Documents\Assignment1-Algo\Assignment1-Algo\small-100.txt', 'w') as f:
    for i in range(100):
        for j in range(10):
            # num = round(random.random(), 2)
            # if num > 0.4: 
            #     pass
            # else:
            #     string = str(i) + " " + str(j) + " " + str(round(random.random(), 2)) + "\n"
            #     f.write(string)
            string = str(i) + " " + str(j) + " " + str(round(random.random(), 2)) + "\n"
            f.write(string)