""" INSTRUCTIONS
1.4 Given a string representing a DNA sequence, print it in blocks, i.e. with gaps every so many bases. 

So given sequence: 

	 aggagtaagcccttgcaactggaaatacacccattg 

an output with a block size of 3 should look like:
 
	agg agt aag ccc ttg caa ctg gaa ata cac cca ttg 

Challenge: output the following sequence with a block size of 10: 

GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT
"""
#set up logging
import logging 
logging.basicConfig(filename="logs/chunk_seq.log", level=logging.INFO, format="%(levelname)s:%(message)s")

#main body of text
def dna_blocks(sequence:str, gap: int):
    logging.info("dna_blocks function called")
    count = 0 
    nucleotide_bases = "ATCG"
    new_sequence = ""

    if not isinstance(sequence, str):
        logging.error("Sequence must be a string")
        raise TypeError("Sequence must be a string")

    if not isinstance(gap, int) or gap < 0:
        logging.error("gap must be a number >= 0")
        raise ValueError("gap must be a number >= 0")
    
    for position, nucleotide in enumerate(sequence):

        if nucleotide in nucleotide_bases:
            count += 1
            new_sequence += nucleotide

            if count % gap == 0:
                new_sequence += " "
            
        else:
            logging.warning(f"Invalid base at position: {position + 1} ('{nucleotide}')")

    logging.info("dna_blocks function completed")
    return new_sequence


#testing the function
if __name__=="__main__":
    sequence = "GCTGAGACTTCCTGGACGGGGGACAGGCTGTGGGGTTTCTCAGATAACTGGGCCCCTGCGCTCAGGAGGCCTTCACCCTCTGCTCTGGGTAAAGTTCATTGGAACAGAAAGAAATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTTAGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTTGCAAATTTTGCATGCTGAAACTTCTCAACCAGAAGAAAGGGCCTTCACAGTGTCCTTTATGTAAGAATGATATAACCAAAAGGAGCCTACAAGAAAGTACGAGATTTGAT"
    print(dna_blocks(sequence, 3))