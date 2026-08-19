"""Módulo de palavras para o Jogo da Forca.

Contém a lista PALAVRAS (palavra, dica) e a função sortear_palavra().
"""

import random

PALAVRAS = [
    ("banana", "Fruta amarela rica em potassio"),
    ("abacaxi", "Fruta tropical com coroa"),
    ("morango", "Fruta vermelha pequena"),
    ("laranja", "Fruta cor de ouro"),
    ("computador", "Maquina eletronica de processar dados"),
    ("teclado", "Tem teclas A, B, C..."),
    ("monitor", "Tela do computador"),
    ("elefante", "Maior animal terrestre"),
    ("girafa", "Animal mais alto do mundo"),
    ("cachorro", "Melhor amigo do homem"),
    ("papagaio", "Ave que repete o que voce fala"),
    ("brasil", "Pais do futebol"),
    ("argentina", "Pais dos hermanos"),
    ("futebol", "Esporte mais popular do Brasil"),
    ("basquete", "Esporte da bola laranja"),
    ("natacao", "Esporte praticado na agua"),
    ("xadrez", "Jogo de estrategia com 64 casas"),
    ("pizza", "Comida italiana redonda"),
    ("chocolate", "Doce feito de cacau"),
    ("violao", "Instrumento de 6 cordas"),
]


def sortear_palavra():
    """Retorna uma tupla (palavra, dica) escolhida aleatoriamente."""
    return random.choice(PALAVRAS)
