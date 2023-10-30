Projeto referente a criar um driver para que receba sinais de guitarra/violão como microfone via adaptador Irig e os converta em ações de mouse e teclado.

# Executar o código

1- Instale o modulo uinput;

  modprobe uinput

2- Navegue até o diretório onde está a pasta do programa e use o comando;
  
  python main.py

  (Desenvolvido e testado com python3.9)

3- Podem haver erros de dependências, para isso as instale com;

  pip install numpy

  pip install python-uinput

  pip install pyaudio

  pip install scipy

4 - É possível testar apenas a parte do uinput(caso não haja uma guitarra)

  Modifique o arquivo test.py conforme deseja testas, entrando com o json de mapeamento notas-teclas e setando as notas que serão testadas

  python test.py

  # Vídeo demonstração

  https://youtu.be/5ZuLxYUdi-I?si=X8G1NO4kWfUzOWL3

  # Vídeo da instalação

  https://www.youtube.com/watch?v=tmLL1RngJ5U

  # Apresentação

  https://docs.google.com/presentation/d/1tN87zwQ_mQpr2aL7gzJJ0I_Iw3oN_qP2L1FVNskfvQE/edit?usp=sharing
  
