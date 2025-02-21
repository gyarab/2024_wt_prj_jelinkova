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
    vstup = input("Prosim zadejte castku: ")
    try:
        castka = float(vstup)
    except ValueError:
        print("Zadali jste neplatny vstup.")
        continue
    if castka <= 0:
        print("Zadali jste neplatny vstup.")
        continue
    break
    

while True:
    vstup = input("Pro prevod z CZK na EUR napis '1', z EUR na CZK '2': ")
    prevod = str(vstup)
    if prevod != "1" and prevod != "2":
        print("Zadali jste neplatny vstup.")
        continue
    if prevod == "2":
        vysledek = castka * kurz
        mena = "korun ceskych"
        break
    if prevod == "1":
        vysledek = castka / kurz
        mena = "eur"
        break

print(f"Vysledek je {vysledek}" + " " + mena + ".")