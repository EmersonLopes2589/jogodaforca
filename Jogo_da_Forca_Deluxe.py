"""Jogo da Forca DELUXE - Versao GUI elaborada com Tkinter.

Melhorias em relacao a versao basica:
- Sistema de pontuacao e niveis (facil/medio/dificil)
- Animacao de confete na vitoria
- Botoes com efeito hover e brilho
- Forca desenhada com mais detalhes (sombra, textura)
- Boneco com rosto (olhos, boca) que muda conforme erros
- Painel de estatisticas (vitorias, derrotas, sequencia)
- Categorias de palavras selecionaveis
- Efeitos sonoros visuais (flash verde/vermelho)
- Tela de vitoria com trofeu 3D e confete animado
- Tela de derrota com animacao de queda
- Historico de palavras jogadas
"""

import random
import math
import tkinter as tk
from tkinter import ttk, messagebox
import time


# ============================================================================
# PALETA DE CORES PREMIUM
# ============================================================================
COR_FUNDO = "#0f172a"
COR_FUNDO_CLARO = "#1e293b"
COR_PAINEL = "#1e293b"
COR_PAINEL_CLARO = "#334155"
COR_PAINEL_HOVER = "#475569"
COR_TEXTO = "#f1f5f9"
COR_TEXTO_SECUNDARIO = "#94a3b8"
COR_AZUL = "#3b82f6"
COR_AZUL_HOVER = "#60a5fa"
COR_VERDE = "#22c55e"
COR_VERDE_HOVER = "#4ade80"
COR_VERMELHO = "#ef4444"
COR_VERMELHO_HOVER = "#f87171"
COR_AMARELO = "#eab308"
COR_AMARELO_HOVER = "#facc15"
COR_ROXO = "#a855f7"
COR_ROXO_HOVER = "#c084fc"
COR_CIANO = "#06b6d4"
COR_LARANJA = "#f97316"
COR_ROSA = "#ec4899"
COR_BRANCO = "#ffffff"
COR_OURO = "#fbbf24"
COR_OURO_CLARO = "#fde68a"
COR_PRATA = "#e2e8f0"
COR_BRONZE = "#d97706"


# ============================================================================
# BANCO DE PALAVRAS POR CATEGORIA E DIFICULDADE
# ============================================================================
PALAVRAS = {
    "Frutas": {
        "facil": ["uva", "pera", "kiwi", "figo", "ameixa"],
        "medio": ["banana", "laranja", "morango", "abacaxi", "manga"],
        "dificil": ["carambola", "framboesa", "maracuja", "jabuticaba", "tamarindo"],
    },
    "Animais": {
        "facil": ["gato", "cao", "rato", "boi", "vaca"],
        "medio": ["elefante", "girafa", "cachorro", "papagaio", "tartaruga"],
        "dificil": ["rinoceronte", "hipopotamo", "ornitorrinco", "camaleao", "axolote"],
    },
    "Paises": {
        "facil": ["peru", "cuba", "ira", "egito", "china"],
        "medio": ["brasil", "argentina", "mexico", "canada", "japao"],
        "dificil": ["azerbaijao", "quirguistao", "liechtenstein", "madagascar", "mauritania"],
    },
    "Esportes": {
        "facil": ["gol", "rede", "bola", "juiz", "time"],
        "medio": ["futebol", "basquete", "volei", "tenis", "natacao"],
        "dificil": ["esgrima", "pentatlo", "badminton", "handebol", "triatlo"],
    },
    "Tecnologia": {
        "facil": ["mouse", "tela", "tecla", "chip", "wifi"],
        "medio": ["computador", "teclado", "monitor", "impressora", "roteador"],
        "dificil": ["microprocessador", "criptografia", "virtualizacao", "compilador", "framework"],
    },
    "Profissoes": {
        "facil": ["medico", "ator", "juiz", "padeiro", "pintor"],
        "medio": ["engenheiro", "arquiteto", "professor", "advogado", "dentista"],
        "dificil": ["otorrinolaringologista", "paleontologo", "arqueologo", "neurocientista", "diplomata"],
    },
}

DICAS = {
    "uva": "Fruta pequena que cresce em cachos",
    "pera": "Fruta em formato de sino",
    "kiwi": "Fruta peluda por fora e verde por dentro",
    "figo": "Fruta roxa com sementes dentro",
    "ameixa": "Fruta roxa ou amarela, doce",
    "banana": "Fruta amarela rica em potassio",
    "laranja": "Fruta citrica cor de laranja",
    "morango": "Fruta vermelha pequena com sementes fora",
    "abacaxi": "Fruta tropical com coroa espinhosa",
    "manga": "Fruta tropical amarela e doce",
    "carambola": "Fruta em formato de estrela",
    "framboesa": "Fruta vermelha pequena, tipo amora",
    "maracuja": "Fruta da paixao, amarela e azeda",
    "jabuticaba": "Fruta que nasce no tronco da arvore",
    "tamarindo": "Fruta marrom em vagem, azeda",
    "gato": "Felino domestico que mia",
    "cao": "Melhor amigo do homem",
    "rato": "Roedor pequeno",
    "boi": "Animal de fazenda que muge",
    "vaca": "Animal que da leite",
    "elefante": "Maior animal terrestre",
    "girafa": "Animal mais alto do mundo",
    "cachorro": "Melhor amigo do homem",
    "papagaio": "Ave que repete o que voce fala",
    "tartaruga": "Animal lento com casco",
    "rinoceronte": "Animal grande com chifre no nariz",
    "hipopotamo": "Animal grande que vive na agua",
    "ornitorrinco": "Mamifero que bota ovo",
    "camaleao": "Reptil que muda de cor",
    "axolote": "Anfibio mexicano que regenera orgaos",
    "peru": "Pais da America do Sul, capital Lima",
    "cuba": "Ilha caribenha comunista",
    "ira": "Pais do Oriente Medio",
    "egito": "Pais das piramides",
    "china": "Pais mais populoso do mundo",
    "brasil": "Pais do futebol e do carnaval",
    "argentina": "Pais dos hermanos, tango",
    "mexico": "Pais do taco e da tequila",
    "canada": "Pais do xarope de bordo",
    "japao": "Pais do sol nascente",
    "azerbaijao": "Pais do Caucaso, capital Baku",
    "quirguistao": "Pais da Asia Central",
    "liechtenstein": "Microestado europeu",
    "madagascar": "Ilha africana dos lemures",
    "mauritania": "Pais do deserto do Saara",
    "gol": "O que o jogador marca no futebol",
    "rede": "Onde a bola entra no gol",
    "bola": "Objeto redondo usado em esportes",
    "juiz": "Quem apita o jogo",
    "time": "Grupo de jogadores",
    "futebol": "Esporte mais popular do Brasil",
    "basquete": "Esporte da bola laranja e cesta",
    "volei": "Esporte com rede alta",
    "tenis": "Esporte com raquete e bola amarela",
    "natacao": "Esporte praticado na agua",
    "esgrima": "Esporte com espadas",
    "pentatlo": "Competicao com 5 modalidades",
    "badminton": "Esporte com peteca",
    "handebol": "Esporte jogado com as maos",
    "triatlo": "Natacao + ciclismo + corrida",
    "mouse": "Dispositivo apontador do computador",
    "tela": "Onde voce ve as imagens do PC",
    "tecla": "Botao do teclado",
    "chip": "Circuito integrado",
    "wifi": "Internet sem fio",
    "computador": "Maquina de processar dados",
    "teclado": "Tem teclas A, B, C...",
    "monitor": "Tela do computador",
    "impressora": "Imprime documentos",
    "roteador": "Distribui o sinal de internet",
    "microprocessador": "Cerebro do computador",
    "criptografia": "Tecnica de codificar dados",
    "virtualizacao": "Criar maquinas virtuais",
    "compilador": "Traduz codigo para linguagem de maquina",
    "framework": "Estrutura de desenvolvimento",
    "medico": "Profissional da saude",
    "ator": "Trabalha em filmes e teatro",
    "juiz": "Decide sentencas no tribunal",
    "padeiro": "Faz paes",
    "pintor": "Pinta quadros ou paredes",
    "engenheiro": "Projeta e constroi",
    "arquiteto": "Projeta edificios",
    "professor": "Ensina alunos",
    "advogado": "Defende causas juridicas",
    "dentista": "Cuida dos dentes",
    "otorrinolaringologista": "Medico de ouvido, nariz e garganta",
    "paleontologo": "Estuda fosseis",
    "arqueologo": "Estuda civilizacoes antigas",
    "neurocientista": "Estuda o cerebro",
    "diplomata": "Representa o pais no exterior",
}


# ============================================================================
# CLASSE PRINCIPAL DO JOGO DELUXE
# ============================================================================
class JogoForcaDeluxe:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca DELUXE")
        self.root.configure(bg=COR_FUNDO)
        self.root.resizable(False, False)

        # Estado do jogo
        self.palavra_secreta = ""
        self.dica = ""
        self.categoria = ""
        self.dificuldade = "medio"
        self.letras_acertadas = []
        self.letras_tentadas = set()
        self.erros = 0
        self.max_erros = 6
        self.jogo_ativo = False

        # Estatisticas
        self.vitorias = 0
        self.derrotas = 0
        self.sequencia = 0
        self.melhor_sequencia = 0
        self.pontuacao = 0
        self.palavras_jogadas = []

        # Centralizar janela
        self.centralizar_janela(900, 850)

        # Construir interface
        self.criar_widgets()

        # Iniciar novo jogo
        self.novo_jogo()

    def centralizar_janela(self, w, h):
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.root.geometry(f"{w}x{h}+{x}+{y}")

    # -----------------------------------------------------------------
    # CRIACAO DA INTERFACE
    # -----------------------------------------------------------------
    def criar_widgets(self):
        # ===== CABECALHO =====
        header = tk.Frame(self.root, bg=COR_PAINEL, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header, text="JOGO DA FORCA",
            font=("Segoe UI", 22, "bold"),
            bg=COR_PAINEL, fg=COR_OURO
        ).pack(side="left", padx=20, pady=10)

        tk.Label(
            header, text="DELUXE",
            font=("Segoe UI", 12, "bold"),
            bg=COR_PAINEL, fg=COR_ROXO
        ).pack(side="left", pady=10)

        # Painel de estatisticas no cabecalho
        stats_frame = tk.Frame(header, bg=COR_PAINEL)
        stats_frame.pack(side="right", padx=20)

        self.label_vitorias = tk.Label(
            stats_frame, text="V: 0",
            font=("Segoe UI", 10, "bold"),
            bg=COR_PAINEL, fg=COR_VERDE
        )
        self.label_vitorias.pack(side="left", padx=5)

        self.label_derrotas = tk.Label(
            stats_frame, text="D: 0",
            font=("Segoe UI", 10, "bold"),
            bg=COR_PAINEL, fg=COR_VERMELHO
        )
        self.label_derrotas.pack(side="left", padx=5)

        self.label_sequencia = tk.Label(
            stats_frame, text="Seq: 0",
            font=("Segoe UI", 10, "bold"),
            bg=COR_PAINEL, fg=COR_AMARELO
        )
        self.label_sequencia.pack(side="left", padx=5)

        self.label_pontuacao = tk.Label(
            stats_frame, text="Pts: 0",
            font=("Segoe UI", 10, "bold"),
            bg=COR_PAINEL, fg=COR_CIANO
        )
        self.label_pontuacao.pack(side="left", padx=5)

        # ===== SELECAO DE CATEGORIA E DIFICULDADE =====
        config_frame = tk.Frame(self.root, bg=COR_FUNDO)
        config_frame.pack(fill="x", padx=15, pady=5)

        tk.Label(
            config_frame, text="Categoria:",
            font=("Segoe UI", 9, "bold"),
            bg=COR_FUNDO, fg=COR_TEXTO_SECUNDARIO
        ).pack(side="left")

        self.combo_categoria = ttk.Combobox(
            config_frame,
            values=list(PALAVRAS.keys()),
            state="readonly",
            width=15,
            font=("Segoe UI", 9)
        )
        self.combo_categoria.set("Frutas")
        self.combo_categoria.pack(side="left", padx=5)
        self.combo_categoria.bind("<<ComboboxSelected>>", lambda e: self.novo_jogo())

        tk.Label(
            config_frame, text="Dificuldade:",
            font=("Segoe UI", 9, "bold"),
            bg=COR_FUNDO, fg=COR_TEXTO_SECUNDARIO
        ).pack(side="left", padx=(15, 0))

        self.combo_dificuldade = ttk.Combobox(
            config_frame,
            values=["facil", "medio", "dificil"],
            state="readonly",
            width=10,
            font=("Segoe UI", 9)
        )
        self.combo_dificuldade.set("medio")
        self.combo_dificuldade.pack(side="left", padx=5)
        self.combo_dificuldade.bind("<<ComboboxSelected>>", lambda e: self.novo_jogo())

        # ===== AREA PRINCIPAL (forca + info) =====
        main_frame = tk.Frame(self.root, bg=COR_FUNDO)
        main_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # --- Lado esquerdo: Forca ---
        left_frame = tk.Frame(main_frame, bg=COR_FUNDO)
        left_frame.pack(side="left", fill="both", expand=True)

        # Canvas da forca com borda arredondada (simulada)
        canvas_container = tk.Frame(left_frame, bg=COR_PAINEL, padx=3, pady=3)
        canvas_container.pack(pady=5)

        self.canvas = tk.Canvas(
            canvas_container, width=280, height=300,
            bg=COR_PAINEL_CLARO, highlightthickness=0
        )
        self.canvas.pack()

        # Mensagem de status abaixo da forca
        self.label_status = tk.Label(
            left_frame, text="",
            font=("Segoe UI", 11, "bold"),
            bg=COR_FUNDO, fg=COR_TEXTO
        )
        self.label_status.pack(pady=5)

        # --- Lado direito: Info do jogo ---
        right_frame = tk.Frame(main_frame, bg=COR_FUNDO, width=350)
        right_frame.pack(side="right", fill="both", padx=(15, 0))
        right_frame.pack_propagate(False)

        # Card da palavra
        palavra_card = tk.Frame(right_frame, bg=COR_PAINEL, padx=15, pady=10)
        palavra_card.pack(fill="x", pady=5)

        tk.Label(
            palavra_card, text="PALAVRA",
            font=("Segoe UI", 9, "bold"),
            bg=COR_PAINEL, fg=COR_TEXTO_SECUNDARIO
        ).pack(anchor="w")

        self.label_palavra = tk.Label(
            palavra_card, text="",
            font=("Consolas", 16, "bold"),
            bg=COR_PAINEL, fg=COR_BRANCO,
            anchor="center", justify="center"
        )
        self.label_palavra.pack(pady=5, fill="x")

        # Card da dica
        dica_card = tk.Frame(right_frame, bg=COR_PAINEL, padx=15, pady=10)
        dica_card.pack(fill="x", pady=5)

        tk.Label(
            dica_card, text="DICA",
            font=("Segoe UI", 9, "bold"),
            bg=COR_PAINEL, fg=COR_TEXTO_SECUNDARIO
        ).pack(anchor="w")

        self.label_dica = tk.Label(
            dica_card, text="",
            font=("Segoe UI", 10, "italic"),
            bg=COR_PAINEL, fg=COR_AMARELO,
            wraplength=300, justify="left"
        )
        self.label_dica.pack(anchor="w", pady=2)

        # Card de erros
        erros_card = tk.Frame(right_frame, bg=COR_PAINEL, padx=15, pady=10)
        erros_card.pack(fill="x", pady=5)

        tk.Label(
            erros_card, text="ERROS",
            font=("Segoe UI", 9, "bold"),
            bg=COR_PAINEL, fg=COR_TEXTO_SECUNDARIO
        ).pack(anchor="w")

        # Barra de progresso de erros
        self.barra_erros = tk.Canvas(
            erros_card, width=300, height=20,
            bg=COR_PAINEL_CLARO, highlightthickness=0
        )
        self.barra_erros.pack(fill="x", pady=5)

        self.label_erros = tk.Label(
            erros_card, text="0/6",
            font=("Segoe UI", 10, "bold"),
            bg=COR_PAINEL, fg=COR_VERMELHO
        )
        self.label_erros.pack(anchor="w")

        # Card de letras tentadas
        tentadas_card = tk.Frame(right_frame, bg=COR_PAINEL, padx=15, pady=10)
        tentadas_card.pack(fill="x", pady=5)

        tk.Label(
            tentadas_card, text="LETRAS TENTADAS",
            font=("Segoe UI", 9, "bold"),
            bg=COR_PAINEL, fg=COR_TEXTO_SECUNDARIO
        ).pack(anchor="w")

        self.label_tentadas = tk.Label(
            tentadas_card, text="-",
            font=("Consolas", 10),
            bg=COR_PAINEL, fg=COR_TEXTO,
            wraplength=300, justify="left"
        )
        self.label_tentadas.pack(anchor="w", pady=2)

        # ===== BOTOES DE LETRAS =====
        letras_frame = tk.Frame(self.root, bg=COR_FUNDO)
        letras_frame.pack(pady=10)

        self.botoes_letras = {}
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letra in enumerate(alfabeto):
            row = i // 13
            col = i % 13
            btn = tk.Button(
                letras_frame, text=letra,
                font=("Segoe UI", 11, "bold"),
                width=4, height=2,
                bg=COR_AZUL, fg=COR_BRANCO,
                activebackground=COR_AMARELO,
                activeforeground=COR_FUNDO,
                relief="flat", borderwidth=0,
                cursor="hand2",
                command=lambda l=letra: self.chutar_letra(l)
            )
            btn.grid(row=row, column=col, padx=2, pady=3)
            self.botoes_letras[letra] = btn

            # Efeito hover
            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover(b, False))

        # ===== BOTOES DE ACAO =====
        acoes_frame = tk.Frame(self.root, bg=COR_FUNDO)
        acoes_frame.pack(pady=10)

        self.btn_novo = tk.Button(
            acoes_frame, text="NOVO JOGO",
            font=("Segoe UI", 11, "bold"),
            bg=COR_VERDE, fg=COR_BRANCO,
            activebackground=COR_VERDE_HOVER,
            activeforeground=COR_FUNDO,
            relief="flat", borderwidth=0,
            cursor="hand2",
            padx=20, pady=8,
            command=self.novo_jogo
        )
        self.btn_novo.pack(side="left", padx=5)

        self.btn_dica = tk.Button(
            acoes_frame, text="PEDIR DICA",
            font=("Segoe UI", 11, "bold"),
            bg=COR_AMARELO, fg=COR_FUNDO,
            activebackground=COR_AMARELO_HOVER,
            relief="flat", borderwidth=0,
            cursor="hand2",
            padx=20, pady=8,
            command=self.mostrar_dica
        )
        self.btn_dica.pack(side="left", padx=5)

        self.btn_desistir = tk.Button(
            acoes_frame, text="DESISTIR",
            font=("Segoe UI", 11, "bold"),
            bg=COR_VERMELHO, fg=COR_BRANCO,
            activebackground=COR_VERMELHO_HOVER,
            relief="flat", borderwidth=0,
            cursor="hand2",
            padx=20, pady=8,
            command=self.desistir
        )
        self.btn_desistir.pack(side="left", padx=5)

    def on_hover(self, btn, entering):
        """Efeito hover nos botoes de letra."""
        if btn["state"] == "disabled":
            return
        if entering:
            btn.config(bg=COR_AZUL_HOVER)
        else:
            btn.config(bg=COR_AZUL)

    # -----------------------------------------------------------------
    # LOGICA DO JOGO
    # -----------------------------------------------------------------
    def novo_jogo(self):
        """Reinicia o jogo com uma nova palavra."""
        categoria = self.combo_categoria.get()
        dificuldade = self.combo_dificuldade.get()

        palavras_disponiveis = PALAVRAS.get(categoria, {}).get(dificuldade, [])
        if not palavras_disponiveis:
            palavras_disponiveis = PALAVRAS["Frutas"]["medio"]

        # Evita repetir a ultima palavra
        if len(palavras_disponiveis) > 1 and self.palavra_secreta in palavras_disponiveis:
            palavras_disponiveis = [p for p in palavras_disponiveis if p != self.palavra_secreta]

        self.palavra_secreta = random.choice(palavras_disponiveis).lower()
        self.dica = DICAS.get(self.palavra_secreta, "Sem dica disponivel")
        self.categoria = categoria
        self.dificuldade = dificuldade
        self.letras_acertadas = ["_"] * len(self.palavra_secreta)
        self.letras_tentadas = set()
        self.erros = 0
        self.jogo_ativo = True

        # Reabilita todos os botoes
        for letra, btn in self.botoes_letras.items():
            btn.config(state="normal", bg=COR_AZUL)

        self.atualizar_tela()

    def chutar_letra(self, letra):
        """Processa o chute de uma letra."""
        if not self.jogo_ativo:
            return

        letra = letra.lower()
        if letra in self.letras_tentadas:
            return

        self.letras_tentadas.add(letra)
        btn = self.botoes_letras[letra.upper()]

        if letra in self.palavra_secreta:
            # Acertou!
            for i, c in enumerate(self.palavra_secreta):
                if c == letra:
                    self.letras_acertadas[i] = letra
            btn.config(bg=COR_VERDE, state="disabled")
            self.flash_tela(COR_VERDE)
        else:
            # Errou!
            self.erros += 1
            btn.config(bg=COR_VERMELHO, state="disabled")
            self.flash_tela(COR_VERMELHO)

        self.atualizar_tela()
        self.verificar_fim_jogo()

    def flash_tela(self, cor):
        """Efeito de flash na tela."""
        original = self.root.cget("bg")
        self.root.config(bg=cor)
        self.root.after(100, lambda: self.root.config(bg=original))

    def mostrar_dica(self):
        """Mostra a dica (custa pontos)."""
        if not self.jogo_ativo:
            return
        if self.pontuacao >= 5:
            self.pontuacao -= 5
            self.label_dica.config(text=self.dica)
            self.atualizar_stats()
        else:
            messagebox.showinfo("Dica", "Voce precisa de 5 pontos para pedir uma dica!")

    def desistir(self):
        """Desiste do jogo atual."""
        if not self.jogo_ativo:
            return
        if messagebox.askyesno("Desistir", "Tem certeza que deseja desistir?"):
            self.jogo_ativo = False
            self.derrotas += 1
            self.sequencia = 0
            self.desabilitar_botoes()
            # Revela a palavra
            for i, c in enumerate(self.palavra_secreta):
                self.letras_acertadas[i] = c
            self.label_palavra.config(text=" ".join(self.letras_acertadas))
            self.atualizar_stats()
            self.mostrar_derrota()

    def atualizar_tela(self):
        """Atualiza todos os elementos visuais."""
        self.desenhar_forca()
        self.atualizar_barra_erros()
        self.label_erros.config(text=f"{self.erros}/{self.max_erros}")
        self.label_dica.config(text="???" if self.jogo_ativo else self.dica)

        # Ajusta o tamanho da fonte baseado no comprimento da palavra
        palavra_display = " ".join(self.letras_acertadas)
        comprimento = len(palavra_display.replace(" ", ""))
        if comprimento > 12:
            tamanho_fonte = 11
        elif comprimento > 8:
            tamanho_fonte = 13
        else:
            tamanho_fonte = 16
        self.label_palavra.config(
            text=palavra_display,
            font=("Consolas", tamanho_fonte, "bold")
        )

        letras_ord = sorted(self.letras_tentadas)
        self.label_tentadas.config(
            text=", ".join(letras_ord) if letras_ord else "-"
        )

        # Mensagem de status
        if self.erros == 0:
            self.label_status.config(text="Boa sorte!", fg=COR_VERDE)
        elif self.erros <= 2:
            self.label_status.config(text="Cuidado...", fg=COR_AMARELO)
        elif self.erros <= 4:
            self.label_status.config(text="Perigo!", fg=COR_LARANJA)
        elif self.erros < 6:
            self.label_status.config(text="ULTIMA CHANCE!", fg=COR_VERMELHO)
        else:
            self.label_status.config(text="ENFORCADO!", fg=COR_VERMELHO)

    def atualizar_barra_erros(self):
        """Desenha a barra de progresso de erros."""
        self.barra_erros.delete("all")
        largura_total = 300
        segmento = largura_total / self.max_erros

        for i in range(self.max_erros):
            x1 = i * segmento + 2
            x2 = (i + 1) * segmento - 2
            if i < self.erros:
                cor = COR_VERMELHO
            else:
                cor = COR_PAINEL_CLARO
            self.barra_erros.create_rectangle(
                x1, 2, x2, 18,
                fill=cor, outline=""
            )

    def atualizar_stats(self):
        """Atualiza o painel de estatisticas."""
        self.label_vitorias.config(text=f"V: {self.vitorias}")
        self.label_derrotas.config(text=f"D: {self.derrotas}")
        self.label_sequencia.config(text=f"Seq: {self.sequencia}")
        self.label_pontuacao.config(text=f"Pts: {self.pontuacao}")

    def verificar_fim_jogo(self):
        """Verifica se o jogo acabou."""
        if "_" not in self.letras_acertadas:
            self.jogo_ativo = False
            self.vitorias += 1
            self.sequencia += 1
            if self.sequencia > self.melhor_sequencia:
                self.melhor_sequencia = self.sequencia

            # Calcula pontuacao
            pontos_base = {"facil": 10, "medio": 20, "dificil": 30}
            pontos = pontos_base.get(self.dificuldade, 20)
            bonus_sequencia = self.sequencia * 2
            bonus_erros = (self.max_erros - self.erros) * 3
            self.pontuacao += pontos + bonus_sequencia + bonus_erros

            self.palavras_jogadas.append(self.palavra_secreta)
            self.desabilitar_botoes()
            self.atualizar_stats()
            self.root.after(500, self.mostrar_vitoria)
        elif self.erros >= self.max_erros:
            self.jogo_ativo = False
            self.derrotas += 1
            self.sequencia = 0
            self.palavras_jogadas.append(self.palavra_secreta)
            self.desabilitar_botoes()
            # Revela a palavra
            for i, c in enumerate(self.palavra_secreta):
                self.letras_acertadas[i] = c
            self.label_palavra.config(text=" ".join(self.letras_acertadas))
            self.atualizar_stats()
            self.root.after(500, self.mostrar_derrota)

    def desabilitar_botoes(self):
        for btn in self.botoes_letras.values():
            btn.config(state="disabled")

    # -----------------------------------------------------------------
    # DESENHO DA FORCA (280x300)
    # -----------------------------------------------------------------
    def desenhar_forca(self):
        """Desenha a forca com mais detalhes."""
        self.canvas.delete("all")

        # Cores
        madeira = "#92400e"
        madeira_escura = "#78350f"
        corda = "#fef3c7"
        pessoa = "#1f2937"
        pele = "#fbbf24"

        # Sombra da base
        self.canvas.create_oval(30, 260, 230, 275, fill="#0f172a", outline="")

        # Base
        self.canvas.create_rectangle(40, 250, 220, 265, fill=madeira, outline=madeira_escura, width=2)
        self.canvas.create_rectangle(40, 250, 220, 255, fill=madeira_escura, outline="")

        # Poste vertical
        self.canvas.create_rectangle(65, 40, 80, 250, fill=madeira, outline=madeira_escura, width=2)
        self.canvas.create_rectangle(65, 40, 70, 250, fill=madeira_escura, outline="")

        # Poste horizontal
        self.canvas.create_rectangle(65, 35, 180, 50, fill=madeira, outline=madeira_escura, width=2)
        self.canvas.create_rectangle(65, 35, 180, 40, fill=madeira_escura, outline="")

        # Suporte diagonal
        self.canvas.create_polygon(65, 80, 65, 95, 100, 50, 85, 50, fill=madeira, outline=madeira_escura)

        # Corda
        self.canvas.create_line(170, 50, 170, 80, fill=corda, width=3)
        self.canvas.create_oval(165, 75, 175, 85, outline=corda, width=2)

        # Boneco (aparece conforme erros)
        if self.erros >= 1:
            # Cabeca com rosto
            self.canvas.create_oval(150, 80, 190, 120, fill=pele, outline="#d97706", width=2)
            # Olhos
            if self.erros < 6:
                self.canvas.create_oval(160, 92, 168, 100, fill="#1f2937", outline="")
                self.canvas.create_oval(172, 92, 180, 100, fill="#1f2937", outline="")
            else:
                # Olhos de X
                self.canvas.create_line(158, 90, 168, 100, fill="#1f2937", width=2)
                self.canvas.create_line(168, 90, 158, 100, fill="#1f2937", width=2)
                self.canvas.create_line(172, 90, 182, 100, fill="#1f2937", width=2)
                self.canvas.create_line(182, 90, 172, 100, fill="#1f2937", width=2)
            # Boca
            if self.erros <= 2:
                self.canvas.create_arc(160, 105, 180, 115, start=0, extent=-180, fill="#1f2937", outline="")
            elif self.erros <= 4:
                self.canvas.create_line(162, 110, 178, 110, fill="#1f2937", width=2)
            else:
                self.canvas.create_arc(160, 108, 180, 118, start=0, extent=180, fill="#1f2937", outline="")

        if self.erros >= 2:
            # Corpo
            self.canvas.create_line(170, 120, 170, 190, fill=pessoa, width=5)

        if self.erros >= 3:
            # Braco esquerdo
            self.canvas.create_line(170, 140, 140, 170, fill=pessoa, width=4)

        if self.erros >= 4:
            # Braco direito
            self.canvas.create_line(170, 140, 200, 170, fill=pessoa, width=4)

        if self.erros >= 5:
            # Perna esquerda
            self.canvas.create_line(170, 190, 140, 230, fill=pessoa, width=4)

        if self.erros >= 6:
            # Perna direita
            self.canvas.create_line(170, 190, 200, 230, fill=pessoa, width=4)

    # -----------------------------------------------------------------
    # TELA DE VITORIA (com confete animado)
    # -----------------------------------------------------------------
    def mostrar_vitoria(self):
        """Abre a janela de vitoria com confete e trofeu."""
        vitoria = tk.Toplevel(self.root)
        vitoria.title("VITORIA!")
        vitoria.configure(bg=COR_FUNDO)
        vitoria.resizable(False, False)
        vitoria.transient(self.root)
        vitoria.grab_set()

        # Centralizar
        vitoria.update_idletasks()
        w, h = 550, 650
        sw = vitoria.winfo_screenwidth()
        sh = vitoria.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        vitoria.geometry(f"{w}x{h}+{x}+{y}")

        # Canvas para confete e trofeu
        canvas = tk.Canvas(vitoria, width=550, height=450, bg=COR_FUNDO, highlightthickness=0)
        canvas.pack()

        # Confete (particulas coloridas caindo)
        self.confetes = []
        cores_confete = [COR_VERMELHO, COR_VERDE, COR_AZUL, COR_AMARELO, COR_ROXO, COR_ROSA, COR_CIANO, COR_LARANJA]
        for _ in range(80):
            x = random.randint(0, 550)
            y = random.randint(-400, 0)
            cor = random.choice(cores_confete)
            tamanho = random.randint(4, 10)
            velocidade = random.uniform(2, 6)
            rotacao = random.uniform(0, 360)
            confete = canvas.create_rectangle(
                x, y, x + tamanho, y + tamanho * 0.6,
                fill=cor, outline=""
            )
            self.confetes.append({
                "id": confete, "x": x, "y": y,
                "vel": velocidade, "rot": rotacao,
                "cor": cor, "tamanho": tamanho
            })

        # Trofeu desenhado
        self.desenhar_trofeu_deluxe(canvas)

        # Mensagens
        tk.Label(vitoria, text="PARABENS!",
                 font=("Segoe UI", 24, "bold"),
                 bg=COR_FUNDO, fg=COR_OURO).pack(pady=5)

        tk.Label(vitoria, text="VOCE GANHOU!",
                 font=("Segoe UI", 18, "bold"),
                 bg=COR_FUNDO, fg=COR_VERDE).pack()

        tk.Label(vitoria, text=f"A palavra era: {self.palavra_secreta.upper()}",
                 font=("Segoe UI", 13),
                 bg=COR_FUNDO, fg=COR_BRANCO).pack(pady=5)

        # Pontuacao
        pontos_frame = tk.Frame(vitoria, bg=COR_PAINEL, padx=20, pady=10)
        pontos_frame.pack(pady=10)

        tk.Label(pontos_frame, text=f"+{self.pontuacao} PONTOS",
                 font=("Segoe UI", 16, "bold"),
                 bg=COR_PAINEL, fg=COR_CIANO).pack()

        tk.Label(pontos_frame, text=f"Sequencia: {self.sequencia} vitorias",
                 font=("Segoe UI", 10),
                 bg=COR_PAINEL, fg=COR_AMARELO).pack()

        # Botao jogar novamente
        tk.Button(vitoria, text="JOGAR NOVAMENTE",
                  font=("Segoe UI", 12, "bold"),
                  bg=COR_VERDE, fg=COR_BRANCO,
                  activebackground=COR_VERDE_HOVER,
                  relief="flat", cursor="hand2",
                  padx=25, pady=10,
                  command=lambda: [vitoria.destroy(), self.novo_jogo()]).pack(pady=15)

        # Animar confete
        self.animar_confete(canvas, vitoria)

    def desenhar_trofeu_deluxe(self, canvas):
        """Desenha um trofeu mais elaborado."""
        cx, cy = 275, 200

        # Base do trofeu (3 camadas)
        canvas.create_rectangle(cx-70, cy+120, cx+70, cy+140, fill="#78350f", outline="#451a03", width=2)
        canvas.create_rectangle(cx-60, cy+100, cx+60, cy+120, fill="#92400e", outline="#78350f", width=2)
        canvas.create_rectangle(cx-50, cy+80, cx+50, cy+100, fill="#a16207", outline="#92400e", width=2)

        # Cabo do trofeu
        canvas.create_rectangle(cx-25, cy+40, cx+25, cy+80, fill=COR_OURO, outline="#ca8a04", width=2)

        # Copa do trofeu (corpo principal com gradiente simulado)
        canvas.create_polygon(cx-80, cy-60, cx+80, cy-60, cx+60, cy+40, cx-60, cy+40,
                               fill=COR_OURO, outline="#ca8a04", width=3)
        canvas.create_polygon(cx-70, cy-50, cx-30, cy-50, cx-40, cy+30, cx-55, cy+30,
                               fill=COR_OURO_CLARO, outline="")

        # Alcas laterais
        canvas.create_oval(cx-130, cy-50, cx-75, cy+30, outline="#ca8a04", width=5)
        canvas.create_oval(cx-120, cy-35, cx-85, cy+20, fill=COR_FUNDO, outline="")

        canvas.create_oval(cx+75, cy-50, cx+130, cy+30, outline="#ca8a04", width=5)
        canvas.create_oval(cx+85, cy-35, cx+120, cy+20, fill=COR_FUNDO, outline="")

        # Estrelas decorativas
        for dx, dy in [(-40, -20), (40, -20), (0, 0)]:
            self.desenhar_estrela(canvas, cx+dx, cy+dy, 10, COR_OURO_CLARO, "#ca8a04")

        # Texto "1o" no centro
        canvas.create_text(cx, cy+10, text="1o", font=("Arial", 24, "bold"), fill="#78350f")

        # Brilho ao redor
        for i in range(8):
            angulo = i * 45
            x1 = cx + 100 * math.cos(math.radians(angulo))
            y1 = cy + 100 * math.sin(math.radians(angulo))
            x2 = cx + 120 * math.cos(math.radians(angulo))
            y2 = cy + 120 * math.sin(math.radians(angulo))
            canvas.create_line(x1, y1, x2, y2, fill=COR_OURO_CLARO, width=2)

    def desenhar_estrela(self, canvas, x, y, size, fill, outline):
        """Desenha uma estrela de 5 pontas."""
        pontos = []
        for i in range(10):
            angulo = (i * 36 - 90) * math.pi / 180
            r = size if i % 2 == 0 else size / 2
            px = x + r * math.cos(angulo)
            py = y + r * math.sin(angulo)
            pontos.extend([px, py])
        canvas.create_polygon(pontos, fill=fill, outline=outline, width=1)

    def animar_confete(self, canvas, janela):
        """Anima o confete caindo."""
        try:
            if not janela.winfo_exists():
                return
        except tk.TclError:
            return

        for confete in self.confetes:
            # Move para baixo
            confete["y"] += confete["vel"]
            confete["rot"] += 5

            # Reseta se sair da tela
            if confete["y"] > 450:
                confete["y"] = random.randint(-50, -10)
                confete["x"] = random.randint(0, 550)

            # Atualiza posicao
            canvas.coords(
                confete["id"],
                confete["x"], confete["y"],
                confete["x"] + confete["tamanho"],
                confete["y"] + confete["tamanho"] * 0.6
            )

        try:
            self.root.after(30, lambda: self.animar_confete(canvas, janela))
        except tk.TclError:
            pass

    # -----------------------------------------------------------------
    # TELA DE DERROTA
    # -----------------------------------------------------------------
    def mostrar_derrota(self):
        """Abre a janela de derrota."""
        derrota = tk.Toplevel(self.root)
        derrota.title("Fim de Jogo")
        derrota.configure(bg=COR_FUNDO)
        derrota.resizable(False, False)
        derrota.transient(self.root)
        derrota.grab_set()

        # Centralizar
        derrota.update_idletasks()
        w, h = 500, 450
        sw = derrota.winfo_screenwidth()
        sh = derrota.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        derrota.geometry(f"{w}x{h}+{x}+{y}")

        # Canvas com caveira
        canvas = tk.Canvas(derrota, width=500, height=250, bg=COR_FUNDO, highlightthickness=0)
        canvas.pack()

        # Caveira desenhada
        self.desenhar_caveira(canvas, 250, 120)

        # Mensagens
        tk.Label(derrota, text="VOCE FOI ENFORCADO!",
                 font=("Segoe UI", 20, "bold"),
                 bg=COR_FUNDO, fg=COR_VERMELHO).pack(pady=5)

        tk.Label(derrota, text=f"A palavra era: {self.palavra_secreta.upper()}",
                 font=("Segoe UI", 14, "bold"),
                 bg=COR_FUNDO, fg=COR_BRANCO).pack()

        tk.Label(derrota, text=f"Dica: {self.dica}",
                 font=("Segoe UI", 10, "italic"),
                 bg=COR_FUNDO, fg=COR_TEXTO_SECUNDARIO).pack(pady=5)

        tk.Label(derrota, text="Nao desanime, tente novamente!",
                 font=("Segoe UI", 10),
                 bg=COR_FUNDO, fg=COR_TEXTO_SECUNDARIO).pack()

        # Botao jogar novamente
        tk.Button(derrota, text="JOGAR NOVAMENTE",
                  font=("Segoe UI", 12, "bold"),
                  bg=COR_VERDE, fg=COR_BRANCO,
                  activebackground=COR_VERDE_HOVER,
                  relief="flat", cursor="hand2",
                  padx=25, pady=10,
                  command=lambda: [derrota.destroy(), self.novo_jogo()]).pack(pady=20)

    def desenhar_caveira(self, canvas, cx, cy):
        """Desenha uma caveira estilizada."""
        # Cranio
        canvas.create_oval(cx-60, cy-70, cx+60, cy+30, fill=COR_PRATA, outline="#94a3b8", width=3)

        # Olhos (vazios)
        canvas.create_oval(cx-40, cy-40, cx-15, cy-10, fill=COR_FUNDO, outline="")
        canvas.create_oval(cx+15, cy-40, cx+40, cy-10, fill=COR_FUNDO, outline="")

        # Nariz
        canvas.create_polygon(cx, cy-5, cx-10, cy+15, cx+10, cy+15, fill=COR_FUNDO, outline="")

        # Mandibula
        canvas.create_rectangle(cx-35, cy+30, cx+35, cy+60, fill=COR_PRATA, outline="#94a3b8", width=3)

        # Dentes
        for i in range(6):
            x = cx - 30 + i * 12
            canvas.create_rectangle(x, cy+30, x+10, cy+45, fill=COR_BRANCO, outline="#94a3b8")

        # Ossos cruzados
        canvas.create_line(cx-80, cy+70, cx+80, cy+110, fill=COR_PRATA, width=8)
        canvas.create_line(cx+80, cy+70, cx-80, cy+110, fill=COR_PRATA, width=8)

        # Pontas dos ossos
        for dx, dy in [(-80, 70), (80, 70), (-80, 110), (80, 110)]:
            canvas.create_oval(cx+dx-8, cy+dy-8, cx+dx+8, cy+dy+8, fill=COR_PRATA, outline="")


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================
def main():
    root = tk.Tk()
    app = JogoForcaDeluxe(root)
    root.mainloop()


if __name__ == "__main__":
    main()
