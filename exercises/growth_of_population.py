# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover 50
# new inhabitants per year come to live in the town. How many years
# does the town need to see its population greater or equal to p = 1200 inhabitants?


def nb_year(p0, percent, aug, p):
    population = [p0 + p0 * percent / 100 + aug]
    while population[-1] < p:
        result = population[-1] + population[-1] * percent/100 + aug
        population.append(result)

    return len(population)


print(nb_year(1500, 5, 100, 5000))  # 15
print(nb_year(1500000, 2.5, 10000, 2000000))    # 10
print(nb_year(1500000, 0.25, 1000, 2000000))    # 94