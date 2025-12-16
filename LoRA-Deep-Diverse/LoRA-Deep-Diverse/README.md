# LoRA Deep–Diverse Fine-Tuning (Qwen2.5-Coder-1.5B-Instruct)

Bu repo, aynı temel modelden başlayarak iki ayrı LoRA eğitimi yapmayı ve
LiveCodeBench (AtCoder easy, 41 soru) ile benchmark etmeyi içerir:

- Eğitim 1: deep_instruction
- Eğitim 2: diverse_instruction

## Kurulum
pip install -r requirements.txt

## Benchmark
En iyi checkpoint seçimi için Pass@1 en yüksek olan checkpoint alınır.

Çıktılar:
- figures/: Loss grafikleri
- logs/: Eğitim logları ve checkpoint tabloları
- results/: Benchmark özetleri ve final tablo
