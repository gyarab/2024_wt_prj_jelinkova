import httpx

url = 'https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt?date=13.02.2025'
r = httpx.get(url)

# print(r.text)
# print(r.status_code)

lines = r.text.split("\n")

povolene_meny = {"AUD", "BRL", "BGN", "CNY", "DKK", "EUR", "CZK", "PHP", "HKD", "INR", "IDR", "ISK", "ILS", "JPY", "ZAR", "CAD", "KRW", "HUF", "MYR", "MXN", "XDR", "NOK", "NZD", "PLN", "RON", "SGD", "SEK", "CHF", "THB", "TRY", "USD", "GBP"}
b = True

while b:
    vstup = input("Prosim zadejte menu, ze ktere prevadite (EUR, CZK..): ")
    mena_prvni = str(vstup).upper()
    if mena_prvni in povolene_meny:
        for line in lines:
            if "|" + mena_prvni + "|" in line:
                row = line
                b = False
                break
    if mena_prvni == "CZK":
        kurz_prvni = 1
        mnozstvi_prvni = 1
        b = False

if mena_prvni != "CZK":
    row_arr = row.split("|")

    kurz_str = row_arr[-1]
    kurz_prvni = float(kurz_str.replace(",","."))

    mnozstvi_prvni = float(row_arr[2])

b = True

while b:
    vstup = input("Prosim zadejte menu, na kterou prevadite (EUR, CZK..): ")
    mena_druha = str(vstup).upper()
    if mena_druha in povolene_meny:
        for line in lines:
            if "|" + mena_druha + "|" in line:
                row = line
                b = False
                break
    if mena_druha == "CZK":
        kurz_druhy = 1
        mnozstvi_druhe = 1
        b = False

if mena_druha != "CZK":
    row_arr = row.split("|")

    kurz_str = row_arr[-1]
    kurz_druhy = float(kurz_str.replace(",","."))

    mnozstvi_druhe = float(row_arr[2])

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

vysledek = castka * (kurz_prvni / kurz_druhy) * (mnozstvi_druhe / mnozstvi_prvni)

print(f"Vysledek je {vysledek}" + " " + mena_druha + ".")
# print(kurz_prvni)
# print(kurz_druhy)