# compare indices, if stringA[1] != stringB[1]: increment hamming_distance

dH_st = 0 # Hamming distance of s and t

# s = list("GAGCCTACTAACGGGAT") # first sequence
s = input("Enter first sequence: \n")
# t = list("CATCGTAATGACGGCCT") # second sequence
t = input("Enter second sequence: \n")

comparing_list = list(zip(s, t))
# print(comparing_list)
for item in comparing_list:
    if item[0] != item[1]:
        dH_st = dH_st + 1

print("The Hamming distance is: ", dH_st)