#WelcomeMessage
#Menu
#LoginValidation

import networkx as nx
import matplotlib.pyplot as plt

#* Here we create a directed graph
burger = nx.DiGraph()

#* Here we create nodes and dependencies
burger.add_edges_from([
    ("Bienvenido a GordiBurger!-Tu lugar favorito para comer", "Tienes cuenta?"),
    ("Tienes cuenta?", "Si/No"),
    ("Si/No", "Hamburguesa-$35.00, hot dog: $25.00, refresco: $20.00, agua fresca:$20.00")
])

#* Here we draw a Grafe...
nx.draw(burger, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, arrows=True)
plt.title("Basic Architecture For Modules")
plt.show()