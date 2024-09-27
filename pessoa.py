#from pokemon import PokemonEletrico, PokemonDeFogo, PokemonDeAgua
from pokemon import *
import random

NOMES = ['João', 'Joana', 'Joãozinho', 'Joaninha']

POKEMONS = [
    PokemonDeFogo('Charmander'),
    PokemonDeFogo('Vulpix'),
    PokemonDeFogo('Ponyta'),
    PokemonEletrico('Pikachu'),
    PokemonEletrico('Magnemite'),
    PokemonEletrico('Voltorb'),
    PokemonDeAgua('Squirtle'),
    PokemonDeAgua('Psyduck'),
    PokemonDeAgua('Polywag'),

]

class Pessoa:
    def __init__(self, nome=None, pokemons=[], dinheiro=100):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

        self.dinheiro = dinheiro
    def __str__(self):
        return self.nome
    def mostrar_pokemon(self):
        if self.pokemons:
            for index, pokemon in enumerate(self.pokemons):
                print('Pokemons de {}'.format(self))
                print('{} - {}'.format(index, pokemon))
        else:
            print('{} não tem nenhum pokemon'.format(self))

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print('{} escolheu {}'.format(self, pokemon_escolhido))
            return pokemon_escolhido
        else:
            print('Não possue nenhum pokemon')


    def batalhar(self, pessoa):
        print('{} Iniciou uma batalha com {}'.format(self, pessoa))
        pokemon_inimigo = pessoa.escolher_pokemon()
        #pessoa.mostrar_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print('{} venceu a batalha'.format(self))
                    self.ganhar_dinheiro(pokemon_inimigo.level * 100)
                    break
                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print('{} venceu a batalha'.format(pessoa))
                    break
        else:
            print('a batalha não pode ocorrer!')

    def mostrar_dinheiro(self):
        print('você tem R${} na carteira'.format(self.dinheiro))

    def ganhar_dinheiro (self, quantidade):
        self.dinheiro += quantidade
        print('você ganhou R$ {}'.format(quantidade))
        self.mostrar_dinheiro()

class Player(Pessoa):
    tipo = 'player'

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print('{} capturou {}'.format(self, pokemon))

    def escolher_pokemon(self):
        self.mostrar_pokemon()

        if self.pokemons:
            while True:
                escolha = input('Escolha seu pokemon: ')
                try:
                    escolha = int(escolha)
                    pokemon_escolhido = self.pokemons[escolha]
                    print('{} escolheu {}'.format(self, pokemon_escolhido))
                    return pokemon_escolhido
                except:
                    print('Escolha inválida')
        else:
            print('Não possue nenhum pokemon')

    def explorar(self):
        if random.random() <=0.3:
            pokemon = random.choice(POKEMONS)
            print('Um {} selvagem apareceu'.format(pokemon))
            escolha = input('Deseja capturar {} ? (s/n): '.format(pokemon))
            if escolha == 's':
                if random.random() >= 0.5:
                    self.capturar(pokemon)
                else:
                    print('{} deu no pé'.format(pokemon))
            else:
                print('Compreensivo, tenha um bom dia')
        else:
            print('Essa exploração não deu em nada')

class Inimigo(Pessoa):
    tipo = 'Inimigo'

    def __init__(self, nome=None, pokemons=None):
        if not pokemons:
            pokemons_aleatorios = []
            for i in range(random.randint(1,6)): #quantidade de pokemons
                pokemons_aleatorios.append(random.choice(POKEMONS))
            super().__init__(nome=None, pokemons=pokemons_aleatorios)
        else:
            super().__init__(nome=None, pokemons=pokemons)

#inimigo = Inimigo()
#print(inimigo)
#inimigo.mostrar_pokemon()

