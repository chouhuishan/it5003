def how_many_years(lines=list[int]) -> list[int]:
    year_each_planet = []
    for line in lines:
        P, R, F = map(int, line.split())
        years = 0
        while P <= F:
            years += 1
            P *= R
        year_each_planet.append(years)
    return year_each_planet


T = int(input())
lines = [input() for _ in range(T)]

for year in how_many_years(lines):
    print(year)
