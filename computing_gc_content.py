import re

# Return a dictionary with identifier: sequence pairs
def import_fasta_from_file(path:str) -> dict:
    f = open(path, 'r')
    dna_seq = []
    for line in f:
        line = line.rstrip()
        dna_seq.append(line)

    dna_seq = ''.join(dna_seq)
    dna_seq1 = re.split('>Rosalind_\d*', dna_seq)[1:]
    identifiers = re.findall(r'Rosalind_\d*', dna_seq)

    id_seq_dict = dict(zip(identifiers, dna_seq1))
    return id_seq_dict

# Return GC-content in %
def gc_content(sequence:str) -> float:
    gc_count = re.findall('[GgCc]', sequence)
    return(float(len(gc_count)*100/len(sequence)))

my_new_dict = import_fasta_from_file("<Enter the path of your pseudo-rosalind-fasta file here.>")

for item in my_new_dict:
    my_new_dict[item] = gc_content(my_new_dict[item])

list_a = list(my_new_dict.keys())
list_b = list(my_new_dict.values())
max_gc = max(list_b)
max_gc_index = list_b.index(max_gc)

print(f'{list_a[max_gc_index]}\n{max_gc}')