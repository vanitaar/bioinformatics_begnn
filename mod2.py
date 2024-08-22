
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i+(n//2)], symbol)
    return array

# http://bioinformaticsalgorithms.com/data/testdatasets/week2/01%20-%20SymbolArray.txt
print(SymbolArray("AAAAGGGG", "A"))
# Output should be {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}

