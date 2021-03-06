import random

# http://www.keithschwarz.com/darts-dice-coins/


class Roulette:
    def __init__(self, roulette_distribution, data=None):
        distribution = roulette_distribution.copy()
        distribution_size = len(distribution)

        if data is None:
            data = range(distribution_size)

        self.alias = [None] * distribution_size
        self.prob = [None] * distribution_size
        self.data = data

        distribution_sum = 0
        for i in range(distribution_size):
            distribution_sum += distribution[i]

        # TODO(andre:2018-05-28): Definir como tratar a situação em que a soma das probabilidades é zero
        if (distribution_sum == 0):
            return

        # Faz com que a soma dos elementos seja igual o tamanho da lista
        normalize_factor = distribution_size / distribution_sum
        for i in range(distribution_size):
            distribution[i] *= normalize_factor

        small = []
        large = []
        for i in range(distribution_size):
            if distribution[i] < 1:
                small.append(i)
            else:
                large.append(i)

        while (len(small) > 0 and len(large) > 0):
            small_element = small.pop()
            large_element = large.pop()
            self.prob[small_element] = distribution[small_element]
            self.alias[small_element] = large_element

            distribution[large_element] = (distribution[large_element] + distribution[small_element]) - 1
            if (distribution[large_element] < 1):
                small.append(large_element)
            else:
                large.append(large_element)

        while (len(large) > 0):
            large_element = large.pop()
            self.prob[large_element] = 1

        while (len(small) > 0):
            small_element = small.pop()
            self.prob[small_element] = 1

    def spin(self):
        index = random.randrange(len(self.prob))
        prob = random.random()

        if (prob >= self.prob[index]):
            index = self.alias[index]

        return self.data[index]


def roulette_spin(distribution):
    return Roulette(distribution).spin()
