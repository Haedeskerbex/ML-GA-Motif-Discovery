import numpy as np
from Bio import SeqIO
import os
import pickle

# Input and output paths
INPUT_FASTA = "../data/ACE2/clean_reduced_ACE2.fasta"
OUTPUT_FEATURES = "onehot_features.pkl"

# Define amino acid vocabulary
AMINO_ACIDS = "ACDEFGHIKLMNPQRSTVWY"  # 20 standard amino acids
AA_TO_INDEX = {aa: i for i, aa in enumerate(AMINO_ACIDS)}

# Function to one-hot encode a sequence
def one_hot_encode(seq, max_length):
    encoded = np.zeros((max_length, len(AMINO_ACIDS)), dtype=np.float32)
    for i, aa in enumerate(seq):
        if aa in AA_TO_INDEX:
            encoded[i, AA_TO_INDEX[aa]] = 1
    return encoded

# Main feature extraction function
def extract_features(input_fasta, output_file):
    sequences = [str(record.seq) for record in SeqIO.parse(input_fasta, "fasta")]
    max_length = max(len(seq) for seq in sequences)  # Pad to longest sequence

    features = np.array([one_hot_encode(seq, max_length) for seq in sequences])

    # Save features
    with open(output_file, "wb") as f:
        pickle.dump(features, f)

    print(f"✅ Extracted features saved to {output_file} | Shape: {features.shape}")

if __name__ == "__main__":
    if not os.path.exists(INPUT_FASTA):
        print(f"❌ ERROR: {INPUT_FASTA} not found!")
    else:
        extract_features(INPUT_FASTA, OUTPUT_FEATURES)

