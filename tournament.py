#Simular um torneio esportivo

import csv
import sys
import random

# Número de simulações a serem realizadas
N = 1000


def main():

    # Assegurar o uso correto
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    file = sys.argv[1]
    # TODO: Ler teams em memória a partir do arquivo
    with open(file, "r") as csv_file:
        leitor = csv.DictReader(csv_file)
        for linha in leitor:
            linha["rating"] = int(linha["rating"])
                #Anexo do dicionário de cada time á Teams
            teams.append(linha)
            
    counts = {}
    # TODO: Simula N torneios e acompanhar a contagem das vitórias
    for t in range(N):
        vencedor = simulate_tournament(teams)
        if vencedor in counts:
            counts[vencedor] +=1
        else:
            counts[vencedor] = 1
      
    
    # Imprimir as chances de vitória de cada equipe, de acordo com a simulação
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
   #Simular um jogo. Return True se o time vencer, Falso caso contrário
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    #Simular uma rodada. Devolver uma lista das equipes vencedoras
    winners = []
    # Simular jogos para todos os pares de equipes
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    # Simular um torneio. Retornar nome do time vencedor
    # TODO
    while len(teams) > 1:
        teams = simulate_round(teams)
        
    return teams[0]['team']
        
if __name__ == "__main__":
    main()
