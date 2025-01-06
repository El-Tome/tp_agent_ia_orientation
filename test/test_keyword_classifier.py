import pytest
from src.keyword_classifier import classify_description

def test_classify_description_sisr():
    # Description contenant des mots-clés SISR
    desc = "Je travaille sur un serveur et je fais de la virtualisation."
    assert classify_description(desc) == "SISR"

def test_classify_description_slam():
    # Description contenant des mots-clés SLAM
    desc = "Je développe une application et gère la base de données."
    assert classify_description(desc) == "SLAM"

def test_classify_description_inconnu():
    # Description ne contenant pas de mots-clés
    desc = "J'aime la technologie et l'informatique en général."
    assert classify_description(desc) == "Inconnu"
