import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
import matplotlib.animation as animation

def simulador_lancamento_obliquo(velocidade_inicial, angulo, altura_inicial, resistencia_ar=False):
    angulo_rad = math.radians(angulo)
    velocidade_inicial_x = velocidade_inicial * math.cos(angulo_rad)
    velocidade_inicial_y = velocidade_inicial * math.sin(angulo_rad)
    gravidade = 9.8
    massa_bola = 10
    coef_resistencia_ar = 0.05 if resistencia_ar else 0

    tempo_voo = (velocidade_inicial_y + math.sqrt(velocidade_inicial_y ** 2 + 2 * gravidade * altura_inicial)) / gravidade
    if angulo == 90:
        distancia_maxima = 0
    else:
        distancia_maxima = (velocidade_inicial**2 * math.sin(2 * angulo_rad)) / gravidade

    altura_maxima = altura_inicial + ((velocidade_inicial_y ** 2) / (2 * gravidade))

    tempo = [i / 100 for i in range(int(tempo_voo * 100))]
    posicao_x = []
    posicao_y = []

    for t in tempo:
        if resistencia_ar:
            # Considerando resistência do ar
            velocidade_inicial_x *= math.exp(-coef_resistencia_ar * t)
            velocidade_inicial_y = (velocidade_inicial * math.sin(angulo_rad) - gravidade * t) * math.exp(-coef_resistencia_ar * t)
        x = velocidade_inicial_x * t
        y = altura_inicial + velocidade_inicial_y * t - 0.5 * gravidade * t ** 2
        if y < 0:
            break
        posicao_x.append(x)
        posicao_y.append(y)

    velocidades = []
    for t in tempo[:len(posicao_x)]:
        velocidade_horizontal = velocidade_inicial_x
        velocidade_vertical = velocidade_inicial_y - gravidade * t
        velocidade_resultante = math.sqrt(velocidade_horizontal ** 2 + velocidade_vertical ** 2)
        velocidades.append(velocidade_resultante)

    energia_potencial = [massa_bola * gravidade * y for y in posicao_y]
    energia_cinetica = [0.5 * massa_bola * velocidade ** 2 for velocidade in velocidades]
    energia_mecanica = [potencial + cinetica for potencial, cinetica in zip(energia_potencial, energia_cinetica)]

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

    return distancia_maxima, altura_maxima, tempo_voo

def plot_grafico():
    velocidade = float(entrada_velocidade.get())
    angulo = float(entrada_angulo.get())
    altura_inicial = float(entrada_altura.get())
    resistencia_ar = var_resistencia.get() == 1

    distancia, altura_max, tempo = simulador_lancamento_obliquo(velocidade, angulo, altura_inicial, resistencia_ar)

    resultado_label.config(text=f"Distância máxima: {distancia:.2f} metros\nAltura máxima: {altura_max:.2f} metros\nTempo de voo: {tempo:.2f} segundos")

# Cria uma janela
janela = tk.Tk()
janela.title("Simulador de Lançamento Oblíquo")
fonte = ('Helvetica', 12)

# Cria rótulos e entradas para as variáveis de entrada
label_velocidade = ttk.Label(janela, text="Velocidade inicial (m/s):", font=fonte)
label_angulo = ttk.Label(janela, text="Ângulo de lançamento (graus):", font=fonte)
label_altura = ttk.Label(janela, text="Altura inicial (m):", font=fonte)
entrada_velocidade = ttk.Entry(janela, font=fonte)
entrada_angulo = ttk.Entry(janela, font=fonte)
entrada_altura = ttk.Entry(janela, font=fonte)

# Checkbox para resistência do ar
var_resistencia = tk.IntVar()
checkbox_resistencia = tk.Checkbutton(janela, text="Considerar resistência do ar", variable=var_resistencia, font=fonte)
checkbox_resistencia.grid(row=3, columnspan=2, pady=5)

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
entrada_velocidade.grid(row=0, column=1, padx=10, pady=5)
entrada_angulo.grid(row=1, column=1, padx=10, pady=5)
entrada_altura.grid(row=2, column=1, padx=10, pady=5)
checkbox_resistencia.grid(row=3, columnspan=2, pady=5)
botao_simular.grid(row=4, columnspan=2, pady=10)
resultado_label.grid(row=5, columnspan=2, padx=10, pady=5)

# Inicia a interface gráfica
janela.mainloop()
