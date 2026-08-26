# 🎮 Jogo da Forca

Implementação em Python com GUI em Tkinter do clássico jogo da forca com **duas versões distintas**.

---

## 📋 Versões Disponíveis

### 1️⃣ **Jogo_da_Forca.py** — Versão Clássica
Uma versão limpa e objetiva do jogo da forca com interface simples e direta.

**Características:**
- Interface gráfica com Tkinter
- 26 botões interativos (letras A–Z)
- Desenho da forca progressivo (6 etapas de erros)
- Exibição de dica da palavra
- Contador de erros e letras tentadas
- Tela de vitória com trofeu animado e fogos
- Tela de derrota com caveira ASCII art
- Botão "Novo Jogo" para reiniciar

**Para executar:**
```bash
python3 Jogo_da_Forca.py
```

---

### 2️⃣ **Jogo_da_Forca_Deluxe.py** — Versão Premium
Uma versão elaborada com recursos avançados, sistema de pontuação e múltiplos níveis.

**Características (Deluxe):**
- ✨ **Sistema de pontuação** com bônus por sequência e acertos
- 🎯 **3 níveis de dificuldade**: Fácil, Médio e Difícil
- 📂 **6 categorias de palavras**: Frutas, Animais, Países, Esportes, Tecnologia, Profissões
- 🎨 **Efeitos visuais avançados**:
  - Botões com efeito hover
  - Flash de tela (verde/vermelho) ao acertar/errar
  - Barra de progresso de erros
  - Forca com detalhes gráficos e sombra
  - Boneco com rosto expressivo (olhos, boca que mudam com erros)
- 📊 **Painel de estatísticas** (vitórias, derrotas, sequência, pontos)
- 🎊 **Confete animado** na vitória
- 🏴 **Caveira desenhada** na derrota (em vez de ASCII art)
- 💡 **Botão "Pedir Dica"** (custa 5 pontos)
- 🚫 **Botão "Desistir"** com confirmação
- 📜 **Histórico de palavras jogadas**
- 🎯 **Seleção de categoria e dificuldade** em tempo real

**Para executar:**
```bash
python3 Jogo_da_Forca_Deluxe.py
```

---

## 📋 Comparação Rápida

| Recurso | Clássica | Deluxe |
|---------|----------|--------|
| Interface básica | ✅ | ✅ |
| Sistema de pontuação | ❌ | ✅ |
| Níveis de dificuldade | ❌ | ✅ |
| Categorias | ❌ | ✅ (6) |
| Efeitos visuais | 🔹 Básicos | 🔸 Avançados |
| Estatísticas | ❌ | ✅ |
| Confete animado | ❌ | ✅ |
| Pedir dica | ❌ | ✅ |
| Desistir | ❌ | ✅ |

---

## 🔧 Requisitos

- **Python 3.8+** (testado com 3.8, 3.10, 3.11)
- **Tkinter** (vem com a maioria das instalações do Python)
  - No Linux (Debian/Ubuntu): `sudo apt install python3-tk`
- **Git** (opcional, para clonar o repositório)

⚠️ **Nota:** Não há dependências externas em pip — ambas as versões usam apenas a biblioteca padrão.

---

## 📥 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/EmersonLopes2589/jogodaforca.git
   cd jogodaforca
   ```

2. (Opcional) Crie um ambiente virtual:
   ```bash
   python3 -m venv env
   source env/bin/activate          # macOS / Linux
   .\env\Scripts\activate           # Windows
   ```

3. No Linux, se necessário, instale Tkinter do sistema:
   ```bash
   # Debian / Ubuntu
   sudo apt update && sudo apt install python3-tk
   ```

4. Execute a versão desejada:
   ```bash
   # Versão clássica
   python3 Jogo_da_Forca.py
   
   # Versão Deluxe
   python3 Jogo_da_Forca_Deluxe.py
   ```

No Windows, normalmente basta executar `python Jogo_da_Forca.py` ou `python Jogo_da_Forca_Deluxe.py` em um terminal.

---

## 🎮 Como Jogar

### Versão Clássica
- Clique nas letras (A–Z) para chutar
- Letras corretas aparecem na palavra
- Letras incorretas aumentam o contador de erros
- Você tem **6 tentativas** por padrão
- Ganhe revelando toda a palavra ou perca com 6 erros

### Versão Deluxe
- Selecione uma **categoria** e **dificuldade** antes de começar
- Clique nas letras (A–Z) para chutar
- **Ganhe pontos** por acertos, bônus de sequência e redução de erros
- Use o botão **"Pedir Dica"** por 5 pontos (se tiver pontos disponíveis)
- Use o botão **"Desistir"** para abandonar a rodada
- Acompanhe suas **estatísticas** no painel superior
- Mude a dificuldade/categoria a qualquer momento para novo jogo

---

## 📁 Estrutura do Repositório

```
jogodaforca/
├── Jogo_da_Forca.py              # Versão clássica
├── Jogo_da_Forca_Deluxe.py       # Versão premium com recursos avançados
├── words.py                       # Lista de palavras e dicas (usado pela versão clássica)
├── words.txt                      # Palavras em formato texto (opcional)
└── README.md                      # Este arquivo
```

---

## 🎨 Personalizando

### Versão Clássica

- **Adicionar palavras:** Edite o arquivo `words.py` — é uma lista de tuplas `("palavra", "dica")`
- **Mudar número de tentativas:** Altere `self.max_erros` dentro da classe `JogoForcaGUI` (padrão: 6)
- **Traduzir/alterar textos:** Procure strings no arquivo `Jogo_da_Forca.py` e substitua conforme desejar
- **Usar arquivo externo:** Implemente a função `carregar_palavras()` para ler de `words.txt`

### Versão Deluxe

- **Adicionar palavras:** Edite o dicionário `PALAVRAS` dentro do arquivo `Jogo_da_Forca_Deluxe.py`
  - Estrutura: `PALAVRAS["Categoria"]["dificuldade"] = ["palavra1", "palavra2", ...]`
- **Adicionar dicas:** Edite o dicionário `DICAS` (chave: palavra, valor: dica)
- **Criar nova categoria:** Adicione uma chave em `PALAVRAS` com palavras por dificuldade
- **Ajustar sistema de pontuação:** Modifique os valores em `pontos_base` dentro de `verificar_fim_jogo()`
- **Alterar paleta de cores:** Procure as constantes `COR_*` no topo do arquivo

---

## 🐛 Solução de Problemas

### "Erro: _tkinter: cannot open display"
A interface gráfica precisa de um servidor X ou similar. Em servidores remotos, use SSH com forwarding X ou execute localmente.

### "Tkinter não encontrado"
No Windows ou Linux, instale o pacote do sistema:
```bash
# Windows: Reinstale Python e marque a opção "tcl/tk and IDLE"

# Linux (Debian/Ubuntu)
sudo apt install python3-tk

# Linux (Fedora/RedHat)
sudo dnf install python3-tkinter

# macOS
brew install python-tk
```

### "Erro ao carregar a palavra"
Verifique se os arquivos `words.py` (clássica) ou o dicionário `PALAVRAS` (Deluxe) estão presentes e bem formatados.

---

## 💡 Ideias para Contribuição

- Adicionar som (com biblioteca como `pygame`)
- Implementar multiplayer ou ranking online
- Adicionar temas (modo claro/escuro)
- Separar lógica do jogo da interface (facilita testes)
- Criar testes unitários
- Exportar/importar palavras de APIs
- Adicionar modo "contra o tempo"

---

## 🤝 Como Contribuir

1. Faça um **fork** do repositório
2. Crie uma **branch** com sua feature: `git checkout -b feature/nome-da-feature`
3. Faça **commits** claros: `git commit -m "Adiciona suporte a temas"`
4. Abra um **Pull Request**

---

## 📜 Licença

**MIT License** — Você é livre para usar, modificar e distribuir este código.

Para adicionar formalmente: crie um arquivo `LICENSE` com o texto da licença MIT.

---

## 📧 Contato & Suporte

Dúvidas ou sugestões? Abra uma **issue** no repositório ou entre em contato.

Algumas melhorias já planejadas:
- ✨ Sistema de rankings persistente
- 🎵 Efeitos sonoros
- 🌐 Modo online/multiplayer
- 📱 Versão mobile
- 🧪 Suite completa de testes

---

**Bom jogo!** 🎮🎉
