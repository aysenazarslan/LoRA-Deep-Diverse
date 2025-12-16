# LoRA Deep–Diverse Fine-Tuning Project

This repository presents a comparative study of LoRA-based fine-tuning using two different instruction-style datasets on a shared base model. The objective is to analyze how dataset characteristics affect code generation performance and to select the best-performing checkpoint using a standardized benchmark.

---

## Project Overview

- **Base Model:** Qwen/Qwen2.5-Coder-1.5B-Instruct  
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)  
- **Training Variants:**
  - deep_instruction
  - diverse_instruction
- **Evaluation Benchmark:** LiveCodeBench (AtCoder Easy – 41 problems)
- **Evaluation Metric:** Pass@1  

Both models are fine-tuned starting from the same base model and evaluated under identical benchmark conditions.

---

## Repository Structure

LoRA-Deep-Diverse/
├── train.py
├── eval.py
├── requirements.txt
├── logs/
├── results/
├── figures/
├── README.md
└── REPORT.md

yaml
Kodu kopyala

---

## Installation

```bash
pip install -r requirements.txt
Training
Two independent LoRA fine-tuning runs are performed using the same base model:

bash
Kodu kopyala
python train.py --dataset_type deep_instruction
python train.py --dataset_type diverse_instruction
Identical hyperparameters are used in both trainings to ensure a fair comparison.

Evaluation
Model performance is evaluated using LiveCodeBench with AtCoder Easy problems:

bash
Kodu kopyala
python eval.py --eval_dir results/livecodebench/evaluations
The checkpoint with the highest Pass@1 score is selected as the final model for each training variant.

Results Summary
Model	Best Checkpoint	Pass@1 (%)	Solved Problems
deep_instruction	step-400-epoch-1	34.1	14 / 41
diverse_instruction	checkpoint-step-800-epoch-3	43.9	18 / 41

Conclusion
The results show that the diverse_instruction model achieves better generalization performance under the same training conditions. This highlights the importance of dataset diversity in LoRA-based fine-tuning for code generation tasks.
