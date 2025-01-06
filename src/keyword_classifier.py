import re

SISR_KEYWORDS = ["serveur", "virtualisation", "maintenance", "réseau"]
SLAM_KEYWORDS = ["application", "développement", "base de données", "programmation"]

def classify_description(description: str) -> str:
    """
    Classifie la description en SISR ou SLAM en se basant sur 
    la présence de mots-clés. 
    Retourne 'SISR', 'SLAM' ou 'Inconnu'.
    """
    # Mettre en minuscule pour simplifier la recherche
    desc_lower = description.lower()

    sisr_score = sum([1 for kw in SISR_KEYWORDS if kw in desc_lower])
    slam_score = sum([1 for kw in SLAM_KEYWORDS if kw in desc_lower])

    if sisr_score > slam_score and sisr_score > 0:
        return "SISR"
    elif slam_score > sisr_score and slam_score > 0:
        return "SLAM"
    else:
        return "Inconnu"
