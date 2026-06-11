# Python-Tamagotchi
# 🐣 Tamagotchi

A Tamagotchi-inspired terminal game written in Python, designed to introduce programming to teenagers. The project is split into multiple files with guided fill-in-the-blank exercises, allowing students to implement and test each feature incrementally. Instructions are written in Brazilian Portuguese.

---

## 🎮 About the game

The player adopts a virtual pet and keeps it alive and happy by managing three attributes, all capped at 10:

| Attribute | Starting value | How to increase |
|---|---|---|
| ⚡ Energy | 5 | Sleep |
| 🧁 Hunger | 5 | Eat |
| 🪙 Money | 3 | Win minigames |

At the start of each run the player **personalizes their pet**: they pick a name, choose one of five ASCII animals (cat, dog, dino, whale or turtle), pick a display color, and choose emojis to represent energy and money on the status bars.

### Main menu actions

- **Play** — spend energy to play a minigame and earn money if you win. Losing a game costs 1 hunger point.
- **Eat** — spend money at the in-game shop to recover hunger.
- **Sleep** — choose how many hours to sleep; each hour recovers 1 energy point.
- **View status** — display the pet and all three attribute bars.

### Shop

| Item | Cost | Hunger recovered |
|---|---|---|
| 🧁 Biscoito | 1 🪙 | +2 |
| 🍫 Chocolate | 2 🪙 | +4 |
| 🍰 Bolo | 3 🪙 | +6 |

### Minigames

| Game | Energy cost | Prize |
|---|---|---|
| ✊ Pedra, Papel, Tesoura | −1 | +2 🪙 |
| 🖖 PPT Turbinado (+ Lagarto e Spock) | −1 | +3 🪙 |
| 🎲 Jogo de Apostas (guess the dice) | −2 | +4 🪙 |
| ❌ Jogo da Velha (Tic-tac-toe) | −3 | +5 🪙 |

The minigame menu only shows the games that have been implemented — students unlock new options as they complete each game file.

---

## 📁 Project structure

```
tamagotchi/
├── animais.py                        # ASCII art for all animals + color codes
├── emojis.py                         # Emoji constants used throughout the game
├── tamagotchi_para_completar.py      # Main file — students paste everything here at the end
│
├── parte_1_personalizacao.py         # Step 1: name, animal, color and emoji choices
├── parte_2_printa_animal_e_status.py # Step 2: display functions
├── parte_3_barra_energia_e_dinheiro.py # Step 3: energy and money bar logic
├── parte_4_dormir_e_comer.py         # Step 4: sleep and eat functions
│
├── jogo_1_pedra_papel_tesoura.py     # Minigame 1: Rock, Paper, Scissors
├── jogo_2_ppt_turbinado.py           # Minigame 2: Rock, Paper, Scissors, Lizard, Spock
├── jogo_3_apostas.py                 # Minigame 3: Dice guessing game
├── jogo_4_velha.py                   # Minigame 4: Tic-tac-toe
│
└── parte_6_menus.py                  # Step 6: main menu + dynamic game menu
```

Each individual file (`parte_X` and `jogo_X`) contains:
- A **header** with pre-filled example variables so the file runs on its own.
- The **function(s) to be completed**, with `{COMPLETE AQUI!!}` placeholders identical to the ones in the main file.
- A **test block** at the end that runs automatically, so students can verify their work before moving on.

---

## 🚀 How to use

### Prerequisites

- Python 3.8+
- No external libraries required

### Running the complete game

```bash
python tamagotchi_para_completar.py
```

### Suggested workflow for students

1. **Start with `parte_1`** — personalize the pet and run the file to see the result.
2. **Work through `parte_2`, `parte_3`, and `parte_4`** — each file has an automatic test block at the end.
3. **Implement the minigames** — each game has its own file and can be done in any order.
4. **Finish with `parte_6`** — add completed games to the `jogos_disponiveis` list to make them appear in the menu.
5. **Paste everything into `tamagotchi_para_completar.py`** — the main file has the same placeholders, so it's a straightforward copy-paste.

### Activating a minigame in the menu

After completing a game file, two steps are needed in `parte_6_menus.py` (and later in the main file):

1. **Paste the game function** into the games section above `jogos_disponiveis`.
2. **Uncomment the corresponding line** in the list:

```python
# before (game disabled):
# {"nome": "Jogo de Apostas — dado", "funcao": jogo_de_apostas, "custo": 2, "premio": 4},

# after (game active!):
{"nome": "Jogo de Apostas — dado", "funcao": jogo_de_apostas, "custo": 2, "premio": 4},
```

The menu renumbers itself automatically — no other changes needed.

---

## 🧩 Concepts practiced

The exercises cover the following Python fundamentals, introduced gradually across the files:

| Concept | Where it appears |
|---|---|
| Variables and data types | Part 1 |
| Functions and `print` / `return` | Parts 2–4 |
| f-strings | Parts 2–4 |
| `if` / `else` conditionals | Parts 2–4, all games |
| `for` loops and `range()` | Parts 3–4 |
| `input()` and type casting | Parts 4, games |
| Lists and indexing | Games 1–4 |
| Dictionaries | Part 4 (`comer`), Part 6 |
| `random.choice()` / `random.randint()` | Games 1–3 |
| Nested functions | Game 4 (`jogo_da_velha`) |
| List of dictionaries as a data structure | Part 6 |

---

## ⚠️ Notes for instructors

- The red squiggly lines that appear in VS Code on `{COMPLETE AQUI!!}` placeholders are expected — they are caused by Pylance trying to parse the placeholders as Python expressions. They disappear as soon as the placeholder is replaced with valid code.
- Each individual file has a header with example variables (e.g. `nome = "Caramelo"`). Students should replace these with their own variables from Part 1 when pasting into the main file.
- `animais.py` and `emojis.py` must be in the same folder as all other files for the imports to work.
- Minigame 4 (Tic-tac-toe) is significantly harder than the others due to list indexing and nested functions.
