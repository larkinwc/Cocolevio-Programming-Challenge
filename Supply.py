#use this to load the input file
def loadData(filename):
    file_in = open(filename, 'r')
    data = []
    for line in file_in:
        #added rstrip to get rid of newline character
        data.append(line.rstrip().split(','))

    #convert our string values to int, besides first row
    for i in range(1, len(data)):    
        data[i] = list(map(int, data[i]))
        
    file_in.close()
    return data

#use this to determine who to sell to
def computeData(supply):
    data = loadData("input.csv")
    results = []
    #make multidemensional list
    results.append([])
    results.append([])
    results.append([])

    while supply > 0:
        #if we don't have enough merchants
        if(len(data[2]) == 0):
            return False
        
        highPrice = data[2].index(max(data[2]))
        supply -= int(data[1][highPrice])
        results[0].append(data[0].pop(highPrice))
        results[1].append(data[1].pop(highPrice))
        results[2].append(data[2].pop(highPrice))
    
    #incase the last business can only take a portion of what we have
    results[1][-1] = results[1][-1] + supply
    return results

def main():

    supply = int(input("Please input supply quantity: "))
    print()

    result = computeData(supply)
    if(result):
        sum = 0
        for i in range(len(result[2])):
            print("We can sell %i objects to company %s at $%i each for a total of $%i" %(result[1][i], result[0][i], result[2][i], result[1][i] * result[2][i]))
            sum += result[1][i] * result[2][i]
        print()
        print("Overall we made $%i" % (sum))
    else:
        print("We can sell to everyone!, because we have more than enough supply")

main()