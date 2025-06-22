# import networkx as nx
# import matplotlib.pyplot as plt

# # Crear un grafo dirigido (para representar el flujo del sistema)
# G = nx.DiGraph()

# # Definir los nodos y conexiones del sistema Gordiburg
# G.add_edges_from([
#     ("Inicio", "Selector (Cuenta)"),
#     ("Selector (Cuenta)", "Login"),
#     ("Selector (Cuenta)", "Signup"),
#     ("Login", "Opciones (Menú/Salir)"),
#     ("Signup", "Selector (Cuenta)"),
#     ("Opciones (Menú/Salir)", "Menú"),
#     ("Opciones (Menú/Salir)", "Salir"),
#     ("Menú", "Pagar"),
#     ("Pagar", "Salir")
# ])

# # Configuración del gráfico
# plt.figure(figsize=(12, 8))
# pos = nx.spring_layout(G, seed=42)

# # Dibujar el grafo
# nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=3000)
# nx.draw_networkx_edges(G, pos, edge_color="gray", arrowstyle="->", arrowsize=20)
# nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

# # Personalización
# plt.title("Diagrama de Flujo - Sistema Gordiburg", fontsize=14)
# plt.axis("off")
# plt.tight_layout()
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Relaciones entre los módulos
relaciones = [
    ("User", "Menu"),
    ("User", "Product Description"),
    ("Menu", "Product Description")
]

# Función para graficar cada tipo de grafo
def graficar_grafo(tipo, relaciones):
    if tipo == "DiGraph":
        G = nx.DiGraph()
    elif tipo == "MultiDiGraph":
        G = nx.MultiDiGraph()
        relaciones *= 2
    elif tipo == "Graph":
        G = nx.Graph()
    elif tipo == "MultiGraph":
        G = nx.MultiGraph()
        relaciones *= 2
    else:
        return

    G.add_edges_from(relaciones)
    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=3000,
            node_color="skyblue", font_size=10, font_weight="bold", arrows=True)
    plt.title(f"Grafo tipo {tipo}")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

# Ejecutar para los 4 tipos
for tipo in ["DiGraph", "MultiDiGraph", "Graph", "MultiGraph"]:
    graficar_grafo(tipo, relaciones)
