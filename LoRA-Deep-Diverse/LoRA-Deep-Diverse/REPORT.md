# LoRA Deep–Diverse Raporu

## 1. Amaç
Qwen/Qwen2.5-Coder-1.5B-Instruct temel modelinden başlayarak iki ayrı LoRA fine-tuning yapılmıştır:
(1) deep_instruction, (2) diverse_instruction.
Amaç, LiveCodeBench (AtCoder easy) benchmark’ı ile en iyi checkpoint’i seçmektir.

## 2. Ayarlar (Özet)
- Base model: Qwen/Qwen2.5-Coder-1.5B-Instruct
- Epoch: 3
- Rank (r): 32
- Alpha: 64
- Context length: 800
- System prompt: You are an expert Python programmer. Please read the problem carefully before writing any Python code.

## 3. Loss Analizi
Train ve validation loss değerleri eğitim boyunca takip edilmiştir.
Grafikler figures/ klasöründe saklanır.

## 4. Benchmark (LiveCodeBench / AtCoder easy)
41 soru üzerinde Pass@1 metriği ile değerlendirme yapılmıştır.
Her model için en iyi checkpoint, Pass@1 değeri en yüksek olan checkpoint seçilerek belirlenmiştir.

| Model | En İyi Checkpoint | Pass@1 (%) | Çözülen Soru |
|---|---|---:|---:|
| deep_instruction | step-400-epoch-1 | 34.1 | 14/41 |
| diverse_instruction | checkpoint-step-800-epoch-3 | 43.9 | 18/41 |

Sonuç: diverse_instruction modeli daha yüksek Pass@1 elde ettiği için final model olarak seçilmiştir.
