# Mutation Predictor

This project is a real-world Mutation Predictor tool for coronaviruses, aimed at predicting significant mutations in spike protein sequences using Machine Learning (ML) models guided by Genetic Algorithms (GA). The project focuses on automating data collection, processing, and model training to create an effective mutation prediction pipeline.

## Objectives
- Develop a robust mutation predictor for coronaviruses.
- Automate data fetching from reliable biological databases.
- Optimize motifs using a Genetic Algorithm guided by ML model predictions.

## Features Implemented So Far
### 1. Automated Data Fetching
- Automated pipeline for fetching spike protein sequences using Snakemake.
- Utilizes Clustal Omega for sequence alignment to detect conserved motif regions.
- Ensures data integrity and completeness by checking and retrying incomplete files.

### 2. Virtual Environment Setup
- Isolated virtual environment for consistent dependencies using Python's `venv`.
- All dependencies required for the project are installed within this environment.

## Installation and Setup
### 1. Clone the Repository
```bash
 git clone <repository_url>
 cd ML-GA-Motif-Discovery/mutation_predictor
```

### 2. Set Up Virtual Environment
```bash
 python3 -m venv lib
 source lib/bin/activate
```
- The virtual environment is located in the `lib` folder.

### 3. Install Dependencies
```bash
 pip install -r requirements.txt
```
Ensure `requirements.txt` contains the latest versions of all dependencies.

## Dependencies
- `biopython>=1.81`
- `pandas>=2.1.1`
- `numpy>=1.26.4`
- `scikit-learn>=1.3.1`
- `matplotlib>=3.8.0`
- `seaborn>=0.13.0`
- `snakemake` (installed separately)

## Running the Project
### 1. Activate Virtual Environment
```bash
 source lib/bin/activate
```
### 2. Start Data Fetching Pipeline
```bash
 snakemake --cores 1
```
- To clean incomplete files and start over:
```bash
 snakemake --cleanup-metadata <incomplete_filenames>
```
- To rerun incomplete jobs:
```bash
 snakemake --rerun-incomplete
```

## Known Issues
- If encountering `pkgutil.ImpImporter` error, ensure `numpy==1.26.4` is installed.
- If `snakemake` is not found, check if the virtual environment is activated and correctly linked.

## Future Steps
- Implement feature encoding for motifs.
- Evolve motifs using Genetic Algorithm.
- Train ML model for mutation significance prediction.
