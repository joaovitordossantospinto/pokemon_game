import pickle
from pessoa import *
from pokemon import *

def escolher_pokemon_incial(player):

    pikachu = PokemonEletrico('Pikachu', level=1)
    charmander = PokemonDeFogo('Charmander', level=1)
    squirtle = PokemonDeAgua('Squirtle', level=1)

    print('{} escolha seu pokemon inicial \n 1 - {}\n 2 - {}\n 3 - {}'.format(player, pikachu, charmander, squirtle))

    while True:
        escolha = input('>>>>>>')

        if escolha == '1':
            player.capturar(pikachu)
            break
        elif escolha == '2':
            player.capturar(charmander)
            break
        elif escolha == '3':
            player.capturar(squirtle)
            break
        else:
            print('Escolha inválida')

def salvar_jogo(player):
    try:
        with open('database.db', 'wb') as arquivo:
            pickle.dump(player, arquivo)
            print('Jogo salvo com sucesso!')
    except Exception as erro:
        print('erro ao salvar o jogo')
        print(erro)

def carregar_jogo():
    try:
        with open('database.db', 'rb') as arquivo:
            pickle.load(arquivo)
            print('Player {} carregado(a) com sucesso'.format(player))
            return player
    except Exception as erro:
        print('erro ao carregar o jogo')
        print(erro)


if __name__ == '__main__':
    print('*******************************')
    print('PROJETINHO POKEMON')
    print('*******************************')

    player = carregar_jogo()

    if not player:

        nome = input('Qual o seu nome? : ')
        player = Player(nome)
        print('Baita nome, Sr(a) {}:'.format(player))
        print('Pegue esta carteira, você irá precisar dela')
        player.mostrar_dinheiro()
        if player.pokemons:
            print('Bacana, você já tem pokemon(s)')
            player.mostrar_pokemon()
        else:
            print('Você irá precisar de ao menos um pokemons para iniciar sua jornada')
            escolher_pokemon_incial(player)
        print('Como você já está pronto, enfrente o Gary aí para ver se você é tudo isso')
        inimigo1 = Inimigo(nome='Gary', pokemons=[PokemonDeAgua('Squirtle', level=1)])
        player.batalhar(inimigo1)
        salvar_jogo(player)


    while True:
        print('----------------------------')
        print('O que deseja fazer?')
        print('1 - Explorar')
        print('2 - Enfrentar um inimigo')
        print('3 - Mostrar Pokeagenda')
        print('0 - Sair do jogo')
        escolha = input('Sua escolha: ')

        if escolha == '0':
            print('Jogo fechado')
            break
        elif escolha == '1':
            player.explorar()
            salvar_jogo(player)
        elif escolha == '2':
            inimigo_aleatorio = Inimigo()
            player.batalhar(inimigo_aleatorio)
            salvar_jogo(player)
        elif escolha == '3':
            player.mostrar_pokemon()
        else:
            print('Escolha inválida')

    #player.capturar(PokemonDeFogo('Charmander', level=1))
    #player.batalhar(inimigo1)
    #player.explorar()
    #player.mostrar_pokemon()