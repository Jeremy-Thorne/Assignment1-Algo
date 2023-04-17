import subprocess
import random

dataList = []
path = "C:/Users/Jeremy/Documents/Assignment1-Algo/Assignment1-Algo/"
sizeList = [100,250,500,1000,2500,5000,10000,25000,50000,100000]
densityList = [0.05, 0.5, 0.95]
timesList = []
typeList = ["array"]

def createFiles():
    for density in densityList:
        for size in sizeList:
            f = open('C:/Users/Jeremy/Documents/Assignment1-Algo/Assignment1-Algo/Data/'+ str(size) + "-" + str(density) + '.txt', 'w')
            for i in range(size):
                num = round(random.random(), 2)
                if num > density:                        
                    pass
                else:
                    string = str(int(random.random() * size)) + " " + str(int(random.random() * 10)) + " " + str(round(random.random(), 2)) + "\n"
                    f.write(string)
            f.close()
def runTest():
    try:
        stdout = subprocess.run(["python", path + "spreadsheetFilebasedTesting.py", 
                            "array", path + str(250) + ".txt", 
                            path + "sampleCommands.in", 
                            path + "sample.out"], 
                            check=True, capture_output=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
    print(stdout)

if __name__ == '__main__':
    # createFiles()
    # runTest()
    # exit()
    for l in range(len(typeList)):
        for k in range(len(densityList)):
            timesList.append("\n" + 'array - density -'+ str(densityList[k]) + ":")
            for i in range(len(sizeList)):
                total = 0
                count = 0
                dataString = path + "Data/" + str(str(sizeList[i])) + "-" + str(densityList[k]) + '.txt'
                print(sizeList[i], end=" ")
                for j in range(5):
                    try:
                        stdout = subprocess.run(["python", path + "spreadsheetFilebasedTesting.py", 
                                            typeList[l], dataString, 
                                            path + "sampleCommands.in", 
                                            path + "sample.out"], 
                                            check=True, capture_output=True, text=True).stdout
                    except subprocess.CalledProcessError as e:
                        raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
                    try:           
                        total += float(stdout)
                    except:
                        print(stdout)
                        exit()
                    count += 1
                avg = round(total / count, 4)
                timesList.append("Time taken for data size - " + str(sizeList[i]) + ": " + str(avg))
            print()

        with open(path + 'time.txt', 'w') as f:
            for time in timesList:
                f.write(time + "\n")
            f.close()


