import urllib.request as req

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

"""
# Try on E. coli genome

# Fetch genome data
url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
with req.urlopen(url) as response:
    ecoli_genome = response.read().decode('utf-8').strip()  # remove any leading/trailing whitespace

# Pass the genome to the SymbolArray function
result = SymbolArray(ecoli_genome, "C")

# print(result) #very slow for long genome   
# print(ecoli_genome)
"""


## SymbolArray --> inefficient algorithm
"""
Why is SymbolArray inefficient? Its for loop makes n = len(Genome) iterations. 
Then, to compute PatternCount(symbol, ExtendedGenome[i:i+(n//2)]), 
we must compare symbol against n//2 symbols of ExtendedGenome. 
As a result, we require a total of n2//2 comparisons to execute SymbolArray(Genome, symbol). 
For a bacterial genome such as E. coli, which contains over 4.5 million nucleotides, 
we will need to execute over ten trillion symbol comparisons in order to generate a symbol array, 
which could take several days on a fast home computer operating several million comparisons per second
"""


def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# http://bioinformaticsalgorithms.com/data/testdatasets/week2/02%20-%20FasterSymbolArray.txt
print(FasterSymbolArray("AAAAGGGG", "A"))

# Fetch genome data
url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
with req.urlopen(url) as response:
    ecoli_genome = response.read().decode('utf-8').strip()  # remove any leading/trailing whitespace
    
# print(FasterSymbolArray(ecoli_genome, "C")) # it worked ! albeit it is a very loong result

faster_result = FasterSymbolArray(ecoli_genome, "C")
key_count = len(list(faster_result.keys()))
print(key_count) # 4639675

print(len(faster_result)) # 4639675
