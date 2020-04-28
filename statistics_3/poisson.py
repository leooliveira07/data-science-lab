from scipy.stats import poisson

# Média de acidentes 3 carros por dia

# Probabilidade de 3 no dia
poisson.pmf(3, 2)

# Probabilidade de 3 ou menos no dia
poisson.cdf(3, 2)

# Probabilidade de mais de 3 no dia
poisson.sf(3, 2)