# 🧬 ML-GA-Motif-Discovery  
### Machine Learning & Genetic Algorithm for Identifying Significant Viral Motifs  

## 🚀 Overview  
This repository implements a **Machine Learning (ML) + Genetic Algorithm (GA) pipeline** to discover **significant motifs in viral spike proteins**. Instead of using heuristic-based motif identification, this approach **optimizes motif discovery using ML-driven fitness evaluation**.  

## 🔬 Key Features  
✅ Fetches **spike protein sequences** from **NCBI & UniProt**  
✅ Aligns sequences using **Clustal Omega (MSA)**  
✅ Extracts **highly conserved motifs** across species  
✅ Encodes motifs as **amino acid frequency vectors**  
✅ Trains an **ML model (Random Forest)** to classify motifs  
✅ Uses **Genetic Algorithm (GA)** to evolve significant motifs  
✅ Validates motifs by comparing with **known functional regions (PROSITE, RBD, NTD)**  

## 📂 Project Structure  
