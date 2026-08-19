"""Módulo de palavras para o Jogo da Forca.

Contém as palavras organizadas por categoria, suporte a carregamento de `words.txt`
(no formato `categoria:palavra:dica` ou `palavra:dica`) e funções utilitárias para
normalização e salvamento de novas palavras.
"""

import random
from collections import defaultdict
import unicodedata
import os

# Palavras internas (fallback). Organizamos por categoria para facilitar manutenção.
PALAVRAS_BY_CATEGORY = {
    "frutas": [
        ("banana", "Fruta amarela rica em potassio"),
        ("abacaxi", "Fruta tropical com coroa"),
        ("morango", "Fruta vermelha pequena"),
        ("laranja", "Fruta cor de ouro"),
    ],
    "tecnologia": [
        ("computador", "Maquina eletronica de processar dados"),
        ("teclado", "Tem teclas A, B, C..."),
        ("monitor", "Tela do computador"),
    ],
    "animais": [
        ("elefante", "Maior animal terrestre"),
        ("girafa", "Animal mais alto do mundo"),
        ("cachorro", "Melhor amigo do homem"),
        ("papagaio", "Ave que repete o que voce fala"),
    ],
    "esportes": [
        ("futebol", "Esporte mais popular do Brasil"),
        ("basquete", "Esporte da bola laranja"),
        ("natacao", "Esporte praticado na agua"),
    ],
    "comida": [
        ("pizza", "Comida italiana redonda"),
        ("chocolate", "Doce feito de cacau"),
    ],
    "musica": [
        ("violao", "Instrumento de 6 cordas"),
    ],
    "jogos": [
        ("xadrez", "Jogo de estrategia com 64 casas"),
    ],
    "paises": [
        ("brasil", "Pais do futebol"),
        ("argentina", "Pais dos hermanos"),
    ],
}

# Flattened fallback list (all categories combined)
PALAVRAS = [p for cat in PALAVRAS_BY_CATEGORY.values() for p in cat]


def normalize_text(s: str) -> str:
    """Remove acentos e caracteres combinantes, retorna em minusculas.

    Ex.: 'coração' -> 'coracao', 'Ç' -> 'c'
    """
    if not isinstance(s, str):
        return s
    s = s.lower()
    nkfd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nkfd if not unicodedata.combining(c))


def carregar_palavras(caminho="words.txt"):
    """Carrega palavras de um arquivo `words.txt`.

    Formatos aceitos por linha:
      - categoria:palavra:dica
      - palavra:dica  (categoria será 'sem_categoria')

    Linhas em branco ou começando por # são ignoradas.
    Retorna um dicionário {categoria: [(palavra, dica), ...], ...}.
    """
    categorias = defaultdict(list)
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha or linha.startswith("#"):
                    continue
                parts = linha.split(":")
                if len(parts) >= 3:
                    categoria = parts[0].strip().lower()
                    palavra = parts[1].strip()
                    dica = ":".join(parts[2:]).strip()
                elif len(parts) == 2:
                    categoria = "sem_categoria"
                    palavra = parts[0].strip()
                    dica = parts[1].strip()
                else:
                    # linha com apenas a palavra
                    categoria = "sem_categoria"
                    palavra = parts[0].strip()
                    dica = ""

                if palavra:
                    categorias[categoria].append((palavra, dica))
    except FileNotFoundError:
        # Arquivo não existe; retornamos um dict vazio
        return {}
    return dict(categorias)


def categorias_disponiveis():
    """Retorna a lista de categorias disponíveis (inclui 'Todas')."""
    carglobal = set(PALAVRAS_BY_CATEGORY.keys())
    carregadas = set()
    carregadas_dict = carregar_palavras()
    if carregadas_dict:
        carregadas = set(carregadas_dict.keys())
    categorias = sorted(list(carglobal | carregadas))
    return ["Todas"] + categorias


def sortear_palavra(categoria=None):
    """Sorteia e retorna (palavra, dica) de acordo com a categoria escolhida.

    - Se `categoria` for None ou 'Todas', sorteia de todas as palavras (inclui as do words.txt se existir).
    - Se a categoria não existir, faz fallback para todas as palavras.
    """
    # Começa com as palavras internas
    por_categoria = {k: list(v) for k, v in PALAVRAS_BY_CATEGORY.items()}

    # Carrega words.txt e mescla (substitui/estende categorias carregadas)
    carregadas = carregar_palavras()
    for cat, lista in carregadas.items():
        if cat in por_categoria:
            por_categoria[cat].extend(lista)
        else:
            por_categoria[cat] = list(lista)

    # Construir lista conforme categoria
    if not categoria or categoria == "Todas":
        todas = []
        for lst in por_categoria.values():
            todas.extend(lst)
        if not todas:
            # fallback para PALAVRAS
            return random.choice(PALAVRAS)
        return random.choice(todas)

    cat = categoria.strip().lower()
    if cat not in por_categoria:
        # fallback para todas
        return sortear_palavra(None)

    lista = por_categoria[cat]
    if not lista:
        return sortear_palavra(None)
    return random.choice(lista)


def save_word(categoria, palavra, dica, caminho="words.txt"):
    """Adiciona uma nova palavra ao arquivo words.txt (apende).

    Retorna True se escrito com sucesso, False caso contrario.
    """
    if not palavra:
        return False
    categoria = (categoria or "sem_categoria").strip().lower()
    palavra = palavra.strip()
    dica = (dica or "").strip()

    linha = f"{categoria}:{palavra}:{dica}\n"
    try:
        # Garantir que o arquivo existe
        mode = "a"
        with open(caminho, mode, encoding="utf-8") as f:
            f.write(linha)
        return True
    except OSError:
        return False


def overwrite_words_file(categorias_dict, caminho="words.txt"):
    """Sobrescreve `words.txt` com o dicionário fornecido.

    categorias_dict deve ser {categoria: [(palavra,dica), ...], ...}
    Usa formato categoria:palavra:dica por linha.
    """
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            for cat, lista in categorias_dict.items():
                for palavra, dica in lista:
                    f.write(f"{cat}:{palavra}:{dica}\n")
        return True
    except OSError:
        return False
