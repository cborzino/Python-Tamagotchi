# são 5 opções de animais, escolha seu preferido

dino = r"""
               ___
              / °_)
     _.----._/ /
    /         /
 __/ (  | (  |
/__.-'|_|--|_|
"""

gato = r"""
      ,_     _,
      |\\___//|
      | 0   0 |
      \=. Y .=/
       )  `  (    ,
      /       \  ((
      |       |   ))
     /| |   | |\_//
     \| |._.| |/-`
      '"'   '"'
"""

cachorro = r""" 
       _=,_
    o_/0 / \
    \__ |  /
     ='|--\
       /    '-.
       \ |_   _'-. /
        |/ \_(   |" 
       C/ ,--___/
"""

baleia = r"""
       .
      ":"
    ___:____     |"\/"|
  ,'        `.    \  /
  |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
"""

tartaruga = r"""
  _____     ____
 /      \  |  o | 
|        |/ ___\| 
|_________/     
|_|_| |_|_|
"""

# cores para imprimir o animal
AMARELO  = "\033[93m"
CIANO    = "\033[96m"
VERMELHO = "\033[31m"
VERDE    = "\033[32m"  
AZUL     = "\033[34m" 
MAGENTA  = "\033[35m" 
BRANCO   = "\033[37m"

# versões dos animais dormindo

dino_dormindo = r"""
                  zzz 
                 zz
                z
               ___
              / -_)
     _.----._/ /
    /         /
 __/ (  | (  |
/__.-'|_|--|_|
"""

gato_dormindo = r"""
                  zzz 
                 zz
                z
      ,_     _,
      |\\___//|
      | -   - |
      \=. Y .=/
       )  `  (    ,
      /       \  ((
      |       |   ))
     /| |   | |\_//
     \| |._.| |/-`
      '"'   '"'
"""

cachorro_dormindo = r""" 
             zzz 
            zz
           z
       _=,_
    o_/- / \
    \__ |  /
     ='|--\
       /    '-.
       \ |_   _'-. /
        |/ \_(   |" 
       C/ ,--___/
"""

baleia_dormindo = r"""
           zzz 
          zz
         z    
    _______     |"\/"|
  ,'        `.    \  /
  |  -        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
"""

tartaruga_dormindo = r"""
                  zzz 
                 zz
                z
  _____     ____
 /      \  |  - | 
|        |/ ____| 
|_________/     
|_|_| |_|_|
"""

# variáveis para deixar os prints mais bonitos 
NEGRITO    = "\033[1m"
RESET   = "\033[0m" 

# print()
# print(f"{NEGRITO}{VERDE}{dino}{RESET}")
# print(f"{NEGRITO}{AMARELO}{gato}{RESET}")
# print(f"{NEGRITO}{BRANCO}{cachorro}{RESET}")
# print(f"{NEGRITO}{AZUL}{baleia}{RESET}")
# print(f"{MAGENTA}{tartaruga}{RESET}")