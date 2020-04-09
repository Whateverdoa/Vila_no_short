import os
import pandas as pd

def print_noshirt_rolls(colorcode, beeld, aantal, stans_tussen,oap,ee,filenaam_uit):
    """
    Take line from list and build csv for that line
    * todo: *args implement
    """

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{colorcode};{aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";;{beeld}\n" * int(aantal * oap + ee), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{colorcode};{aantal} etiketten;leeg.pdf\n", end="", file=fn)
        print(f";;stans.pdf\n" * stans_tussen, end="", file=fn)


def print_Rhein_rolls(omschrijving, colorcode, beeld, aantal, stans_tussen,oap,ee,filenaam_uit):
    """
    Take line from list and build csv for that line
    """

    with open(filenaam_uit, "a", encoding="utf-8") as fn:
        # open a file to append the strings too
        # print(f".;stans.pdf\n", end='', file=fn)

        print(f"{colorcode};{aantal} etiketten;leeg.pdf\n", end="", file=fn)

        print(f";;{beeld}\n" * int(aantal * oap + ee), end="", file=fn)
        # print(f"{colorcode}, {int(aantal * oap)};leeg.pdf\n", end="", file=fn)

        print(f"{colorcode};{aantal} etiketten;leeg.pdf\n", end="", file=fn)
        print(f";;stans.pdf\n" * stans_tussen, end="", file=fn)


def rhein_voorbereiden(aantal_per_lijst):

    split_csv = [x for x in os.listdir("tmp") if x.endswith(".csv")]
    print(f'split_csv {split_csv}')
    lijst_lengte = len(split_csv)

    use = lijst_lengte // aantal_per_lijst
    print(f'var=use {use}')

    count = 0
    for line in split_csv:
        file_Naam_In = f"tmp/{line}"  # changename

        # file_Naam_In = f"{naam}_inschiet.csv"
        filenaam_uit = f"vdps/vdp{count:>{0}{4}}_bewerkt.csv"  # changename
        print(file_Naam_In)
        print(filenaam_uit)
        count += 1

        trespa_lijst = pd.read_csv(file_Naam_In, ",", encoding="utf-8")
        print(trespa_lijst[0:1])

        oap = overaantalpercentage = 1  # 1.02 = 2% overlevering
        ee = 5  # = etiketten overlevering handmatig

    Rhein_df = [["omschrijving_sluit","Colorcode", "beeld", "aantal"]]
    Rhein_df.to_csv("lijst_in.csv", index=0)

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
            c = str(new_input_list[beg:eind][0][2])
            d = int(new_input_list[beg:eind][0][3])
            print_Rhein_rolls(a, b, c, d)

            beg += 1
            eind += 1