#use this to load the input file
def loadData(filename):
    file_in = open(filename, 'r')
    data = []
    for line in file_in:
        #added rstrip to get rid of newline character
        data.append(line.rstrip().split(','))
    return data

#use this to determine who to sell to
def computeData():
    data = loadData("input.csv")

    #compute results
    results = data
    
    return results

def main():
    
    result = computeData()
    print(result)

main()