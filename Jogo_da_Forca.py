"""Jogo da Forca - Versao GUI com Tkinter.

Interface grafica completa:
- Janela principal com a forca desenhada em Canvas
- 26 botoes de letras (A-Z) que desabilitam ao serem clicados
- Placar de erros, acertos e letras tentadas
- Janela de vitoria com trofeu animado e fogos
- Janela de derrota com a forca completa
- Botao para jogar novamente
"""

import random
import math
import tkinter as tk


# Cores
COR_FUNDO = "#1e293b"
COR_PAINEL = "#334155"
COR_TEXTO = "#f1f5f9"
COR_AZUL = "#3b82f6"
COR_VERDE = "#22c55e"
COR_VERMELHO = "#ef4444"
COR_AMARELO = "#eab308"
COR_CINZA = "#64748b"
COR_BRANCO = "#ffffff"
COR_OURO = "#facc15"


# ============================================================================
# BASE DE PALAVRAS (com dicas)
# ============================================================================
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
    """Sorteia uma palavra e sua dica."""
    return random.choice(PALAVRAS)


# ============================================================================
# CLASSE PRINCIPAL DO JOGO
# ============================================================================
class JogoForcaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.configure(bg=COR_FUNDO)
        self.root.resizable(False, False)

        # Estado do jogo
        self.palavra_secreta = ""
        self.dica = ""
        self.letras_acertadas = []
        self.letras_tentadas = set()
        self.erros = 0
        self.max_erros = 6
        self.jogo_ativo = False

        # Centralizar janela (aumentada para caber tudo)
        self.centralizar_janela(720, 820)

        # Construir interface
        self.criar_widgets()

        # Iniciar novo jogo
        self.novo_jogo()

    def centralizar_janela(self, w, h):
        """Centraliza a janela na tela."""
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
        # Titulo
        self.titulo = tk.Label(
            self.root, text="JOGO DA FORCA",
            font=("Segoe UI", 24, "bold"),
            bg=COR_FUNDO, fg=COR_OURO,
            pady=5
        )
        self.titulo.pack()

        # Frame da forca (canvas) - reduzido para dar mais espaco aos botoes
        self.frame_forca = tk.Frame(self.root, bg=COR_FUNDO)
        self.frame_forca.pack(pady=2)

        self.canvas = tk.Canvas(
            self.frame_forca, width=260, height=280,
            bg=COR_PAINEL, highlightthickness=0
        )
        self.canvas.pack()

        # Info: erros e dica
        self.frame_info = tk.Frame(self.root, bg=COR_FUNDO)
        self.frame_info.pack(pady=4, fill="x", padx=20)

        self.label_erros = tk.Label(
            self.frame_info, text="",
            font=("Segoe UI", 12, "bold"),
            bg=COR_FUNDO, fg=COR_VERMELHO
        )
        self.label_erros.pack(side="left")

        self.label_dica = tk.Label(
            self.frame_info, text="",
            font=("Segoe UI", 11, "italic"),
            bg=COR_FUNDO, fg=COR_TEXTO
        )
        self.label_dica.pack(side="right")

        # Palavra
        self.label_palavra = tk.Label(
            self.root, text="",
            font=("Consolas", 26, "bold"),
            bg=COR_FUNDO, fg=COR_BRANCO,
            pady=5
        )
        self.label_palavra.pack()

        # Letras tentadas
        self.label_tentadas = tk.Label(
            self.root, text="",
            font=("Segoe UI", 10),
            bg=COR_FUNDO, fg=COR_CINZA
        )
        self.label_tentadas.pack()

        # Frame dos botoes de letras - 13 colunas x 2 fileiras
        self.frame_botoes = tk.Frame(self.root, bg=COR_FUNDO)
        self.frame_botoes.pack(pady=10)

        self.botoes_letras = {}
        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, letra in enumerate(alfabeto):
            row = i // 13
            col = i % 13
            btn = tk.Button(
                self.frame_botoes, text=letra,
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

        # Botao novo jogo
        self.btn_novo = tk.Button(
            self.root, text="NOVO JOGO",
            font=("Segoe UI", 12, "bold"),
            bg=COR_VERDE, fg=COR_BRANCO,
            activebackground=COR_AMARELO,
            activeforeground=COR_FUNDO,
            relief="flat", borderwidth=0,
            cursor="hand2",
            padx=20, pady=8,
            command=self.novo_jogo
        )
        self.btn_novo.pack(pady=8)

    # -----------------------------------------------------------------
    # LOGICA DO JOGO
    # -----------------------------------------------------------------
    def novo_jogo(self):
        """Reinicia o jogo com uma nova palavra."""
        self.palavra_secreta, self.dica = sortear_palavra()
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
        else:
            # Errou!
            self.erros += 1
            btn.config(bg=COR_VERMELHO, state="disabled")

        self.atualizar_tela()
        self.verificar_fim_jogo()

    def atualizar_tela(self):
        """Atualiza todos os elementos visuais."""
        self.desenhar_forca()
        self.label_erros.config(text=f"Erros: {self.erros}/{self.max_erros}")
        self.label_dica.config(text=f"Dica: {self.dica}")
        self.label_palavra.config(text=" ".join(self.letras_acertadas))
        letras_ord = sorted(self.letras_tentadas)
        self.label_tentadas.config(
            text=f"Letras tentadas: {', '.join(letras_ord) if letras_ord else '-'}"
        )

    def verificar_fim_jogo(self):
        """Verifica se o jogo acabou e mostra a tela apropriada."""
        if "_" not in self.letras_acertadas:
            self.jogo_ativo = False
            self.desabilitar_botoes()
            self.root.after(400, self.mostrar_vitoria)
        elif self.erros >= self.max_erros:
            self.jogo_ativo = False
            self.desabilitar_botoes()
            # Revela a palavra
            for i, c in enumerate(self.palavra_secreta):
                self.letras_acertadas[i] = c
            self.label_palavra.config(text=" ".join(self.letras_acertadas))
            self.root.after(400, self.mostrar_derrota)

    def desabilitar_botoes(self):
        for btn in self.botoes_letras.values():
            btn.config(state="disabled")

    # -----------------------------------------------------------------
    # DESENHO DA FORCA NO CANVAS (260x280)
    # -----------------------------------------------------------------
    def desenhar_forca(self):
        """Desenha a forca com o numero de erros correspondente."""
        self.canvas.delete("all")

        # Cores
        madeira = "#92400e"
        corda = "#fef3c7"
        pessoa = "#1f2937"

        # Estrutura da forca (sempre visivel)
        # Base
        self.canvas.create_line(40, 250, 220, 250, fill=madeira, width=6)
        # Vertical
        self.canvas.create_line(70, 250, 70, 40, fill=madeira, width=6)
        # Horizontal
        self.canvas.create_line(70, 40, 170, 40, fill=madeira, width=6)
        # Suporte diagonal
        self.canvas.create_line(70, 75, 105, 40, fill=madeira, width=4)
        # Corda
        self.canvas.create_line(170, 40, 170, 75, fill=corda, width=3)

        # Boneco (aparece conforme erros)
        if self.erros >= 1:
            # Cabeca
            self.canvas.create_oval(150, 75, 190, 115, fill=pessoa, outline="#fbbf24", width=2)
        if self.erros >= 2:
            # Corpo
            self.canvas.create_line(170, 115, 170, 180, fill=pessoa, width=4)
        if self.erros >= 3:
            # Braco esquerdo
            self.canvas.create_line(170, 135, 140, 165, fill=pessoa, width=4)
        if self.erros >= 4:
            # Braco direito
            self.canvas.create_line(170, 135, 200, 165, fill=pessoa, width=4)
        if self.erros >= 5:
            # Perna esquerda
            self.canvas.create_line(170, 180, 140, 215, fill=pessoa, width=4)
        if self.erros >= 6:
            # Perna direita
            self.canvas.create_line(170, 180, 200, 215, fill=pessoa, width=4)
            # Olhos de X
            self.canvas.create_line(155, 85, 165, 95, fill="#ef4444", width=2)
            self.canvas.create_line(165, 85, 155, 95, fill="#ef4444", width=2)
            self.canvas.create_line(175, 85, 185, 95, fill="#ef4444", width=2)
            self.canvas.create_line(185, 85, 175, 95, fill="#ef4444", width=2)

        # Mensagem de status
        if self.erros == 0:
            self.canvas.create_text(130, 268, text="Voce tem 6 chances!",
                                     fill=COR_TEXTO, font=("Segoe UI", 9, "bold"))
        elif self.erros <= 3:
            self.canvas.create_text(130, 268, text="Cuidado!",
                                     fill=COR_AMARELO, font=("Segoe UI", 9, "bold"))
        elif self.erros < 6:
            self.canvas.create_text(130, 268, text="A forca esta chegando!",
                                     fill="#fb923c", font=("Segoe UI", 9, "bold"))
        else:
            self.canvas.create_text(130, 268, text="ENFORCADO!",
                                     fill=COR_VERMELHO, font=("Segoe UI", 11, "bold"))

    # -----------------------------------------------------------------
    # TELA DE VITORIA (com trofeu animado)
    # -----------------------------------------------------------------
    def mostrar_vitoria(self):
        """Abre a janela de vitoria com trofeu e fogos."""
        vitoria = tk.Toplevel(self.root)
        vitoria.title("VITORIA!")
        vitoria.configure(bg=COR_FUNDO)
        vitoria.resizable(False, False)
        vitoria.transient(self.root)
        vitoria.grab_set()

        # Centralizar
        vitoria.update_idletasks()
        w, h = 500, 580
        sw = vitoria.winfo_screenwidth()
        sh = vitoria.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        vitoria.geometry(f"{w}x{h}+{x}+{y}")

        # Canvas para o trofeu
        canvas = tk.Canvas(vitoria, width=500, height=400, bg=COR_FUNDO, highlightthickness=0)
        canvas.pack()

        # Animacao de fogos (estrelas piscando)
        self.fogos = []
        for _ in range(40):
            x = random.randint(20, 480)
            y = random.randint(20, 380)
            cor = random.choice(["#facc15", "#fb923c", "#ef4444", "#22c55e", "#3b82f6", "#a855f7"])
            tamanho = random.randint(3, 8)
            fogo = canvas.create_text(x, y, text="*", fill=cor, font=("Arial", tamanho, "bold"))
            self.fogos.append((fogo, cor))

        # Trofeu desenhado
        self.desenhar_trofeu(canvas)

        # Mensagem
        tk.Label(vitoria, text="PARABENS, VOCE GANHOU!",
                 font=("Segoe UI", 18, "bold"),
                 bg=COR_FUNDO, fg=COR_OURO).pack(pady=5)

        tk.Label(vitoria, text=f"A palavra era: {self.palavra_secreta.upper()}",
                 font=("Segoe UI", 12),
                 bg=COR_FUNDO, fg=COR_BRANCO).pack()

        tk.Label(vitoria, text=f"Erros cometidos: {self.erros}/{self.max_erros}",
                 font=("Segoe UI", 11),
                 bg=COR_FUNDO, fg=COR_VERDE).pack(pady=5)

        # Botao jogar novamente
        tk.Button(vitoria, text="JOGAR NOVAMENTE",
                  font=("Segoe UI", 12, "bold"),
                  bg=COR_VERDE, fg=COR_BRANCO,
                  activebackground=COR_AMARELO,
                  relief="flat", cursor="hand2",
                  padx=20, pady=8,
                  command=lambda: [vitoria.destroy(), self.novo_jogo()]).pack(pady=10)

        # Animar
        self.animar_fogos(canvas, 0)

    def desenhar_trofeu(self, canvas):
        """Desenha um trofeu estilizado no canvas."""
        # Base do trofeu
        canvas.create_rectangle(180, 320, 320, 360, fill="#92400e", outline="#78350f", width=2)
        canvas.create_rectangle(160, 340, 340, 370, fill="#a16207", outline="#78350f", width=2)

        # Cabo do trofeu
        canvas.create_rectangle(220, 280, 280, 320, fill="#facc15", outline="#ca8a04", width=2)

        # Copa do trofeu (corpo principal)
        canvas.create_polygon(170, 130, 330, 130, 310, 280, 190, 280,
                               fill="#facc15", outline="#ca8a04", width=3)

        # Brilho na copa
        canvas.create_polygon(180, 140, 220, 140, 200, 270, 190, 270,
                               fill="#fde68a", outline="")

        # Alcas laterais
        canvas.create_oval(120, 140, 175, 220, outline="#ca8a04", width=4)
        canvas.create_oval(130, 155, 165, 215, fill=COR_FUNDO, outline="")

        canvas.create_oval(325, 140, 380, 220, outline="#ca8a04", width=4)
        canvas.create_oval(335, 155, 370, 215, fill=COR_FUNDO, outline="")

        # Estrelas
        for x, y in [(195, 180), (305, 180), (250, 200)]:
            self.desenhar_estrela(canvas, x, y, 12, "#fde68a", "#facc15")

        # Texto "1o" no centro
        canvas.create_text(250, 220, text="1o", font=("Arial", 28, "bold"), fill="#92400e")

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

    def animar_fogos(self, canvas, frame):
        """Anima os fogos piscando."""
        for fogo_id, cor in self.fogos:
            # Troca a cor periodicamente
            nova_cor = random.choice(["#facc15", "#fb923c", "#ef4444", "#22c55e", "#3b82f6", "#a855f7", "#f472b6"])
            canvas.itemconfig(fogo_id, fill=nova_cor)
            # Move ligeiramente
            x, y = canvas.coords(fogo_id)
            canvas.move(fogo_id, random.randint(-2, 2), random.randint(-2, 2))

        # Continua animando enquanto a janela existe
        try:
            if canvas.winfo_exists():
                self.root.after(100, lambda: self.animar_fogos(canvas, frame + 1))
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
        w, h = 500, 400
        sw = derrota.winfo_screenwidth()
        sh = derrota.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        derrota.geometry(f"{w}x{h}+{x}+{y}")

        # Caveira ASCII art
        skull = """
            .ed$$$" ""$$$$be.
          -"           ^""**$$$e.
        ."                   '$$$c
       /                      "4$$b
      d  3                      $$$$
      $  *                   .d$$$$
     .$  ^c           $$$$$e$$$$$$$$
     d$L  4.         $$$$$$$$$$$$$$$
     $$$$b ^ceeeee.  $$$$$$$$$$$$$$$$
     $$$$P d$$$$F $ $$$$$$$$$$$$$$$$$
      3$$$F "$$$$b   $   $$$$$$P**$$.
      $$P"  ^$$$$    \\  d$$$$    \\  3
       \\        4    \\  d$$$      4 $
        \\              \\ d$$$$        \\
         -._.           \\  $$$$e       $
           \\           \\  $$$$F  ..  4
         4 $$$b          \\  $$P  d$$$ 4
             ^$$$$e       \\ d$P  .$$$P
               ^$$$$$c  ..  $$  .$$$$$
                  ^$$$$$$$$  d$$$$$
                     "$$$$$$$$$$P
                        "$$P"
        """
        tk.Label(derrota, text=skull, font=("Courier", 8),
                 bg=COR_FUNDO, fg=COR_VERMELHO, justify="center").pack(pady=10)

        tk.Label(derrota, text="VOCE FOI ENFORCADO!",
                 font=("Segoe UI", 20, "bold"),
                 bg=COR_FUNDO, fg=COR_VERMELHO).pack(pady=5)

        tk.Label(derrota, text=f"A palavra era: {self.palavra_secreta.upper()}",
                 font=("Segoe UI", 13, "bold"),
                 bg=COR_FUNDO, fg=COR_BRANCO).pack()

        tk.Label(derrota, text="Nao desanime, tente novamente!",
                 font=("Segoe UI", 10, "italic"),
                 bg=COR_FUNDO, fg=COR_CINZA).pack(pady=5)

        # Botao jogar novamente
        tk.Button(derrota, text="JOGAR NOVAMENTE",
                  font=("Segoe UI", 12, "bold"),
                  bg=COR_VERDE, fg=COR_BRANCO,
                  activebackground=COR_AMARELO,
                  relief="flat", cursor="hand2",
                  padx=20, pady=8,
                  command=lambda: [derrota.destroy(), self.novo_jogo()]).pack(pady=15)


# ============================================================================
# PONTO DE ENTRADA
# ============================================================================
def main():
    root = tk.Tk()
    app = JogoForcaGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
