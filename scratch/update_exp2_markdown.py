import json
import sys

file_path = r'c:\Users\Alice Bernadino\Music\Projeto-ps-Voxar\notebook.ipynb'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Inserir análise após as curvas do Exp 2
    # Atualmente a célula 30 (index 29) tem as curvas
    analysis_exp2 = [
        "#### 📈 Impacto do Data Augmentation na Generalização\n",
        "\n",
        "Ao comparar estas curvas com as do Baseline, observamos:\n",
        "1.  **Redução do Overfitting:** A distância entre a perda de treino e validação diminuiu drasticamente. O modelo agora é 'forçado' a aprender características genéricas de textura em vez de memorizar pixels específicos.\n",
        "2.  **Establização da Validação:** As oscilações na acurácia de validação foram suavizadas. O modelo não sofre mais tanto com 'sorte' ou 'azar' em lotes específicos de validação, indicando maior robustez."
    ]
    
    # Check if already exists
    exists = any("Impacto do Data Augmentation na Generalização" in "".join(c.get('source', [])) for c in data['cells'])
    
    if not exists:
        # We need to find the exact index. 
        # It's after the cell containing "plt.show()" for Exp 2.
        target_idx = -1
        for i, cell in enumerate(data['cells']):
            if cell['cell_type'] == 'code' and 'plot_learning_curves' in "".join(cell['source']) and i > 25:
                target_idx = i + 1
                break
        
        if target_idx != -1:
            new_cell = {
                "cell_type": "markdown",
                "metadata": {},
                "source": analysis_exp2
            }
            data['cells'].insert(target_idx, new_cell)
            print(f"Markdown cell inserted at index {target_idx}.")
        else:
            print("Target cell for insertion not found.")

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print("Notebook updated.")

except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
