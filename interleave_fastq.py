#!/usr/bin/env python3
import argparse
from Bio import SeqIO

def interleave_fastq(forward_file, reverse_file, output_file):
	#Open the two FASTQ files
	r1_reads = SeqIO.parse(forward_file, "fastq")
	r2_reads = SeqIO.parse(reverse_file, "fastq")

	#Interleave the sequences
	interleave = (read for pair in zip(r1_reads, r2_reads) for read in pair)
	
	#Save to the output file
	SeqIO.write(interleave, output_file, "fastq")
	

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Interleave Paired-End FASTQ Files')
	parser.add_argument('forward_file', help='Forward reads FASTQ file')
	parser.add_argument('reverse_file', help='Reverse reads FASTQ file')
	parser.add_argument('output_file', help='Output interleaved FASTQ file')
	args = parser.parse_args()
	interleave_fastq(args.forward_file, args.reverse_file, args.output_file)


