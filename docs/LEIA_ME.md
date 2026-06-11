# 🐣 Tamagotchi — Guia de Arquivos

Olá! Aqui estão todos os arquivos do projeto divididos em partes.
A ideia é que você complete e teste cada parte separadamente antes
de juntar tudo no arquivo principal.

---

## 📁 Estrutura dos arquivos

| Arquivo | O que você vai fazer |
|---|---|
| `parte_1_personalizacao.py` | Escolher nome, animal, cor e emojis do seu tamagotchi |
| `parte_2_printa_animal_e_status.py` | Funções que mostram o bichinho e seus atributos na tela |
| `parte_3_barra_energia_e_dinheiro.py` | Funções que atualizam e exibem as barras de energia e dinheiro |
| `parte_4_dormir_e_comer.py` | Funções que permitem o tamagotchi dormir e comer |
| `jogo_1_pedra_papel_tesoura.py` | 🎮 Jogo clássico — Pedra, Papel, Tesoura |
| `jogo_2_ppt_turbinado.py` | 🎮 Versão turbinada com Lagarto e Spock |
| `jogo_3_apostas.py` | 🎮 Adivinhe o dado! |
| `jogo_4_velha.py` | 🎮 Jogo da Velha contra o computador |
| `parte_6_menus.py` | Os menus que conectam tudo — aqui o jogo inteiro roda! |
| `tamagotchi_lacunas.py` | **Arquivo principal** — onde você cola tudo no final |

---

## 🚀 Como usar

### Passo a passo sugerido:

1. **Comece pela parte 1** — personalize seu tamagotchi e rode o arquivo para ver o resultado.

2. **Avance pelas partes 2, 3 e 4** — cada arquivo tem um bloco de TESTE no final que roda
   automaticamente. Assim você sabe se está certo antes de continuar!

3. **Implemente os jogos** — cada jogo está no seu próprio arquivo (`jogo_1_`, `jogo_2_`, etc).
   Você pode fazer só os que quiser, em qualquer ordem!

4. **Na parte 6**, adicione na lista `jogos_disponiveis` os jogos que você implementou.
   O menu vai aparecer automaticamente com as opções certas — veja as instruções dentro do arquivo!

5. **No arquivo principal** (`tamagotchi_lacunas.py`), cole todas as suas respostas
   das partes anteriores nos lugares certos.

---

## 🎮 Como adicionar um jogo implementado ao menu

Depois de completar um arquivo de jogo (ex: `jogo_3_apostas.py`), faça duas coisas
no arquivo `parte_6_menus.py` (e depois no `tamagotchi_lacunas.py`):

**1. Cole a função do jogo** na seção "JOGOS" (logo acima da lista `jogos_disponiveis`).

**2. Ative a linha do jogo** na lista `jogos_disponiveis`, apagando o `#` do início:

```python
# antes (jogo desativado):
# {"nome": "Jogo de Apostas — dado", "funcao": jogo_de_apostas, "custo": 2, "premio": 4},

# depois (jogo ativado!):
{"nome": "Jogo de Apostas — dado", "funcao": jogo_de_apostas, "custo": 2, "premio": 4},
```

O menu vai aparecer automaticamente com o jogo novo — sem precisar mexer em mais nada!

---

## ⚠️ Atenção

- Cada arquivo de parte tem um **CABEÇALHO** com variáveis de exemplo (como `nome = "Bolinha"`).
  Elas existem só para o teste funcionar — quando você copiar para o arquivo principal,
  use as **suas** variáveis da parte 1!

- Os `{COMPLETE AQUI!!}` nos arquivos de parte são **idênticos** aos do arquivo principal.
  Tudo que você escrever aqui pode ser colado lá diretamente.

- Os arquivos `animais.py` e `emojis.py` precisam estar na mesma pasta para tudo funcionar.

---

Boa sorte e divirta-se! 🐱🐶🐹
