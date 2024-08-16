# datasets --> https://bioinformaticsalgorithms.com/data/testdatasets/week1/01%20-%20PatternCount.txt
    
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

print(PatternCount("GCGCG", "GCG")) # Output: 2

# oriC of Vibrio cholerae
Text = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"
Pattern = "TGATCA"

print(PatternCount(Text, Pattern)) # Output: 8

# when pattern not pre-defined: 
#range through every k-mer in a Text and assign every pattern a value of 0
# n = len(Text)
# for i in range(n-k+1):
#     Pattern = Text[i:i+k]
#     freq[Pattern] = 0

# function to GENERATE a frequency map using what learnt above
# initialized 0 
# def FrequencyMap(Text, k):
#     freq = {}
#     n = len(Text)
#     for i in range(n-k+1):
#         Pattern = Text[i:i+k]
#         freq[Pattern] = 0
#     return freq

# TO SOLVE THE FREQUENT WORDS PROBLEM

# completed FreqMap function:
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k] 
        freq[Pattern] = 0 #adding new key
    # add another for loop here to range over each k-mer Pattern of text and increase freq[Pattern] by 1 each time
    for i in range(n-k+1):
        Pattern = Text[i:i+k] #defining the variable
        freq[Pattern] += 1
    return freq

# The second loop is necessary to count the occurrences of each k-mer in the text. Here’s a step-by-step explanation:
# First Loop: This loop initializes the dictionary freq with all possible k-mers from the text, setting their counts to 0. It ensures that every k-mer is included in the dictionary, even if it doesn’t appear in the text.
# Second Loop: This loop actually counts the occurrences of each k-mer. It iterates over the text again, and for each k-mer, it increments its count in the freq dictionary.
# Without the second loop, the dictionary would only contain k-mers with a count of 0, as the first loop only initializes the dictionary but doesn’t count the occurrences.


# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
      # add each key to words whose corresponding frequency value is equal to m
        if freq[key] == m:
            words.append(key)
    return sorted(words)

# https://bioinformaticsalgorithms.com/data/testdatasets/week1/04%20-%20FrequentWordsNoDuplicates.txt

print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)) # Output: ['CATG', 'GCAT']

# Text in reference to previously defined oriC of Vibrio cholerae (line 13)
k = 3
print(FrequentWords(Text, k)) 
# Output: k=10 ['CTCTTGATCA', 'TCTTGATCAT']
# Output: k=3 ['TGA']

# TO SOLVE THE REVERSE COMPLEMENT PROBLEM: Find the reverse complement of a DNA string.
    #  Input: A DNA string Pattern.
    #  Output: The reverse complement of Pattern.
    
# "highest-level" function:
# def ReverseComplement(Pattern):
#     Pattern = Reverse(Pattern) # reverse all letters in a string
#     Pattern = Complement(Pattern) # complement each letter in a string
#     return Pattern

def Reverse(Pattern):
    rev = "" # initialize empty str
    # loop through pattern for len + 1 (as range 2nd arg is exclusive)
    for i in range(1, len(Pattern) + 1):
        rev += Pattern[-i] # 0 1 2 3 --> -1 -2 -3 -4 
    return rev

print(Reverse('AAAACCCGGT')) # Output: "TGGCCCAAAA"

