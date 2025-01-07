def run_questionnaire():
    print("Bienvenue dans l’orienteur BTS SIO !")
    print("Veuillez répondre aux questions suivantes :\n")

    questions = [
        {
            "text": "Aimez-vous travailler sur des serveurs (oui/non) ?",
            "sisr_points": 2,
            "slam_points": 0
        },
        {
            "text": "Aimez-vous développer des applications (oui/non) ?",
            "sisr_points": 0,
            "slam_points": 2
        },
        {
            "text": "Vous intéressez-vous à la maintenance réseau (oui/non) ?",
            "sisr_points": 2,
            "slam_points": 0
        },
        {
            "text": "Êtes-vous passionné par l’algorithmique et la programmation (oui/non) ?",
            "sisr_points": 0,
            "slam_points": 2
        }
    ]

    sisr_score = 0
    slam_score = 0

    for q in questions:
        answer = input(q["text"] + " ")
        if answer.lower() in ["oui", "o"]:
            sisr_score += q["sisr_points"]
            slam_score += q["slam_points"]
        # Si la réponse est "non", on n’ajoute rien

    # Décision finale
    if sisr_score > slam_score:
        print("\nVous semblez être plus orienté(e) vers la spécialité SISR.")
    elif slam_score > sisr_score:
        print("\nVous semblez être plus orienté(e) vers la spécialité SLAM.")
    else:
        print("\nImpossible de déterminer clairement une orientation. Essayez-en une autre ?")
