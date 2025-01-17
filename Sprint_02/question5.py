import re


def max_population(data):
    city = []
    population = []
    for d in data:
        r = re.findall(r'\w{2}_\w{4,7}', d)
        city.append(r)
        p = re.findall(r'\d{5}', d)
        population.append(p)
    max_city = city[population.index(max(population))]
    max_pop = max(population)

    return max_city[0], int(max_pop[0])


data = ["id,name,poppulation,is_capital",
        "3024,eu_kyiv,24834,y",
        "3025,eu_volynia,20231,n",
        "3026,eu_galych,23745,n",
        "4892,me_medina,18038,n",
        "4401,af_cairo,18946,y",
        "4700,me_tabriz,13421,n",
        "4899,me_bagdad,22723,y",
        "6600,af_zulu,09720,n"]

print(max_population(data))
