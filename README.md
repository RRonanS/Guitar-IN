Projeto referente a criar um driver para que receba sinais de guitarra via adaptador Irig e os converta em ações de mouse e teclado, com aplicação final de gerar tablaturas automaticamente
Discente: Pedro Leão Nogueira Steinbach

# Planejamento

Semana 1 (Passada);

  -  Verificar viabilidade da ideia  OK

  -  Selecionar frameworks se for o caso  OK

  -  Preparar ambiente de desenvolvimento  OK

Semana 2 (Passada);

  - Hello world do programa  OK

  - Obtenção e processamento inicial dos dados de entrada  OK

Semana 3 (Passada);

  - Tabelamento de entrada em notas  OK

  - Conversão de dados de entrada(notas da guitarra) em ações de mouse-teclado  OK

Semana 4 (Em andamento);

  - Testes de integração  HALF-OK

  - Criação da versão base da aplicação(Se houver tempo)

  - Preparação da apresentação, correção de erros e otimizações

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
  
