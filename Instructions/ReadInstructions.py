
def calculate_timestamp(str):
        timestampArr = str.split(":",3)
        hour = int (timestampArr[0])
        min = int(timestampArr[1])
        sec = float(timestampArr[2])
        timestamp = sec + min * 60 + hour * 60 * 60
        timestamp = round(timestamp,3)
        return timestamp

def read_file(file_name):
    f = open(file_name, "r")
    lines = f.readlines()
    f.close()

    instructions = []
    for i in range(len(lines)-1):
        
        lineArr = lines[i].split("	", 3)

        #calculate time stamp - 0:00:00.000
        timestamp = calculate_timestamp(lineArr[0])

        # number of bits
        print i
        bits = int(lineArr[1])

        #power W/M/S
        power = lineArr[2][:1]

        instructions.append([timestamp,bits,power])        

    #duration
    for i in range (0, len(lines)-2):
        duration = round(instructions[i+1][0]-instructions[i][0],3)
        instructions[i].append(duration)
    duration = round (calculate_timestamp(lines[len(lines)-1])-instructions[i][0], 3)
    instructions[len(lines)-2].append(duration)
  
    return instructions

instructions = read_file('Emily Browning - Sweet Dreams.txt')
print instructions
