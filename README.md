para testar e contribuir:

crie um ambiente virtual python na sua maquina usando:
    python -m venv /caminho/para/novo/ambiente/virtual

clone o repositorio usando:
    git clone https://github.com/guilhermerodriguesmain/Boneco-de-palito.git

ative o ambiente virtual python usando:
    .\Scripts\activate
        # certifique se de estar no diretorio raiz do ambiente virtual criado

acesse o diretorio clonado usando:
    no windows:
      cd caminho/para/o/diretorio/clonado
      dir 
          # deve aparecer algo como:
          Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        05/06/2025     01:35                __pycache__
-a----        05/06/2025     01:30           1425 campo.py
-a----        05/06/2025     01:30           3620 game.py
-a----        05/06/2025     01:30           1392 personagem.py
-a----        05/06/2025     01:30             32 requeriments.txt

instale as dependencias usando:
    pip install -r requeriments.txt

se deu tudo certo até aqui, basta usar a linha de comando abaixo para executar o script:
  python -m game.py
  
