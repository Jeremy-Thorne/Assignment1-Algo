def record(time): 
    with open(r'C:\Users\Jeremy\Documents\Assignment1-Algo\Assignment1-Algo\time.txt', 'r') as l:
            lines = l.readlines()
            total = float(lines[0])
            total += time
            count = int(lines[1])
            count += 1
            avg = float(total) / count
    if count == 3:
        print(round(avg, 4))
        with open(r'C:\Users\Jeremy\Documents\Assignment1-Algo\Assignment1-Algo\time.txt', 'w') as f:
            f.write(str(0) + "\n")
            f.write(str(0) + "\n")
            f.write(str(0))
    else:     
        with open(r'C:\Users\Jeremy\Documents\Assignment1-Algo\Assignment1-Algo\time.txt', 'w') as f:
            f.write(str(total) + "\n")
            f.write(str(count) + "\n")
            f.write(str(avg))
    print( count )
