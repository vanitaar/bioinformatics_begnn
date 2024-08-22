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
# print(FasterSymbolArray("AAAAGGGG", "A"))

# Fetch genome data
url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
with req.urlopen(url) as response:
    ecoli_genome = response.read().decode('utf-8').strip()  # remove any leading/trailing whitespace
    
# print(FasterSymbolArray(ecoli_genome, "C")) # it worked ! albeit it is a very loong result

faster_result = FasterSymbolArray(ecoli_genome, "C")
key_count = len(list(faster_result.keys()))
print(key_count) # 4639675

# print(len(faster_result)) # 4639675

def FasterSymbolArray2(Genome, symbol):
    array = {}
    n = len(Genome)
    half_n = n // 2
    ExtendedGenome = Genome + Genome[:half_n]

    # Initialize array with zeros
    current_count = sum(1 for i in range(half_n) if ExtendedGenome[i] == symbol)

    for i in range(n):
        array[i] = current_count
        if ExtendedGenome[i] == symbol:
            current_count -= 1
        if ExtendedGenome[i + half_n] == symbol:
            current_count += 1

    return array


# print(FasterSymbolArray2("AAAAGGGG", "A"))


# Skew Array

def ComputeSkewArray(Genome):
    Skew = [0]  # Initialize the skew array with Skew[0] = 0
# note: Skew[-1] --> in ref to the last element of array
# no need to explicitly keep track of index separately    
    for nuc in Genome:
        if nuc == "G":
            Skew.append(Skew[-1] + 1)
        elif nuc == "C":
            Skew.append(Skew[-1] - 1)
        # nuc == "A" or "T" --> will append last value
        else:
            Skew.append(Skew[-1])
    return Skew

example_genome = "CATGGGCATCGGCCATACGCC"
skew_array = ComputeSkewArray(example_genome)
print(skew_array) # [0, -1, -1, -1, 0, 1, 2, 1, 1, 1, 0, 1, 2, 1, 0, 0, 0, 0, -1, 0, -1, -2]
print(" ".join(map(str, skew_array))) # 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2

example_genome2 = "GAGCCACCGCGATA"
skew_array2 = ComputeSkewArray(example_genome2)
print(skew_array2) # [0, 1, 1, 2, 1, 0, 0, -1, -2, -1, -2, -1, -1, -1, -1]
print(" ".join(map(str, skew_array2))) # 0 1 1 2 1 0 0 -1 -2 -1 -2 -1 -1 -1 -1

# optimized skew array fn
def SkewArray(Genome):
    skew = [0]  # Initialize skew with 0
    for i in Genome:
        skew.append(skew[-1] - 1 if i == 'C' else (skew[-1] + 1 if i == 'G' else skew[-1]))
    # return skew --> get in list
    return " ".join(map(str, skew))

print(SkewArray("CATGGGCATCGGCCATACGCC"))
print(SkewArray("GAGCCACCGCGATA"))

# Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum. --> indicative of approx position of ori
def MinimumSkew(Genome):
    # generate an empty list positions
    positions = []
    # set a variable equal to SkewArray(Genome)
    skew_arr = ComputeSkewArray(Genome)
    # find the minimum value of all values in the skew array
    min_value = min(skew_arr)
    # range over the length of the skew array and add all positions achieving the min to positions
    for i in range(len(skew_arr)): # alt : use enumerate?
        if skew_arr[i] == min_value:
            positions.append(i)
    
    return positions

# http://bioinformaticsalgorithms.com/data/testdatasets/week2/04%20-%20MinimumSkew.txt

print(MinimumSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")) # [11, 24]


# Hamming Distance Problem
"""
We say that position i in k-mers p and q is a mismatch 
if the symbols at position i of the two strings are not the same. 
The **TOTAL NUMBER OF MISMATCHES** between strings p and q is called the Hamming distance between these strings. 
Implement a function to compute this distance, called HammingDistance(p, q)
"""

def HammingDistance(p, q):
    hamming_dist = 0 # initialize
    if len(p) != len(q):
        return "Strings not of equal length"
    else:
        for i in range(len(p)):
            if p[i] != q[i]:
                hamming_dist += 1
        return hamming_dist
    
# http://bioinformaticsalgorithms.com/data/testdatasets/week2/05%20-%20HammingDistance.txt
print(HammingDistance("GGGCCGTTGGT", "GGACCGTTGAC"))  # 3

# using zip
    # for pi, qi in zip(p, q):
    #     if pi != qi:
    #         hamming_dist += 1

# Approximate Pattern Matching Problem
#  Input: Strings Pattern and Text along with an integer d.
#  Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
# Given PatternMatching in mod1.py, define an approximate pattern matching fn to 
# Find all approximate occurrences of a pattern in a string.
    
def ApproximatePatternMatching(Pattern, Text, d):
    positions = []  # Initialize list to hold positions
    k = len(Pattern)
    for i in range(len(Text) - k + 1):
        if HammingDistance(Pattern, Text[i:i+k]) <= d:
            positions.append(i)
    return positions

# http://bioinformaticsalgorithms.com/data/testdatasets/week2/06%20-%20ApproximatePatternMatching.txt

Pattern = "ATTCTGGA"
Text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3

print(ApproximatePatternMatching(Pattern, Text, d)) # [6, 7, 26, 27]

# using list comprehension
def ApproximatePatternMatching2(Pattern, Text, d):
    k = len(Pattern)
    return [i for i in range(len(Text) - k + 1) if HammingDistance(Pattern, Text[i:i+k]) <= d]

print(ApproximatePatternMatching2(Pattern, Text, d))