# QuandoOGremioJoga

Script em Python que mostra ao usuário as informações do próximo jogo do Grêmio.  
Além disso, mostra também:
- Campeonato;
- Data e horário;
- Estádio.
  
As informações são tiradas do [site oficial do Grêmio](https://gremio.net/).

### Como usar:
Basta apenas digitar ```python gremio.py``` na linha de comando.  
Há três parâmetros que podem ser utilizados para modificar o comportamento do programa:
- ```-cores```: Mostra as cores principais dos times que vão jogar;
- ```-extenso```: Mostra os nomes dos times em extenso;
- ```-formato=X```: Modifica o formato da saída (não compatível com o parâmetro ```-cores```), X podendo ser:
    - 0: saída padrão;
    - 1: mostra apenas o nome dos times;
    - 2: mostra o nome dos times, data e horário;
    - 3: mostra o nome dos times, campeonato, data e horário;
    - 3: mostra o nome dos times, data, horário e estádio;
    - 4: mostra o nome dos times, campeonato, data, horário e estádio.
