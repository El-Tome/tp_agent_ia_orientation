from transformers import pipeline

# On choisit un pipeline "zero-shot-classification" avec un modèle XNLI multilingue
classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")


def classify_zero_shot(description: str) -> str:
    # On définit la liste de classes possibles
    candidate_labels = ["SISR", "SLAM", "Inconnu"]

    # On interroge le pipeline
    result = classifier(description, candidate_labels)
    # result ressemble à un dictionnaire contenant "labels" et "scores".

    # On récupère le label avec la plus forte probabilité
    best_label = result["labels"][0]
    return best_label


if __name__ == "__main__":
    # Petit test
    text = "Je développe une application web"
    pred = classify_zero_shot(text)
    print(f"Texte : {text}")
    print(f"Prédiction zero-shot : {pred}")
