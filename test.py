import random


def biased_rolls(prob_list, s, n):
    random.seed(s)
    rolls = random.choices(list(range(1, len(prob_list) + 1)), prob_list, k=n)
    return rolls


def draw_histogram(m, rolls, width):
    print("frequency histogram:", m, "-sides to die", sep='')
    list1 = list(range(1, m + 1))
    a = max(set(rolls), key=rolls.count)
    most = (rolls.count(a))
    y = (most / width)

    def findappearance(x):
        n = rolls.count(x)
        b = n / y
        c = round(b)
        if b > width:
            print(x, '.', width * '#', sep='')
        else:
            print(x, ".", c * '#', (width - c) * '-', sep='')

    list(map(findappearance, list1))
    pass


if __name__ == "__main__":
    rolls = biased_rolls([1 / 12, 1 / 4, 1 / 3, 1 / 12, 1 / 12, 1 / 6], (2 ** 32) - 1, 20)
    print(rolls)
    draw_histogram(6, rolls, 50)
    pass
