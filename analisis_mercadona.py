import pandas as pd # Importamos Pandas para manipular datos en forma de DataFrame
import matplotlib.pyplot as plt # Importamos Matplotlib para generar gráficos

def carregar_fitxer(ruta):
    """Llegeix el fitxer CSV i el transforma en un DataFrame."""
    taula_dades = pd.read_csv(ruta) # Carga el archivo CSV en un DataFrame
    taula_dades.dropna(inplace=True) # Elimina las filas con valores nulos para limpiar los datos
    return taula_dades # Devuelve el DataFrame más limpio

def calcular_resum(df):
    """Calcula estadístiques bàsiques sobre les dades de vendes."""
    return df.describe() # Retorna un resumen estadístico del DataFrame

def generar_grafics(df):
    """Crea visualitzacions gràfiques de les dades."""

    # Calculamos el total de unidades vendidas por producto
    vendes_per_producte = df.groupby("producte")["quantitat"].sum().sort_values(ascending=False)

    # Calculamos los ingresos totales por producto
    ingressos_per_producte = df.groupby("producte").apply(lambda x: (x["quantitat"] * x["preu"]).sum(), include_groups=False).sort_values(ascending=False)

    # Generamos un gráfico de barras para visualizar la cantidad de ventas por producto
    plt.figure(figsize=(14, 8)) # Tamaño
    vendes_per_producte.plot(kind="bar") # Creo el gráfico
    plt.title("Vendes totals per producte") # Título
    plt.xlabel("Producte") # Eje X
    plt.ylabel("Quantitat") # Eje Y
    plt.xticks(rotation=75, fontsize=12, ha='right') # Roto las etiquetas para que se lea mejor
    plt.show() # Mostrar gráfico

    # Gràfic d'ingressos per producte
    plt.figure(figsize=(14, 8))
    ingressos_per_producte.plot(kind="bar")
    plt.title("Ingressos per producte")
    plt.xlabel("Producte")
    plt.ylabel("Total d'ingressos (€)")
    plt.xticks(rotation=75, fontsize=12, ha='right')
    plt.show()

def executar():
    arxiu = "dades.csv" # Defino la ruta del archivo CSV con los datos de ventas
    dades = carregar_fitxer(arxiu) # Cargo los datos desde el archivo
    estadistiques = calcular_resum(dades) # Calculo estadísticas básicas
    print("Resum de les dades: ") # Muestro un mensaje informativo
    print(estadistiques) # Imprimo las estadísticas en la consola
    generar_grafics(dades) # Genero gráficos con los datos cargados

if __name__ == "__main__":
    executar()