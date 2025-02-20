import httpx

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025'
r = httpx.get(url)

# print(r.text)
# print(r.status_code)

lines = r.text.split("\n")

for line in lines:
    if "|EUR|" in line:
        row = line

# print(row)

row_arr = row.split("|")

kurz_str = row_arr[-1]
kurz_str = float(kurz_str.replace(",","."))

kurz = float(kurz_str)
# print(kurz_str)

while True:
    vstup = input("Zadejte castku: ")
    try:
        castka = int(vstup)
    except ValueError:
        print("Neplatny vstup!")
        continue
    break

while True:
    vstup = input("Zadejte smer prevodu (EUR->CZK / CZK->EUR): ")
    prevod = str(vstup)
    if prevod != "EUR->CZK" and prevod != "CZK->EUR":
        print("Neplatny vstup!")
        continue
    if prevod == "EUR->CZK":
        vysledek = castka * kurz
        break
    if prevod == "CZK->EUR":
        vysledek = castka / kurz
        break

print(f"Vysledek je {vysledek}")