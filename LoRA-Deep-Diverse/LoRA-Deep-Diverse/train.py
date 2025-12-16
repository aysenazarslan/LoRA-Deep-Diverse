"""
train.py - LoRA training script placeholder.
Notebook/Colab'daki eğitim kodunu buraya taşıyıp çalıştırabilirsiniz.
"""
import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset_type", choices=["deep_instruction","diverse_instruction"], required=True)
    p.add_argument("--base_model", default="Qwen/Qwen2.5-Coder-1.5B-Instruct")
    p.add_argument("--epochs", type=int, default=3)
    p.add_argument("--rank", type=int, default=32)
    p.add_argument("--alpha", type=int, default=64)
    p.add_argument("--context_length", type=int, default=800)
    p.add_argument("--output_dir", default="models")
    args = p.parse_args()
    print("Training config:", vars(args))
    print("TODO: Colab eğitim hücresindeki kodu buraya taşı.")
if __name__ == "__main__":
    main()
