import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

pokemons = {}
pokemons_numbers = {}

for i in range(1, n + 1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons.update({pokemon: i})
    pokemons_numbers.update({i: pokemon})

for _ in range(m):
    search = sys.stdin.readline().rstrip()
    try:
        print(pokemons_numbers.get(int(search)))
    except ValueError:
        print(pokemons.get(search))
