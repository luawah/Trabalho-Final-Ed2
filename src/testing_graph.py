from get_data import datarows
from models.Country import Country
from models.Discipline import Discipline
from models.Result import Result
from models.Olympics import Olympics

olympics = Olympics()
france = Country(datarows[1]['Country'])
archery = Discipline(datarows[1]['Discipline'])
france_archery = Result(france,archery, datarows[1]['Medal'], datrows[1]['Year'])

france.add_result(france_archery)
archery.add_result(france_archery)

olympics.add_country(france)
olympics.add_discipline(archery)
olympics.add_result(france_archery)

c2 = Country(datarows[32]['Country'])
olympics.add_country(c2)

# for country in olympics.countries:
#     print(country)

# for discipline in olympics.disciplines:
#     print(discipline)

# for result in olympics.results:
#     print(result)

olympics.visualize()



