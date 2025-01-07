# tests/evaluation.py
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# On importe le classifieur "mots-clés"
from src.zero_shot_classifier import classify_zero_shot


def evaluate_classifier(descriptions, labels):
    # On fait des prédictions
    predictions = [classify_zero_shot(desc) for desc in descriptions]

    # Calcul des métriques
    acc = accuracy_score(labels, predictions)
    prec = precision_score(labels, predictions, average='macro', zero_division=0)
    rec = recall_score(labels, predictions, average='macro', zero_division=0)
    f1 = f1_score(labels, predictions, average='macro', zero_division=0)

    print(f"Accuracy:  {acc:.2f}")
    print(f"Precision: {prec:.2f}")
    print(f"Recall:    {rec:.2f}")
    print(f"F1-score:  {f1:.2f}")

    # Matrice de confusion
    cm = confusion_matrix(labels, predictions, labels=["SISR", "SLAM", "Inconnu"])
    print("Matrice de confusion :\n", cm)

    sns.heatmap(cm, annot=True, fmt='d',
                xticklabels=["SISR", "SLAM", "Inconnu"],
                yticklabels=["SISR", "SLAM", "Inconnu"])
    plt.xlabel("Prédiction")
    plt.ylabel("Vrai label")
    plt.title("Matrice de confusion - Classifieur Mots-Clés")
    plt.show()


if __name__ == "__main__":
    descriptions = [
        "Je travaille sur des serveurs et de la virtualisation",  # SISR
        "Je développe des applications web",  # SLAM
        "Je gère la maintenance du réseau",  # SISR
        "Je code des scripts Python pour manipuler des BDD",  # SLAM
        "J'aime l'informatique en général",  # Inconnu
    ]

    labels = [
        "SISR",
        "SLAM",
        "SISR",
        "SLAM",
        "Inconnu",
    ]

    evaluate_classifier(descriptions, labels)
