import pandas as pd
import matplotlib.pyplot as plt


# ==============================
# CARREGAMENTO DOS DADOS
# ==============================

dados = pd.read_csv("data/measurements.csv")


# ==============================
# ANÁLISE DOS DADOS
# ==============================

dados.info()

print("\nEstatísticas dos dados:")
print(dados.describe())


temperatura_inicial = dados["temperature_C"].iloc[0]
temperatura_final = dados["temperature_C"].iloc[-1]

tempo_inicial = dados["time_s"].iloc[0]
tempo_final = dados["time_s"].iloc[-1]

variacao = temperatura_final - temperatura_inicial
variacao_tempo = tempo_final - tempo_inicial

taxa_media = variacao / variacao_tempo

desvio_padrao = dados["temperature_C"].std()


print("\nAnálise da temperatura:")
print("Temperatura inicial:", temperatura_inicial, "°C")
print("Temperatura final:", temperatura_final, "°C")
print("Variação de temperatura:", variacao, "°C")
print("Desvio padrão da temperatura:", f"{desvio_padrao:.3f}", "°C")
print("Taxa média de aquecimento:", f"{taxa_media:.3f}", "°C/s")


# ==============================
# TAXA DE AQUECIMENTO POR INTERVALO
# ==============================

dados["taxa_aquecimento"] = (
    dados["temperature_C"].diff() / dados["time_s"].diff()
)

print("\nTaxa de aquecimento por intervalo:")
print(dados[["time_s", "taxa_aquecimento"]])


# ==============================
# GRÁFICOS
# ==============================

# Gráfico da temperatura

plt.figure()

plt.plot(
    dados["time_s"],
    dados["temperature_C"],
    marker="o"
)

plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature vs Time")

plt.savefig("plots/temperature_vs_time.png")


# Gráfico da taxa de aquecimento

plt.figure()

plt.plot(
    dados["time_s"],
    dados["taxa_aquecimento"],
    marker="o"
)

plt.xlabel("Time (s)")
plt.ylabel("Heating Rate (°C/s)")
plt.title("Heating Rate vs Time")

plt.savefig("plots/heating_rate_vs_time.png")


# Mostrar os gráficos

plt.show()