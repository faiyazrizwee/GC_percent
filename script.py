#Counts the number of nucleotide
def freq_nucleotide(seq):
    '''Counts the number of nucleotide'''

    #converting the sequence to uppercase
    seq = seq.upper()

    #relplacing gaps and newlines
    seq = seq.replace(" ", "").replace("\n", "").replace("\r", "")

    #counting number of nucleotides
    print(f'Count A = {seq.count('A')}')
    print(f'Count T = {seq.count('T')}')
    print(f'Count G = {seq.count('G')}')
    print(f'Count C = {seq.count('C')}')


def gc_per(seq):
    ''''GC percent'''
    #converting the sequence to uppercase
    seq = seq.upper()

    #counting Guanine and Cytosine
    g_count = seq.count('G')
    c_count = seq.count('C')

    #Total sequence
    total = len(seq)

    #Calculating GC percent
    percent = round(((g_count + c_count) / total) * 100, 2)
    return percent

# for example take a sequence

seq = 'atgccgatgatcgctaggagctcgctaggctgacgcgctag'

freq_nucleotide(seq)

print(f'GC percent of given sequence is : {gc_per(seq)}')