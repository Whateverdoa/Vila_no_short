import pandas as pd
from pathlib import Path
from source.standard_pad_module import *

# split_csv = paden_dict["pad_tmp"].glob(".csv")
p = paden_dict["pad_tmp"]
print(p)
split_csv = sorted(list(p.glob('*.csv')))


count = 0
for posix_pad_naar_csv in split_csv:
    file_Naam_In = posix_pad_naar_csv  # changename

    # file_Naam_In = f"{naam}_inschiet.csv"
    filenaam_uit = f"vdps/vdp{count:>{0}{4}}_bewerkt.csv"  # changename
    print(file_Naam_In)
    print(filenaam_uit)
    count += 1

    inputlijst = pd.read_csv(file_Naam_In, ",", encoding="utf-8", dtype="str")
    print(inputlijst[0:1])

    oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
    ee = 5  # = etiketten overlevering handmatig


    # ___________________________________________________________________________________________


def noshort_rolls_4kolommen(
    omschrijving_sluit, sluit_barcode, beeld, aantal_etiketten, wikkel
):
    """verwijzing naar plek  basis_csv_bestand-in"""

    inloop = pd.DataFrame(
        [["", 0, "", "stans.pdf"] for x in range(2)],
        columns=["omschrijving_sluit_1", "sluit_barcode_1", "aantal_1", "beeld"],
        dtype="str",
    )

    sluitetiket = pd.DataFrame(
        [
            [
                f"{omschrijving_sluit}",
                f"{sluit_barcode}",
                f"{aantal_etiketten}",
                "leeg.pdf",
            ]
        ],
        columns=["omschrijving_sluit_1", "sluit_barcode_1", "aantal_1", "beeld"],
        dtype="str",
    )

    tussen_rol_en_sluit = pd.DataFrame(
        [["", 0, "", "stans.pdf"] for x in range(wikkel)],
        columns=["omschrijving_sluit_1", "sluit_barcode_1", "aantal_1", "beeld"],
        dtype="str",
    )

    lichaam_rol = pd.DataFrame(
        [[" ", "100000000000", "", beeld]] * int(aantal_etiketten),
        columns=["omschrijving_sluit_1", "sluit_barcode_1", "aantal_1", "beeld"],
        dtype="str",
    )

    rol = pd.concat([inloop, sluitetiket, tussen_rol_en_sluit, lichaam_rol])

    return rol




input_lijst_dataframe = inputlijst[["omschrijving_sluit", "sluit_barcode", "aantal", "beeld"]]
input_lijst_dataframe.to_csv("lijst_in.csv", index=0)

new_input_list = []

with open("lijst_in.csv") as input:
    num = 0
    for line in input:
        line_split = line.split(",")

        new_input_list.append(line_split)
        num += 1

list_length = len(new_input_list)

beg = 1
eind = 2

with open(filenaam_uit, "w", encoding="utf-8") as fn:

    print("sluit_barcode;beeld1;pdf1", file=fn)

with open(filenaam_uit, "a", encoding="utf-8") as fn:
    for _ in range(list_length - 1):
        a = str(new_input_list[beg:eind][0][0])
        b = str(new_input_list[beg:eind][0][1])
        c = int(new_input_list[beg:eind][0][2])
        print_noshirt_rolls(a, b, c)

        beg += 1
        eind += 1