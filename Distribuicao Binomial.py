from scipy.stats import binom

# Jogar uma moeda 5 vezes, e dar cara 3 vezes
prob = binom.pmf(3, 5, 0.5)

# Passar 4 sinais de 4 tempos, e pegar 0, 1, 2, 3, 4 sinais verdes
binom.pmf(0, 4, 0.25)
binom.pmf(1, 4, 0.25)
binom.pmf(2, 4, 0.25)
binom.pmf(3, 4, 0.25)
binom.pmf(4, 4, 0.25)

# Se fossem sinais de 2 tempos
binom.pmf(4, 4, 0.5)

# Probabilidade acumulativa
binom.cdf(4, 4, 0.25)

# Acertar 7 em 12 questões com 4 alternativas cada
binom.pmf(7, 12, 0.25) * 100

binom.pmf(5, 12, 0.75)