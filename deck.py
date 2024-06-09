import collections
Carta = collections.namedtuple('Carta', ['num', 'naipe'])

class Baralho:

    numList = [str(card) for card in range(2,11)] + list('QJKA')
    naipesList  = 'paus copas espada ouro'.split()

    def __init__(self):
        self._carta = [Carta(num, naipe)
                for naipe in self.naipesList
                for num in self.numList]
    def __len__(self):
        return len(self._carta)

baralho1 = Baralho()
print(len(baralho1))
