""" INSTRUCTIONS
2.1. Refer back to exercise 1.4, where we printed a DNA string in blocks, with a space between each block. Now further develop your code so that it displays a DNA string in the style used in GenBank records. 

So given the DNA sequence: 

GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGC CTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAA GAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGG AACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAA AGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTT AGTCAACTTGTTGAAGAGCTATTGAAAATCATTTGTGCTTTTCAGCTTGACACAGGTTTGGAGTATGCAA ACAGCTATAATTTTGCAAAAAAGGAAAATAACTCTCCTGAACATCTAAAAGATGAAGTTTCTATCATCCA AAGTATGGGCTACAGAAACCGTGCCAAAAGACTTCTACAGAGTGAACCCGAAAATCCTTCCTTGCAGGAA ACCAGTCTCAGTGTCCAACTCTCTAACCTTGGAACTGTGAGAACTCTGAGGACAAAGCAGCGGATACAAC CTCAAAAGACGTCTGTCTACATTGAATTGGGATCTGATTCTTCTGAAGATACCGTTAATAAGGCAACTTA TTGCAGTGTGGGAGATCAAG 

The output should be in columns with the row number at the start

Hint: it’s a good idea to make your code into a function which has parameters for the block size and number of blocks per row, as well as the string to print. Also, see if you can ensure that the bases are always in lower case when printed regardless of the input.
"""
# load the logging tools
import logging
logging.basicConfig(filename="logs/genebank_style.log", level=logging.INFO, )

#main body of code 
def dna_genebank(sequence:str, blocks: int, gap: int):
    logging.info("dna_genebank function called")
    count = 0 
    new_sequence = ""
    sequence_lower = sequence.lower()
    nucleotide_bases = "atcg"
    length = str(len(sequence))
    indent = int(len(length)) + 1

    if not isinstance(sequence, str):
        logging.error("Sequence must be a string")
        raise TypeError("Sequence must be a string")
    
    if not isinstance(blocks, int) and blocks > 0:
        logging.error("Blocks must be an integer greater or equal to zero")
        raise ValueError("Blocks must be an integer greater or equal to zero")
    
    if not isinstance(gap, int) and blocks > 0:
        logging.error("Gap must be an integer greater or equal to zero")
        raise ValueError("Gap must be an integer greater or equal to zero")
    
    for position, nucleotide in enumerate(sequence_lower):
        if nucleotide in nucleotide_bases:
            count += 1

            if count == 1:
                new_sequence += f"{count:> {indent}} "
            
            new_sequence += nucleotide

            if count % gap == 0:
                new_sequence += " "

            if count % (gap * blocks) == 0 and count < len(sequence):
                new_sequence += f"\n{count:>{indent}} "

        else:
            logging.warning(f"Invalid base at position: {position + 1} ('{nucleotide}')")

    logging.info("dna_genebank function complete")
    return new_sequence

#testing the function
if __name__=="__main__":
    sequence = "GCGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    print(dna_genebank(sequence, 5, 10))