import animais
import emojis

# =============================================================
# PARTE 1 — PERSONALIZE SEU TAMAGOTCHI!
# Depois de completar, rode esse arquivo para ver o resultado :)
# =============================================================

# crie uma variável para armazenar o nome do seu tamagotchi
{COMPLETE AQUI!!}

# acesse o arquivo "animais.py" para ver como são as opções de animais e escolha um deles ;)
# ao escrever animais. dá para acessar as variáveis criadas no arquivo "animais.py"
meu_tamagotchi = animais.{COMPLETE AQUI!!}

# também no arquivo "animais.py", veja as cores em que seu animal pode ser desenhado no terminal
# complete depois do . com a cor desejada
cor = animais.{COMPLETE AQUI!!}

# versão dormindo do seu tamagotchi (deve combinar com o animal escolhido acima!)
# como fizemos acima para poder acessar uma variável que estava no arquivo "animais.py"?
animal_dormindo = {COMPLETE AQUI!!}

# escolha o emoji que representa a ENERGIA do seu tamagotchi
# sugestões: emojis.fogo, emojis.raio, emojis.coracao_rosa, emojis.coracao_amarelo, emojis.flor
emoji_energia = emojis.{COMPLETE AQUI!!}

# escolha o emoji que representa o DINHEIRO do seu tamagotchi
# sugestões: emojis.diamante, emojis.moeda, emojis.saca_dinheiro, emojis.flor, emojis.chocolate
# como fizemos acima para poder acessar uma variável que estava no arquivo "emojis.py"?
emoji_dinheiro = {COMPLETE AQUI!!}
                  
# escolha o emoji que representa a FOME do seu tamagotchi
emoji_fome = {COMPLETE AQUI!!}


# =============================================================
# TESTE — rode o arquivo e veja se ficou como você queria!
# =============================================================
print("=" * 40)
print("  SEU TAMAGOTCHI:")
print("=" * 40)
print(f"  nome:          {nome}")
print(f"  emoji energia: {emoji_energia}")
print(f"  emoji dinheiro:{emoji_dinheiro}")
print(f"  emoji fome:{emoji_fome}")
print()
print(f"{cor}{meu_tamagotchi}{animais.RESET}")
print()
print("  versão dormindo:")
print(f"{cor}{animal_dormindo}{animais.RESET}")
print("=" * 40)
print("  Se ficou do jeito que você queria, copie suas")
print("  variáveis para o arquivo principal!")
print("=" * 40)
