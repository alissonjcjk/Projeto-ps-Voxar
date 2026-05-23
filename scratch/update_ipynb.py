import nbformat
import sys

file_path = r'c:\Users\Alice Bernadino\Music\Projeto-ps-Voxar\notebook.ipynb'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # 1. Inserir célula Markdown após o Baseline (index 14)
    analysis_source = (
        "#### 📊 Análise das Curvas de Aprendizado (Baseline)\n\n"
        "Observando os gráficos de perda e acurácia gerados acima, notamos:\n"
        "1.  **Overfitting Moderado:** A perda de treino continua caindo enquanto a de validação estabiliza ou sobe levemente após a época 10. Isso sugere que o modelo começou a memorizar o ruído do treino.\n"
        "2.  **Instabilidade na Validação:** A curva de acurácia de validação apresenta oscilações, típicas de um dataset pequeno onde cada erro tem grande impacto percentual.\n"
        "3.  **Convergência Rápida:** O *fine-tuning* da ResNet-18 converge quase instantaneamente, validando o uso de pesos pré-treinados para extração de texturas de estrada."
    )
    
    already_exists = any("Análise das Curvas de Aprendizado (Baseline)" in getattr(c, 'source', '') for c in nb.cells)
    
    if not already_exists:
        new_cell = nbformat.v4.new_markdown_cell(source=analysis_source)
        nb.cells.insert(15, new_cell)
        print("Markdown cell inserted.")
    else:
        print("Markdown cell already exists.")

    # 2. Corrigir .applymap para .map
    modified_code = 0
    for cell in nb.cells:
        if cell.cell_type == 'code':
            if '.applymap(' in cell.source:
                cell.source = cell.source.replace('.applymap(', '.map(')
                modified_code += 1
    
    print(f"{modified_code} code cells updated.")

    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Notebook saved successfully.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
