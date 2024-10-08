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

# using slice https://stackoverflow.com/questions/509211/how-slicing-in-python-works
def Reverse2(Pattern):
    return Pattern[::-1]

print(Reverse2('AAAACCCGGT')) # Output: "TGGCCCAAAA"

def Complement(Pattern):
    nucleotide_complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement = ""
    for nuc in Pattern:
        complement += nucleotide_complements[nuc]
    return complement

print(Complement("AAAACCCGGT")) # Output: "TTTTGGGCCA"

# using list comprehension to optimize
def Complement2(Pattern):
    nucleotide_complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
    complement = "".join(nucleotide_complements[nuc] for nuc in Pattern)
    return complement

print(Complement2("AAAACCCGGT")) # Output: "TTTTGGGCCA"

# putting it all together

def ReverseComplement(Pattern):
    Pattern = Reverse2(Pattern) # reverse all letters in a string
    Pattern = Complement2(Pattern) # complement each letter in a string
    return Pattern

print(ReverseComplement("AAAACCCGGT")) # Output: "ACCGGGTTTT"
# http://bioinformaticsalgorithms.com/data/testdatasets/week1/05%20-%20ReverseComplement.txt


# these are 4 most freq 9-mers in oriC of VC
# first 2 are rev complements of each other
print(ReverseComplement("ATGATCAAG")) # CTTGATCAT
print(ReverseComplement("CTTGATCAT")) # ATGATCAAG
print(ReverseComplement("TCTTGATCA")) # TGATCAAGA
print(ReverseComplement("CTCTTGATC")) # GATCAAGAG

# also recall importance of ATG in start code??

# taking ATGATCAAG as the DnaA box, we need to check for other occurrences of this string pattern
# there maybe these repeats occurring throughtout the VC genome, rather than just in the ori region

# the Pattern Matching Problem
#http://bioinformaticsalgorithms.com/data/testdatasets/week1/06%20-%20PatternMatching.txt

def PatternMatching(Pattern, Genome):
    positions = [] # to contain starting positions of where string patern matched
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
            
    return positions


# or using list comprehension
def PatternMatching2(Pattern, Genome):
    return [idx for idx in range(len(Genome) - len(Pattern) + 1) if Genome[idx:idx+len(Pattern)] == Pattern]

print(PatternMatching("ATAT", "GATATATGCATATACTT")) # [1, 3 , 9]
print(PatternMatching2("ATAT", "GATATATGCATATACTT")) # [1, 3 , 9]

# applying to Vibrio Cholera genome https://bioinformaticsalgorithms.com/data/realdatasets/Replication/Vibrio_cholerae.txt
# Pattern = "CTTGATCAT" --> positions = [60039, 98409, 129189, **152283, 152354, 152411**, 163207, 197028, 200160, 357976, 376771, 392723, 532935, 600085, 622755, 1065555]
# Pattern = "ATGATCAAG" --> [116556, 149355, **151913, 152013, 152394**, 186189, 194276, 200076, 224527,
#307692, 479770, 610980, 653338, 679985, 768828, 878903, 985368]

# ori region of Thermotoga petrophil
# https://bioinformaticsalgorithms.com/data/realdatasets/Replication/t_petrophila_oriC.txt

Text_T_Petrophil_ori = \
"AACTCTATACCTCCTTTTTGTCGAATTTGTGTGATTTATAGAGAAAATCTTATTAACTGAAACTAAAATGGTAGGTTTGGTGGTAGGTTTTGTGTACATTTTGTAGTATCTGATTTTTAATTACATACCGTATATTGTATTAAATTGACGAACAATTGCATGGAATTGAATATATGCAAAACAAACCTACCACCAAACTCTGTATTGACCATTTTAGGACAACTTCAGGGTGGTAGGTTTCTGAAGCTCTCATCAATAGACTATTTTAGTCTTTACAAACAATATTACCGTTCAGATTCAAGATTCTACAACGCTGTTTTAATGGGCGTTGCAGAAAACTTACCACCTAAAATCCAGTATCCAAGCCGATTTCAGAGAAACCTACCACTTACCTACCACTTACCTACCACCCGGGTGGTAAGTTGCAGACATTATTAAAAACCTCATCAGAAGCTTGTTCAAAAATTTCAATACTCGAAACCTACCACCTGCGTCCCCTATTATTTACTACTACTAATAATAGCAGTATAATTGATCTGA"

count_1 = PatternCount(Text_T_Petrophil_ori, "ATGATCAAG")
count_2 = PatternCount(Text_T_Petrophil_ori, "CTTGATCAT")

print(count_1) # 0
print(count_2) # 0
print(count_1 + count_2) # 0
# to confirm:
print(PatternMatching("ATGATCAAG", Text_T_Petrophil_ori)) # []

#This region does not contain a single occurrence of "ATGATCAAG" or "CTTGATCAT"! Thus, different bacteria may use different DnaA boxes as “hidden messages” to the DnaA protein.

print(FrequentWords(Text_T_Petrophil_ori, 9))
print(FrequencyMap(Text_T_Petrophil_ori, 9))


# Quiz 1
print(PatternCount("AAA", "GACCATCAAAACTGATAAACTACTTAAAAATCAGT")) # 0
print(PatternCount("GACCATCAAAACTGATAAACTACTTAAAAATCAGT", "AAA")) # 6
print(ReverseComplement("GCTAGCT")) # "AGCTAGC"
print(FrequentWords("CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT", 3)) #CCT

print(PatternCount("GACCATCAAAACTGATAAACTACTTAAAAATCAGT", "AAA")) # 6
print(FrequentWords("CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA", 3)) # AGG
print(ReverseComplement("TTGTGTC")) # GACACAA