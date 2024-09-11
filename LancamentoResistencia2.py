import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation

def simulador_lancamento_obliquo(velocidade_inicial, angulo, altura_inicial, gravidade, coef_resistencia_ar, resistencia_ar):
    angulo_rad = math.radians(angulo)
    velocidade_inicial_x = velocidade_inicial * math.cos(angulo_rad)
    velocidade_inicial_y = velocidade_inicial * math.sin(angulo_rad)
    massa_bola = 10

    # Se resistência do ar não for considerada, o coeficiente é zero
    if not resistencia_ar:
        coef_resistencia_ar = 0

    # Listas para armazenar posição, tempo e velocidade
    posicao_x = [0]
    posicao_y = [altura_inicial]
    velocidades_x = [velocidade_inicial_x]
    velocidades_y = [velocidade_inicial_y]

    dt = 0.01  # Pequeno intervalo de tempo
    tempo = [0]  # Inicia em zero

    while posicao_y[-1] >= 0:  # Continua enquanto a bola não atingir o chão
        t = tempo[-1] + dt

        # Atualizando as velocidades com ou sem resistência do ar
        velocidade_x = velocidades_x[-1] * (1 - coef_resistencia_ar * dt)
        velocidade_y = velocidades_y[-1] - gravidade * dt

        # Atualizando a posição
        x = posicao_x[-1] + velocidade_x * dt
        y = posicao_y[-1] + velocidade_y * dt

        # Adiciona os novos valores nas listas
        posicao_x.append(x)
        posicao_y.append(y)
        velocidades_x.append(velocidade_x)
        velocidades_y.append(velocidade_y)
        tempo.append(t)

    # Distância máxima é a última posição em X
    distancia_maxima = posicao_x[-1]

    # Altura máxima é o maior valor de y
    altura_maxima = max(posicao_y)

    # Tempo de voo é o último valor de tempo
    tempo_voo = tempo[-1]

    # Cálculo das energias
    velocidades = [math.sqrt(vx ** 2 + vy ** 2) for vx, vy in zip(velocidades_x, velocidades_y)]
    energia_potencial = [massa_bola * gravidade * y for y in posicao_y]
    energia_cinetica = [0.5 * massa_bola * v ** 2 for v in velocidades]
    energia_mecanica = [pot + cin for pot, cin in zip(energia_potencial, energia_cinetica)]

    # Função para animação
    def update(frame):
        ax_trajetoria.clear()
        ax_trajetoria.set_xlim(0, max(posicao_x))
        ax_trajetoria.set_ylim(0, max(posicao_y) + 1)
        ax_trajetoria.plot(posicao_x, posicao_y, label='Trajetória')
        ax_trajetoria.plot(posicao_x[frame], posicao_y[frame], 'ro')  # Objeto em movimento
        ax_trajetoria.set_xlabel('Distância (m)')
        ax_trajetoria.set_ylabel('Altura (m)')
        ax_trajetoria.legend()
        ax_trajetoria.grid(True)

        # Atualiza os gráficos de energia
        ax_energia.clear()
        ax_energia.plot(tempo[:len(energia_potencial)], energia_potencial, 'r', label='Energia Potencial Gravitacional')
        ax_energia.plot(tempo[:len(energia_cinetica)], energia_cinetica, 'b', label='Energia Cinética')
        ax_energia.plot(tempo[:len(energia_mecanica)], energia_mecanica, 'g', label='Energia Mecânica Total')
        ax_energia.set_xlabel('Tempo (s)')
        ax_energia.set_ylabel('Energia (J)')
        ax_energia.legend()
        ax_energia.grid(True)

    fig, (ax_trajetoria, ax_energia) = plt.subplots(1, 2, figsize=(14, 6))
    ani = animation.FuncAnimation(fig, update, frames=len(posicao_x), interval=20)
    plt.show()

    # Exibir os resultados no terminal
    print(f"Distância máxima: {distancia_maxima:.2f} metros")
    print(f"Altura máxima: {altura_maxima:.2f} metros")
    print(f"Tempo de voo: {tempo_voo:.2f} segundos")

    return distancia_maxima, altura_maxima, tempo_voo

def plot_grafico():
    velocidade = float(entrada_velocidade.get())
    angulo = float(entrada_angulo.get())
    altura_inicial = float(entrada_altura.get())
    gravidade = float(entrada_gravidade.get())
    coef_resistencia_ar = float(entrada_coef_resistencia.get())
    resistencia_ar = var_resistencia.get() == 1  # Verifica se o checkbox está marcado

    distancia, altura_max, tempo = simulador_lancamento_obliquo(velocidade, angulo, altura_inicial, gravidade, coef_resistencia_ar, resistencia_ar)

    # Exibir os resultados na janela
    resultado_label.config(text=f"Distância máxima: {distancia:.2f} metros\nAltura máxima: {altura_max:.2f} metros\nTempo de voo: {tempo:.2f} segundos")

# Cria uma janela
janela = tk.Tk()
janela.title("Simulador de Lançamento Oblíquo")
fonte = ('Helvetica', 12)

# Cria rótulos e entradas para as variáveis de entrada
label_velocidade = ttk.Label(janela, text="Velocidade inicial (m/s):", font=fonte)
label_angulo = ttk.Label(janela, text="Ângulo de lançamento (graus):", font=fonte)
label_altura = ttk.Label(janela, text="Altura inicial (m):", font=fonte)
label_gravidade = ttk.Label(janela, text="Gravidade (m/s²):", font=fonte)
label_coef_resistencia = ttk.Label(janela, text="Coeficiente de Arrasto:", font=fonte)

entrada_velocidade = ttk.Entry(janela, font=fonte)
entrada_angulo = ttk.Entry(janela, font=fonte)
entrada_altura = ttk.Entry(janela, font=fonte)
entrada_gravidade = ttk.Entry(janela, font=fonte)
entrada_coef_resistencia = ttk.Entry(janela, font=fonte)

# Checkbox para resistência do ar
var_resistencia = tk.IntVar()
checkbox_resistencia = tk.Checkbutton(janela, text="Considerar resistência do ar", variable=var_resistencia, font=fonte)

# Botão de simulação
botao_simular = ttk.Button(janela, text="Simular", command=plot_grafico, style='Estilo.TButton')
janela.option_add('*TButton*padding', (5, 5))
janela.style = ttk.Style()
janela.style.configure('Estilo.TButton', font=fonte, foreground='white', background='#4CAF50', width=20)

# Rótulo para exibir resultados
resultado_label = ttk.Label(janela, font=fonte, anchor='center')

# Organiza os widgets na janela
label_velocidade.grid(row=0, column=0, padx=10, pady=5)
label_angulo.grid(row=1, column=0, padx=10, pady=5)
label_altura.grid(row=2, column=0, padx=10, pady=5)
label_gravidade.grid(row=3, column=0, padx=10, pady=5)
label_coef_resistencia.grid(row=4, column=0, padx=10, pady=5)

entrada_velocidade.grid(row=0, column=1, padx=10, pady=5)
entrada_angulo.grid(row=1, column=1, padx=10, pady=5)
entrada_altura.grid(row=2, column=1, padx=10, pady=5)
entrada_gravidade.grid(row=3, column=1, padx=10, pady=5)
entrada_coef_resistencia.grid(row=4, column=1, padx=10, pady=5)

checkbox_resistencia.grid(row=5, columnspan=2, pady=5)
botao_simular.grid(row=6, columnspan=2, pady=10)
resultado_label.grid(row=7, columnspan=2, padx=10, pady=5)

# Inicia a interface gráfica
janela.mainloop()
