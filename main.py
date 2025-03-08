#Counts the number of nucleotide
def freq_nucleotide(seq):
    '''Counts the number of nucleotide'''

    #converting the sequence to uppercase
    seq = seq.upper()

    #relplacing gaps and newlines
    seq = seq.replace(" ", "").replace("\n", "").replace("\r", "")

    #counting number of nucleotides
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')

    return a_count, t_count, g_count, c_count

def gc_per(seq):
    seq = seq.upper()
    g_count = seq.count('G')
    c_count = seq.count('C')
    total = len(seq)
    percent = round(((g_count + c_count) / total) * 100, 2)
    return percent
