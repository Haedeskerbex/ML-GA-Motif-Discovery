from Bio import SeqIO

input_file = "../data/ACE2/reduced_ACE2.fasta"
output_file = "../data/ACE2/clean_reduced_ACE2.fasta"

with open(output_file, "w") as out_f:
    for record in SeqIO.parse(input_file, "fasta"):
        record.seq = record.seq.replace("-","")  # Remove gaps
        SeqIO.write(record, out_f, "fasta")

print("Cleaned FASTA saved as", output_file)
