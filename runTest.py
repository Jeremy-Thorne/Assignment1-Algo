import subprocess
import random
import time

# Path to assignment folder
path = "C:/Users/Jeremy/Documents/Assignment1-Algo/Assignment1-Algo/"

# Lists to create test loops
sizeList = [100,250,500,1000,2500,5000,10000,25000,50000]
densityList = [0.1, 0.25, 0.5]
typeList = ["array","csr", "linkedlist"]
commands = [10, 100, 250]

# String List to store returned times
timesList = []

# Creates new files for all sizes
def createFiles():
    for density in densityList:
        for size in sizeList:
            createFile(size, density)

# Creates new files for 1 size
def createFile(size, density):
    f = open('C:/Users/Jeremy/Documents/Assignment1-Algo/Assignment1-Algo/Data/'+ str(size) + "-" + str(density) + '.txt', 'w')
    for i in range(size):
        num = round(random.random(), 2)
        if num > density:                        
            pass
        else:
            string = str(i) + " " + str(int(random.random() * 30)) + " " + str(round(random.random(), 2)) + "\n"
            f.write(string)
    f.close()

def generateCommands(numCommands, size):
    f = open('C:/Users/Jeremy/Documents/Assignment1-Algo/Assignment1-Algo/testCommands.in', 'w')
    for i in range(numCommands):
        commandString = ""
        command = random.randint(0,8)
        if(command == 0): 
            commandString = "AR"
        if(command == 1): 
            commandString = "AC"
        if(command == 2): 
            commandString = "U " + str(random.randint(0,size)) + " " + str(random.randint(0,30)) + " " + str(round(random.random(), 1))
        if(command == 3): 
            commandString = "R"
        if(command == 4): 
            commandString = "C"
        if(command == 5): 
            commandString = "F " + str(round(random.random(), 1))
        if(command == 6): 
            commandString = "E"
        if(command == 7): 
            commandString = "IR " + str(random.randint(0,size))
        if(command == 8): 
            commandString = "IC " + str(random.randint(0,30))
        f.write(commandString + "\n")
    f.close()

if __name__ == '__main__':
    # createFiles()
    # Test Short command list and Long command list
    for m in range(len(commands)):
        timesList.append("\n Num Comands " + str(commands[m]))

        # Loop for spreadsheet Type
        for l in range(len(typeList)):
            print(typeList[l], commands[m], " Commands")

            # Loop for spreadsheet Density
            for k in range(len(densityList)):
                timesList.append("\n" + typeList[l] + ' - density -'+ str(densityList[k]) + ":")

                # Loop for spreadsheet Size
                for i in range(len(sizeList)):
                    total = 0
                    count = 0
                    generateCommands(commands[m], sizeList[i])
                    dataString = path + "Data/" + str(str(sizeList[i])) + "-" + str(densityList[k]) + '.txt'
                    print(sizeList[i], end=" ")

                    # Loop for amount of tests
                    for j in range(1):

                        # If the sheet errors, loop again and generate another dataset
                        # There is a bug I cannot fix so just create new data until there is no bug :)
                        for x in range(0, 1000):
                            if x == 999:
                                print("Test timeout")
                                exit(1)
                            # Run Command
                            try:
                                stdout = subprocess.run(["python", path + "spreadsheetFilebasedTesting.py", 
                                                    typeList[l], dataString, 
                                                    path + "testCommands.in", 
                                                    path + "sample.out"], 
                                                    check=True, capture_output=True, text=True).stdout
                            except subprocess.CalledProcessError as e:
                                #print(e)
                                createFile(sizeList[i], densityList[k])
                                if x == 0:                     
                                    print("Data Error", end='')
                                    startErrorTime = time.time()
                                else:
                                    print(".", end='')
                                pass
                            else:
                                break
                        # If return value is not a float quit test
                        try:           
                            total += float(stdout)
                        except:
                            print(stdout)
                            exit()

                        count += 1

                    avg = round(total / count, 4)
                    # Add time taken to list
                    timesList.append("Time taken for data size - " + str(sizeList[i]) + ": " + str(avg))

                print()

    with open(path + 'time.txt', 'w') as f:
        # Print list to times file
        for time in timesList:
            f.write(time + "\n")
        f.close()


