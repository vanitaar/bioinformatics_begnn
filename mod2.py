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

# Try on E. coli genome

# Fetch genome data
url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt"
with req.urlopen(url) as response:
    ecoli_genome = response.read().decode('utf-8').strip()  # remove any leading/trailing whitespace

# Pass the genome to the SymbolArray function
result = SymbolArray(ecoli_genome, "C")

print(result) #very slow for long genome   
print(ecoli_genome)
