import pandas as pd
import matplotlib.pyplot as plt

def carregar_fitxer(ruta):
    """Llegeix el fitxer CSV i el transforma en un DataFrame."""
    taula_dades = pd.read_csv(ruta)
    taula_dades.dropna(inplace=True) # Eliminacio de valors nuls
    return taula_dades

def calcular_resum(df):
    """Calcula estadístiques bàsiques sobre les dades de vendes."""
    return df.describe()

def generar_grafics(df):
    """Crea visualitzacions gràfiques de les dades."""
    vendes_per_producte = df.groupby("producte")["quantitat"].sum().sort_values(ascending=False)
    ingressos_per_producte = df.groupby("producte").apply(lambda x: (x["quantitat"] * x["preu"]).sum(), include_groups=False).sort_values(ascending=False)

    # Gràfic de quantitats venudes
    plt.figure(figsize=(14, 8))
    vendes_per_producte.plot(kind="bar")
    plt.title("Vendes totals per producte")
    plt.xlabel("Producte")
    plt.ylabel("Quantitat")
    plt.xticks(rotation=75, fontsize=12, ha='right')
    plt.show()

    # Gràfic d'ingressos per producte
    plt.figure(figsize=(14, 8))
    ingressos_per_producte.plot(kind="bar")
    plt.title("Ingressos per producte")
    plt.xlabel("Producte")
    plt.ylabel("Total d'ingressos (€)")
    plt.xticks(rotation=75, fontsize=12, ha='right')
    plt.show()

def executar():
    arxiu = "dades.csv" # Ruta del fitxer CSV
    dades = carregar_fitxer(arxiu)
    estadistiques = calcular_resum(dades)
    print("Resum de les dades: ")
    print(estadistiques)
    generar_grafics(dades)

if __name__ == "__main__":
    executar()