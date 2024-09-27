import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None): #nome argumento não obrigatório
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        self.ataque = self.level * 5
        self.vida = self.level + 10

    def __str__(self):
        return '{}' '({})' .format(self.nome, self.level)

    def atacar (self, pokemon):
        ataque_efetivo = int(self.ataque * random.random() * 1.3)
        pokemon.vida -= ataque_efetivo
        #pokemon.vida = pokemon.vida - ataque_efetivo // Significa a mesma coisa da linha acima
        print('{} perdeu {} pontos de vida'.format(pokemon, ataque_efetivo))

        if pokemon.vida <= 0:
            print('{} foi derrotado'.format(pokemon))
            return True
        else:
            return False

class PokemonEletrico(Pokemon):
    tipo = 'eletrico'
    def atacar(self, pokemon):
        print('{} ({}) deu cum choquinho em {}'.format(self.nome, self.level, pokemon))
        return super().atacar(pokemon)

class PokemonDeFogo(Pokemon):
    tipo = 'fogo'
    def atacar(self, pokemon):
        print('{} ({}) chamuscou {}'.format(self.nome, self.level, pokemon))
        return super().atacar(pokemon)

class PokemonDeAgua(Pokemon):
    tipo = 'agua'
    def atacar(self, pokemon):
        print('{} ({}) molhou {}'.format(self.nome, self.level, pokemon))
        return super().atacar(pokemon)

#meu_pokemon = PokemonDeFogo('charmander', '50')

#pokemon_do_meu_vizinho = PokemonEletrico('pikachu')

#meu_pokemon.atacar(pokemon_do_meu_vizinho)