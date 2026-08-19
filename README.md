# Jogo da Forca

Implementação em Python (GUI com Tkinter) do clássico jogo da forca. Este repositório contém o arquivo principal `Jogo_da_Forca.py` que abre uma interface gráfica completa para jogar.

## Sobre

O jogo seleciona uma palavra secreta (com dica) e o jogador tenta adivinhar letra a letra. A interface usa Tkinter e mostra a forca desenhada, botões com as letras, contagem de erros e telas de vitória/derrota.

## Requisitos

- Python 3.8+ (testado com 3.8/3.10/3.11)
- Tkinter (vem com a maioria das instalações do Python, em distribuições Linux pode ser necessário instalar o pacote do sistema `python3-tk`)
- Git (opcional, para clonar o repositório)

Observação: não há dependências externas em pip para esta versão — tudo roda com a biblioteca padrão.

## Instalação

1. Clone o repositório:

   git clone https://github.com/EmersonLopes2589/jogodaforca.git
   cd jogodaforca

2. (Opcional) Crie um ambiente virtual:

   python3 -m venv env
   source env/bin/activate    # macOS / Linux
   .\env\Scripts\activate   # Windows PowerShell

3. No Linux (se necessário), instale o Tkinter do sistema:

   # Debian / Ubuntu
   sudo apt update && sudo apt install python3-tk

4. Execute o jogo:

   python3 Jogo_da_Forca.py

No Windows normalmente basta executar `python Jogo_da_Forca.py` em um terminal.

## Como jogar

- A janela principal mostra a forca, dica e os botões com as letras (A–Z).
- Clique nas letras para chutar — letras corretas aparecem na palavra; letras incorretas aumentam o contador de erros.
- Você tem 6 tentativas por padrão (variável `max_erros` no código).
- Ao vencer, surge uma janela de vitória com animação; ao perder, surge a janela de derrota mostrando a palavra.

## Palavras e dicas (words.py)

As palavras e suas dicas foram extraídas para o módulo `words.py`.

- Local: `words.py` no diretório raiz do repositório.
- Formato: a variável `PALAVRAS` é uma lista de tuplas `("palavra", "dica")` em letras minúsculas.
- Para adicionar/editar palavras, abra e edite `words.py` diretamente.

Se preferir usar um arquivo de texto externo, você pode criar um `words.txt` no formato `palavra:dica` por linha (ou apenas `palavra` sem dica). Para carregar `words.txt` automaticamente, substitua a função `sortear_palavra()` em `words.py` por uma versão que leia o arquivo — por exemplo:

```python
# carregar words.txt no formato palavra:dica

def carregar_palavras(caminho="words.txt"):
    pares = []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha or linha.startswith("#"):
                    continue
                if ":" in linha:
                    p, d = linha.split(":", 1)
                    pares.append((p.strip().lower(), d.strip()))
                else:
                    pares.append((linha.strip().lower(), ""))
    except FileNotFoundError:
        pass
    return pares

# Exemplo de uso em sortear_palavra():
# palavras = carregar_palavras()
# if palavras:
#     return random.choice(palavras)
# return random.choice(PALAVRAS)  # fallback
```

## Estrutura do repositório

- Jogo_da_Forca.py — código-fonte principal (interface Tkinter e lógica do jogo)
- words.py — lista de palavras/dicas e função de sorteio
- README.md — este arquivo

## Como personalizar

- Lista de palavras/dicas: a base está em `words.py` (uma lista de tuplas `("palavra", "dica")`). Para adicionar ou alterar palavras, edite essa lista ou use um `words.txt` externo e adapte `words.py` como mostrado acima.

- Mudar número de tentativas: altere `self.max_erros` dentro da classe `JogoForcaGUI` (valor padrão: 6).

- Traduzir/alterar textos: procure strings no topo do arquivo `Jogo_da_Forca.py` e substitua conforme desejar.

## Observações e solução de problemas

- Erro "_tkinter: cannot open display" em sistemas headless: a interface gráfica precisa de um servidor X ou similar; em servidores remotos use forwarding X ou execute localmente.
- Se o Tkinter não for encontrado no Windows/Linux, instale o pacote do sistema (`python3-tk`) ou verifique a instalação do Python.

## Como contribuir

1. Faça um fork do repositório.
2. Crie uma branch com sua feature: `git checkout -b feature/nome-da-feature`.
3. Faça commits claros e abra um Pull Request.

Dicas de contribuição:
- Adicione uma opção para carregar palavras de um arquivo ou API.
- Separe a lógica do jogo da interface para facilitar testes unitários.

## Licença

Sugestão: MIT. Para adicionar: crie um arquivo `LICENSE` com o texto da licença MIT e adicione o cabeçalho apropriado nos arquivos, se desejar.

## Contato

Se quiser, eu posso:
- Gerar um `words.txt` com palavras de exemplo;
- Extrair a lista `PALAVRAS` para um arquivo externo e atualizar o código automaticamente;
- Adicionar testes unitários e separar a lógica da interface.

Diga qual dessas opções prefere que eu implemente e eu faço as alterações neste repositório e confirmo o commit com instruções de uso.
