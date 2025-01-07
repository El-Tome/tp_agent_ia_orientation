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
        # SISR
        "Je travaille sur des serveurs et de la virtualisation",
        "Je gère la maintenance du réseau",
        "J'installe et configure des systèmes d'exploitation Linux",
        "Je supervise les performances des serveurs en temps réel",
        "Je configure des firewalls pour sécuriser le réseau",
        "Je mets en place des solutions de sauvegarde pour les données",
        "Je travaille sur des projets de migration vers le cloud",
        "Je suis responsable de la gestion du réseau de l'entreprise",
        "Je configure des commutateurs et des routeurs Cisco",
        "Je répare des serveurs physiques en cas de panne matérielle",

        # SLAM
        "Je développe des applications web",
        "Je code des scripts Python pour manipuler des BDD",
        "Je conçois des interfaces utilisateur en JavaScript et HTML",
        "Je crée des applications mobiles en utilisant Flutter",
        "Je développe des outils de reporting pour analyser les données",
        "Je travaille sur des API REST pour connecter différentes applications",
        "Je m'occupe de la maintenance et du développement d'une application CRM",
        "Je conçois des bases de données relationnelles pour des projets clients",
        "Je développe des scripts pour automatiser des processus métier",
        "Je code des applications full-stack en Node.js et React",

        # Inconnu
        "J'aime l'informatique en général",
        "Je découvre différentes technologies pour le plaisir",
        "Je m'intéresse autant au hardware qu'au software",
        "Je fais des projets personnels sans spécialisation particulière",
        "Je suis passionné par l'innovation dans le domaine de la tech",
        "J'apprends les bases de la programmation pour le plaisir",
        "Je lis des articles sur les tendances technologiques",
        "Je dépanne les ordinateurs de mes amis pour m'amuser",
        "Je m'intéresse à tout ce qui touche au numérique sans préférence",
        "Je participe à des forums en ligne sur des sujets techniques divers",

        # SISR
        "Je configure des serveurs de messagerie pour une entreprise",
        "Je travaille sur des solutions de virtualisation comme VMware et Hyper-V",
        "Je configure des VPN pour permettre le télétravail sécurisé",
        "Je surveille l'état des systèmes et des réseaux avec des outils comme Nagios",
        "Je mets en place des stratégies de sauvegarde avec des outils comme Veeam",
        "Je dépanne les problèmes de connectivité réseau sur le terrain",
        "Je déploie des solutions de stockage SAN et NAS",
        "Je fais la gestion des utilisateurs et des permissions via Active Directory",
        "Je m'assure de la sécurité des systèmes en appliquant des mises à jour régulières",
        "Je configure des solutions proxy pour sécuriser les accès Internet",
        "Je gère la performance des systèmes en optimisant les ressources",

        # SLAM
        "Je développe une application de gestion des stocks pour une PME",
        "Je conçois des sites web en utilisant WordPress et des frameworks PHP",
        "Je code des scripts en Python pour extraire des données depuis des API externes",
        "Je construis des dashboards interactifs pour visualiser des données complexes",
        "Je développe des applications SaaS pour les entreprises",
        "Je crée des systèmes d'authentification sécurisés pour des sites web",
        "Je travaille sur des projets de migration de bases de données SQL vers NoSQL",
        "Je programme des jeux vidéo en utilisant Unity et C#",
        "Je déploie des microservices avec Docker et Kubernetes",
        "Je fais de la maintenance sur des applications mobiles développées en React Native",
        "Je développe des bots pour automatiser des tâches sur des plateformes comme Discord",

        # Inconnu
        "Je suis curieux de découvrir des langages de programmation comme Rust",
        "J'aime explorer les nouvelles technologies sans but professionnel",
        "Je regarde des vidéos sur les innovations en intelligence artificielle",
        "Je participe à des ateliers pour apprendre les bases du codage",
        "Je m'intéresse à l'histoire des systèmes informatiques",
        "Je suis fasciné par les algorithmes de compression de données",
        "Je construis des PC pour le plaisir d'apprendre",
        "Je suis passionné par les nouvelles tendances en cybersécurité",
        "Je fais des expériences avec des gadgets IoT comme Raspberry Pi",
        "Je participe à des compétitions de hackathon sans m'y spécialiser",
        "J'explore les bases de la cryptographie pour mieux comprendre la blockchain",
    ]

    labels = [
        # SISR
        "SISR",
        "SISR",
        "SISR",
        "SISR",
        "SISR",
        "SISR",
        "SISR",
        "SISR",
        "SISR",
        "SISR",

        # SLAM
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",
        "SLAM",

        # Inconnu
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",
        "Inconnu",

        # SISR
        "SISR", "SISR", "SISR", "SISR", "SISR", "SISR", "SISR", "SISR", "SISR", "SISR", "SISR",

        # SLAM
        "SLAM", "SLAM", "SLAM", "SLAM", "SLAM", "SLAM", "SLAM", "SLAM", "SLAM", "SLAM", "SLAM",

        # Inconnu
        "Inconnu", "Inconnu", "Inconnu", "Inconnu", "Inconnu", "Inconnu", "Inconnu", "Inconnu", "Inconnu", "Inconnu",
        "Inconnu",

    ]

    evaluate_classifier(descriptions, labels)
