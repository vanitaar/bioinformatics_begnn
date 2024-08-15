# datasets --> https://bioinformaticsalgorithms.com/data/testdatasets/week1/01%20-%20PatternCount.txt
    
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

print(PatternCount("GCGCG", "GCG"))