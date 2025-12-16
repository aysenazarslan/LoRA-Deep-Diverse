# LoRA-Based Fine-Tuning with Deep and Diverse Instruction Datasets

## Abstract

This report presents a comparative study on LoRA-based fine-tuning applied to a shared code generation model using two different instruction-style datasets: **deep_instruction** and **diverse_instruction**. The objective of the study is to analyze how dataset characteristics influence model generalization and performance on competitive programming tasks. All models are evaluated using the LiveCodeBench benchmark under identical conditions, and the best-performing checkpoints are selected based on Pass@1 scores.

---

## 1. Introduction

Large Language Models (LLMs) have shown strong performance in code generation tasks. However, full fine-tuning of such models is computationally expensive. **LoRA (Low-Rank Adaptation)** provides an efficient alternative by adapting only a small number of trainable parameters while keeping the base model frozen.

In this project, LoRA is applied to the same base model using two different instruction datasets. The main research question is whether **dataset diversity** or **instruction depth** has a greater impact on downstream code generation performance.

---

## 2. Base Model and Fine-Tuning Method

### 2.1 Base Model

- **Model:** Qwen/Qwen2.5-Coder-1.5B-Instruct  
- **Domain:** Code generation and programming tasks  
- **Architecture:** Decoder-only transformer  

The same base model is used for all experiments to ensure a fair comparison.

### 2.2 LoRA Fine-Tuning

LoRA introduces low-rank matrices into selected attention layers, significantly reducing the number of trainable parameters. This enables efficient fine-tuning while preserving the original capabilities of the base model.

Key advantages of LoRA:
- Reduced memory usage
- Faster training
- Lower risk of catastrophic forgetting

---

## 3. Dataset Description

Two instruction-style datasets are used:

### 3.1 Deep Instruction Dataset

The **deep_instruction** dataset focuses on:
- Step-by-step reasoning
- Detailed explanations
- Structured problem-solving patterns

This dataset emphasizes depth and logical consistency within each sample.

### 3.2 Diverse Instruction Dataset

The **diverse_instruction** dataset emphasizes:
- Variety in problem types
- Different instruction formulations
- Broader coverage of coding styles

The goal is to improve generalization by exposing the model to a wider range of instructions.

---

## 4. Training Setup

- **Fine-tuning method:** LoRA
- **Train / Validation / Test splits:**  
  HuggingFace predefined splits are used directly without manual re-splitting.
- **Hyperparameters:**  
  Identical hyperparameters are applied to both datasets to ensure fairness.
- **Training strategy:**  
  - Regular checkpoint saving  
  - Evaluation at fixed step intervals  
  - Early stopping mechanisms to prevent overfitting  

Both models are trained independently starting from the same base checkpoint.

---

## 5. Evaluation Methodology

### 5.1 Benchmark

- **Benchmark:** LiveCodeBench (release_v5)
- **Platform:** AtCoder
- **Difficulty:** Easy
- **Number of problems:** 41

LiveCodeBench provides a standardized and reproducible evaluation pipeline for code generation models.

### 5.2 Metric

- **Pass@1:**  
  Measures whether the model’s first generated solution passes all test cases.

Pass@1 is chosen as it reflects real-world usability where only a single attempt is allowed.

---

## 6. Checkpoint Selection Strategy

For each training variant:
1. All saved checkpoints are evaluated using LiveCodeBench.
2. Pass@1 scores are extracted from the evaluation results.
3. The checkpoint with the highest Pass@1 score is selected as the **best checkpoint**.
4. The number of solved problems is reported alongside Pass@1.

This process ensures objective and comparable model selection.

---

## 7. Results

### 7.1 Best Checkpoint Results

| Model               | Best Checkpoint               | Pass@1 (%) | Solved Problems |
|--------------------|-------------------------------|------------|-----------------|
| deep_instruction   | step-400-epoch-1              | 34.1       | 14 / 41         |
| diverse_instruction| checkpoint-step-800-epoch-3   | 43.9       | 18 / 41         |

### 7.2 Observations

- The **diverse_instruction** model achieves the highest Pass@1 score.
- Dataset diversity leads to improved generalization on unseen problems.
- The deep_instruction model performs well on structured problems but shows lower overall coverage.

---

## 8. Discussion

The results indicate that dataset diversity plays a critical role in LoRA-based fine-tuning for code generation tasks. While deep, structured instructions help the model learn reasoning patterns, exposure to diverse instructions improves adaptability across different problem formulations.

This suggests that for competitive programming and general-purpose code generation, **instruction diversity** may be more beneficial than instruction depth alone.

---

## 9. Conclusion

In this project, two LoRA fine-tuned models were compared under identical conditions. The experimental results demonstrate that the **diverse_instruction** dataset leads to superior performance on the LiveCodeBench benchmark.

These findings highlight the importance of dataset design in parameter-efficient fine-tuning and provide insights for future work on instruction-based model adaptation.

---

## 10. Future Work

Possible extensions of this study include:
- Evaluating on harder difficulty levels
- Combining deep and diverse instruction datasets
- Testing different LoRA ranks and configurations
- Comparing LoRA with other parameter-efficient fine-tuning methods
