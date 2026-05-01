# Classificação de Superfícies de Vias — Voxar Labs PS 2025

Solução para o desafio de classificação de imagens em 3 classes (**Asphalt**, **Belgian Blocks**, **Off-road**), desenvolvida como parte do processo seletivo da Voxar Labs.

---

## Estrutura do Projeto

```
projeto-ps-voxar/
├── notebook.ipynb        # Notebook principal com toda a solução e análise
├── requirements.txt      # Dependências Python
└── README.md             # Este arquivo
```

---

## Dataset

O dataset é composto por imagens de superfícies de vias capturadas em condições variadas (iluminação, chuva, período noturno, diferentes câmeras). Estrutura esperada:

```
dataset_processed/
├── train/
│   ├── asphalt/         # 655 imagens
│   ├── belgian_blocks/  # 94 imagens
│   └── offroad/         # 151 imagens
└── test/
    ├── asphalt/         # 218 imagens
    ├── belgian_blocks/  # 32 imagens
    └── offroad/         # 50 imagens
```

> ⚠️ O dataset **não está versionado** neste repositório. Coloque a pasta `dataset_processed/` na raiz do projeto antes de executar o notebook.

---

## Como Executar

```bash
# 1. Crie e ative um ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Abra o notebook
jupyter notebook notebook.ipynb
```

---

## Abordagem

| Etapa | Detalhe |
|---|---|
| **Modelo base** | ResNet-18 pré-treinado (ImageNet) |
| **Estratégia** | Fine-tuning das últimas camadas |
| **Desbalanceamento** | `CrossEntropyLoss` com pesos por classe |
| **Augmentation** | Flip, rotação, jitter de cor, blur |
| **Métricas** | F1-score macro, matriz de confusão por classe |

---

## Experimentos

1. **Baseline** — ResNet-18 fine-tuning simples
2. **Exp 1** — Adição de `class_weight` na loss function
3. **Exp 2** — Data augmentation agressivo

---

## Uso de LLMs

O desenvolvimento deste projeto contou com suporte de LLMs (Google Gemini) para:
- Revisão de código e boas práticas
- Redação técnica das seções de análise

