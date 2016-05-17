#Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:

#* `G` -> `C`
#* `C` -> `G`
#* `T` -> `A`
#* `A` -> `U`

def to_rna(dna_string):
    rna_string = []
    for char in dna_string:
        if char =="G":
            rna_string.append('C')
        elif char == "C":
            rna_string.append('G')
        elif char == "T":
            rna_string.append('A')
        elif char == "A":
            rna_string.append('U')
        else:
            rna_string.append('')
    rna_string = "".join(rna_string)
    return rna_string