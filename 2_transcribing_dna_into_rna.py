dna = "TTAGCCCGGGCAGATCTTAGGAGGCGTTTAGTGGATTGCGCAGGGCCATTCGCCGTGTTAGAAATTTAGGTCGCGTTGTACAAAAGCTCAACGTATTCCTACTTCGTCGGCAGGTTAGTGACAGTACCTATACTCTCACTACTGCTCCGCGCGCTGAATCTCAACGCGAATCCAACCCTCAACATAAGACAGCGACTCCGTTGTGGGTTGGATGAAGCGGGCGTTTTATGCGGGGGATCCTGACGAGCCTGCCCGAAGAAGGGCCCTCAGTAGCCCACATTAGATCCTAAGTTCGATGAATAAAGTCTTCGTATTCCGAATTTGGTCCAGCAGCAGTCATGTAAGCCGAGGGGACAAAAATAGGAATTACAGTCGCAGGATTCCATTTATGGGTTCCTTTCACGAACTGGGACCCACGGTCATCCTATTAGCATATCAAATAGTCTGACGATTTAATGAGACAAAGGAACTCTTTATGGGCAACGTGCAGACTAGGGAGGTGCGTCAGAATGAACGCGGATCTTAAGGGACGACTTTTCGGGGTTAAGGCGCAGGTCTAGGAACTGGAGTCTACTTGCCCGACATGCGGACGGTCCGAGCGTACGGTCGGGACAGACAGAAATGTCCGCTGCAGTCCCGCTCCCAAATGGTCGTGGAGAAAGCAGCACTGTGTTACCGAGGGGACGAGATTTTAATTTGTAAAGGACTACTACGGCCGCCCGCATACTCCAGTTGCGCAAGTTAGCATGCAAGCTCGCGAGTAAACGTTGTATACCCGAATGTGTAGTGCCTGCTAAGCCTCATTGCTCTCCTAGTGGCACAAATGGCGTTCTGTTGTACTGGTCAAGGCGGGTGTGTCATCTTAATATCGGGGCTTCCGCGCTTCTACGGCAGATCGATTTTATAGTCACCCAGG"

# My original solution:
# dna = list(dna)
# rna = ["U" if nucleotide == "T" else nucleotide for nucleotide in dna]
# rna = "".join(rna)
# print(rna)

# Better solution:
print(dna.replace("T", "U"))