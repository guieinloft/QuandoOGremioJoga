import sys
import json
import requests
from bs4 import BeautifulSoup


def pega_cores(cores, time1, time2):
    '''pega as cores que vão ser utilizadas pra mostrar os times'''
    if cores:
        with open('./cores.json', 'r', encoding='utf8') as arq:
            dcores = json.load(arq)
        if time1 in dcores.keys():
            cor1 = dcores[time1]
        else:
            cor1 = 97

        if time2 in dcores.keys():
            cor2 = dcores[time2]
        else:
            cor2 = 97

    return (cor1, cor2)


def pega_parametros():
    '''pega os parametros especificados pelo usuario'''
    extenso = False
    cores = False
    formato = 0
    for param in sys.argv:
        if '-extenso' in param:
            extenso = True
        if '-cores' in param:
            cores = True
        if '-formato' in param:
            formato = int(param.split('=')[1])

    return [extenso, cores, formato]


def imprime(times, campeonato, info, tcores, formato):
    '''imprime a string do bagulho'''
    match formato:
        case 1:
            print("%s X %s" % (times[0], times[1]))
        case 2:
            print("%s X %s: %s" % (times[0], times[1], info[0]))
        case 3:
            print("%s X %s (%s): %s"
                  % (times[0], times[1], campeonato, info[0]))
        case 4:
            print("%s X %s: %s- %s"
                  % (times[0], times[1], info[0], info[1]))
        case 5:
            print("%s X %s (%s): %s- %s"
                  % (times[0], times[1], campeonato, info[0], info[1]))
        case _:
            print("\033[1;%dm%s X \033[1;%dm%s\033[0m\n%s\n%s\n%s"
                  % (tcores[0], times[0], tcores[1], times[1],
                     campeonato, info[0], info[1]))


def main():
    '''funcao principal do codigo'''
    cabecalho = {'User-Agent':
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                 + 'AppleWebKit/537.36 (KHTML, like Gecko)'}
    pagina = 'https://gremio.net'
    dados = requests.get(pagina, headers=cabecalho, timeout=1)
    soup = BeautifulSoup(dados.text, 'html.parser')

    extenso, cores, formato = pega_parametros()

    info = soup.find_all(class_='info')

    times = soup.find_all(class_='sigla')
    times[0] = times[0].text
    times[1] = times[1].text

    if cores:
        tcores = pega_cores(cores, times[0], times[1])
    else:
        tcores = (97, 97)

    if extenso:
        times = info[0].text
        times = times.split(" x ")

    campeonato = soup.find(class_='equipe').text
    info = info[1].text
    info = info.split('\xa0')
    info.remove(' ')
    while '' in info:
        info.remove('')

    imprime(times, campeonato, info, tcores, formato)


if __name__ == '__main__':
    main()
