# Simulador de Lançamento Oblíquo

Este é um simulador de lançamento oblíquo desenvolvido em Python, que utiliza a biblioteca Tkinter para a interface gráfica e Matplotlib para a visualização da trajetória e das energias envolvidas durante o movimento. O simulador permite a inclusão opcional da resistência do ar nos cálculos.

## Funcionalidades

- **Entrada de dados:** O usuário pode fornecer a velocidade inicial, o ângulo de lançamento e a altura inicial do objeto.
- **Simulação com/sem resistência do ar:** Existe uma opção para considerar a resistência do ar durante a simulação.
- **Visualização gráfica:** O simulador exibe a trajetória do objeto e gráficos das energias cinética, potencial e mecânica total.
- **Resultados detalhados:** O simulador calcula e exibe a distância máxima, a altura máxima atingida e o tempo de voo.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `math`
  - `matplotlib`
  - `tkinter`

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/seu-usuario/simulador-lancamento-obliquo.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd simulador-lancamento-obliquo
    ```
3. Instale as dependências necessárias:
    ```bash
    pip install matplotlib
    ```

## Como Usar

1. Execute o script Python:
    ```bash
    python simulador_lancamento_obliquo.py
    ```
2. A interface gráfica será aberta. Preencha os campos de entrada com os valores desejados:
    - **Velocidade inicial (m/s):** Valor da velocidade inicial do objeto.
    - **Ângulo de lançamento (graus):** Ângulo de lançamento em relação ao solo.
    - **Altura inicial (m):** Altura inicial do objeto.
    - **Considerar resistência do ar:** Marque esta opção se desejar incluir a resistência do ar na simulação.

3. Clique em **Simular** para ver os resultados:
    - A trajetória do objeto será exibida no gráfico da esquerda.
    - Os gráficos das energias cinética, potencial e mecânica total serão exibidos à direita.
    - Os resultados numéricos, como a distância máxima, a altura máxima e o tempo de voo, aparecerão abaixo dos botões.

## Exemplo de Uso

Para uma velocidade inicial de `20 m/s`, um ângulo de `45 graus`, e uma altura inicial de `0 metros` sem resistência do ar:

- **Distância máxima:** 40.82 metros
- **Altura máxima:** 10.20 metros
- **Tempo de voo:** 2.88 segundos

## Personalização

Você pode ajustar os parâmetros padrão e o comportamento do simulador editando o código Python conforme necessário. O coeficiente de resistência do ar e a massa do objeto são exemplos de valores que podem ser alterados.

#### Felipe Parreiras
<div style="display: inline-block;">
<a href="https://t.me/fparreiras">
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white"/> 
</a>

<a href="https://www.linkedin.com/in/felipe-parreiras-56b075277/">
<img align="center" height="20px" width="90px" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>
