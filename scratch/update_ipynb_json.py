import json
import sys

file_path = r'c:\Users\Alice Bernadino\Music\Projeto-ps-Voxar\notebook.ipynb'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Inserir célula Markdown após index 14
    analysis_source = [
        "#### 📊 Análise das Curvas de Aprendizado (Baseline)\n",
        "\n",
        "Observando os gráficos de perda e acurácia gerados acima, notamos:\n",
        "1.  **Overfitting Moderado:** A perda de treino continua caindo enquanto a de validação estabiliza ou sobe levemente após a época 10. Isso sugere que o modelo começou a memorizar o ruído do treino.\n",
        "2.  **Instabilidade na Validação:** A curva de acurácia de validação apresenta oscilações, típicas de um dataset pequeno onde cada erro tem grande impacto percentual.\n",
        "3.  **Convergência Rápida:** O *fine-tuning* da ResNet-18 converge quase instantaneamente, validando o uso de pesos pré-treinados para extração de texturas de estrada."
    ]
    
    already_exists = any("Análise das Curvas de Aprendizado (Baseline)" in "".join(c.get('source', [])) for c in data['cells'])
    
    if not already_exists:
        new_cell = {
            "cell_type": "markdown",
            "metadata": {},
            "source": analysis_source
        }
        data['cells'].insert(15, new_cell)
        print("Markdown cell inserted.")
    else:
        print("Markdown cell already exists.")

    # 2. Corrigir .applymap para .map
    modified_code = 0
    for cell in data['cells']:
        if cell['cell_type'] == 'code':
            new_source = []
            changed = False
            for line in cell['source']:
                if '.applymap(' in line:
                    new_source.append(line.replace('.applymap(', '.map('))
                    changed = True
                else:
                    new_source.append(line)
            if changed:
                cell['source'] = new_source
                modified_code += 1
    
    print(f"{modified_code} code cells updated.")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print("Notebook saved successfully.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
