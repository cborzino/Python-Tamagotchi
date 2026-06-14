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

The repository is organized into four groups of files, each serving a different purpose during the learning process.

### Core files

These files contain the shared resources and the complete version of the project.

```text
animais.py
emojis.py
tamagotchi.py
```

* `animais.py` contains all ASCII-art animals and terminal color definitions.
* `emojis.py` contains the emoji constants used throughout the game.
* `tamagotchi.py` is the complete reference implementation of the project.

---

### Guided exercises (`material/`)

The files in the `material/` folder are the main learning activities. Each one introduces a new programming concept and asks students to complete specific sections marked with `{COMPLETE AQUI!!}`.

```text
material/
├── parte_1_personalizacao.py
├── parte_2_printa_animal_e_status.py
├── parte_3_barra_energia_e_dinheiro.py
├── parte_4_dormir_e_comer.py
├── parte_6_menus.py
└── tamagotchi_para_completar.py
```

The recommended order is:

1. Personalize the pet.
2. Display the pet and status information.
3. Implement the attribute bars.
4. Implement sleeping and eating mechanics.
5. Add minigames.
6. Build the final menu system.
7. Assemble everything in `tamagotchi_para_completar.py`.

---

### Minigames (`jogos/`)

Each minigame is provided in its own file so that students can implement and test it independently.

```text
jogos/
├── jogo_1_pedra_papel_tesoura.py
├── jogo_2_ppt_turbinado.py
├── jogo_3_apostas.py
└── jogo_4_velha.py
```

Students can complete the games in any order and later integrate them into the main menu.

---

### Documentation (`docs/`)

```text
docs/
└── LEIA_ME.md
```

Additional documentation and instructor notes can be stored here.

---

### File design philosophy

Each exercise file (`parte_X`) and each minigame file (`jogo_X`) is intentionally self-contained:

* A header provides example variables so the file can run independently.
* Only a small portion of the code is left incomplete.
* Test code at the bottom executes automatically.
* The same placeholders appear in `tamagotchi_para_completar.py`, making final integration a simple copy-and-paste process.

This structure allows students to focus on one concept at a time while continuously testing their progress.

## 🚀 How to use

### Prerequisites

- Python 3.8+
- No external libraries required

### Running the complete game

```bash
python tamagotchi.py
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
* `animais.py` and `emojis.py` are imported by the complete Tamagotchi implementation and should remain alongside `tamagotchi.py`. If the folder structure is modified, import statements may need to be updated accordingly.
- Minigame 4 (Tic-tac-toe) is significantly harder than the others due to list indexing and nested functions.
