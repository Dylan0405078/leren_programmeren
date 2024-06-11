import matplotlib.pyplot as plt
import networkx as nx

def generate_flowchart():
    G = nx.DiGraph()

    # Definieer de knopen en verbindingen
    nodes = [
        ("Hoofdprogramma", "Welkom"),
        ("Welkom", "Stap 1"),
        ("Stap 1", "Aantal bolletjes geldig?"),
        ("Aantal bolletjes geldig?", "Aantal bolletjes"),
        ("Aantal bolletjes geldig?", "Print foutmelding"),
        ("Aantal bolletjes", "1 tot 3"),
        ("Aantal bolletjes", "4 tot 8"),
        ("Aantal bolletjes", "Meer dan 8"),
        ("1 tot 3", "Stap 2"),
        ("4 tot 8", "Voeg toe aan bestelling"),
        ("4 tot 8", "Meer Bestellen"),
        ("Meer dan 8", "Print foutmelding"),
        ("Stap 2", "Hoorntje of bakje geldig?"),
        ("Hoorntje of bakje geldig?", "Stap 3"),
        ("Hoorntje of bakje geldig?", "Print foutmelding"),
        ("Stap 3", "Print bestelling samenvatting"),
        ("Print bestelling samenvatting", "Voeg toe aan bestelling"),
        ("Meer Bestellen", "Meer bestellen?"),
        ("Meer bestellen?", "Welkom"),
        ("Meer bestellen?", "Print afscheid"),
        ("Print afscheid", "Print bonnetje")
    ]

    # Voeg knopen en verbindingen toe aan de grafiek
    for start, end in nodes:
        G.add_edge(start, end)

    # Positie van knopen instellen
    pos = nx.spring_layout(G)

    # Teken de flowchart
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_weight="bold", arrowsize=20,
            edge_color='grey', width=2, alpha=0.7, arrows=True)
    plt.title("Flowchart")
    plt.show()

generate_flowchart()
