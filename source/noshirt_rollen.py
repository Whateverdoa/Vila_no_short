""" quick for 6 banen"""

import pandas as pd
import os
from pathlib import Path
import PySimpleGUI as sg

from source.standard_pad_module import cleaner, dir_maak_comp_lijst
from source.functies_mes import read_out_4,wikkel_4_baans_tc,read_out_6,wikkel_6_baans_tc
from source.rol_soorten import rhein_voorbereiden

import sys

sg.ChangeLookAndFeel('GreenTan')

if len(sys.argv) == 1:
    fname = sg.popup_get_file('CSV name == ordernummer!!, click OK om door te gaan.')
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    # ______________cleanup
    # cleaning files and dirs will now be at the end of the session
    # ______________cleanup
    wdir = Path.cwd()


    Etiketten_Y = 8
    data_uit_vdp = int(Etiketten_Y)
    inloop = int(Etiketten_Y) * 10
    print(f'{inloop} etiketten = (10 sheets van {Etiketten_Y}) in en -uitloop')
    print(type(inloop))

    pad = Path(fname)
    print(pad)
    print(pad.stem)
    print(pad.parent)

    df = pd.read_csv(fname, ";")
    print(df.head())

    print(df.aantal.sum())

    # df = pd.read_csv("myfile.csv", delimiter=";", dtype="str")

    file_in = pd.read_csv(fname, delimiter=";")
    ordernummer = pad.stem

    file_in.tail()
    mes = 6
    aantal_banen = 6*6  # int(input("aantal_banen: >")) ##tijdelijk
    aantal_per_lijst = mes

    totaal = file_in.aantal.sum()
    print(totaal)
    row = len(file_in)
    print(row)
    opb = ongeveer_per_baan = (totaal // aantal_banen)
    print(f'aantal rollen= {row}')
    afwijking = 0  # mag niet kleiner zijn dan kleinste rol

    stans_tussen = 1  # normaal waarde = 1 , geursamples is 30

    print(f'totaal van lijst is {totaal} en het gemiddelde over {aantal_banen} banen is {opb}')

    benamingen = [f'tmp{naam}.csv' for naam in range(1, aantal_banen + 1)]
    print(benamingen)

    a = 0

    begin_eind_lijst = []
    be_LIJST = []

    for num in range(len(file_in)):
        b = file_in.aantal.iloc[a:(num + 1)].sum()
        # print(a, num)
        #     print(b)

        if num == (len(file_in) - 1):
            c = file_in.aantal.iloc[a:num].sum()
            begin_eind_lijst.append([c, a, num + 1])
            be_LIJST.append([a, num + 1])

            csv_naam = f'tmp/tmp{a:>{0}{4}}.csv'
            print(csv_naam)
            file_in.iloc[a:(num + 1)].to_csv(csv_naam)
            print("einde")



        elif b >= opb + afwijking:

            csv_naam = f'tmp/tmp{a:>{0}{4}}.csv'
            print(csv_naam)
            file_in.iloc[a:(num + 1)].to_csv(csv_naam)

            begin_eind_lijst.append([b, a, num])
            be_LIJST.append([a, num + 1])
            be_LIJST.append(f'[{a}:{num}]')
            a = num + 1

        continue

    split_csv = [x for x in os.listdir("tmp") if x.endswith(".csv")]
    print(f'split_csv {split_csv}')
    lijst_lengte = len(split_csv)

    use = lijst_lengte // aantal_per_lijst
    print(f'var=use {use}')
    # ------------------------------------------------

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


        # ___________________________________________________________________________________________
        def print_noshirt_rolls(colorcode, beeld, aantal):
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


        df = trespa_lijst[["Colorcode", "beeld", "aantal"]]
        df.to_csv("lijst_in.csv", index=0)

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

    # __________________________

    print(begin_eind_lijst)
    print(be_LIJST)
    print(be_LIJST[0])
    print(be_LIJST[0][1:])
    print(be_LIJST[0][:1])

    begin = be_LIJST[0][1:]
    eind = be_LIJST[0][:1]
    print(len(begin_eind_lijst))

    # _______________________________________________________________________________________________
    if len(benamingen) == len(split_csv):
        print("-" * 80)
        print(f"{len(benamingen)} zijn er {len(split_csv)} gemaakt. Aantal banen klopt")
        print("-" * 80)
    else:
        print("-" * 80)
        print(f"geen match, ipv {len(benamingen)} zijn er {len(split_csv)} gemaakt.")
        print("-" * 80)

    vdp_csv = [x for x in os.listdir("vdps") if x.endswith(".csv")]
    print(vdp_csv)

    gesplitste_lijst = []
    begin = 0
    eind = aantal_per_lijst
    for index in range(use):
        gesplitste_lijst.append(vdp_csv[begin:eind])
        begin += aantal_per_lijst
        eind += aantal_per_lijst

    if mes == 4:

        read_out_4(gesplitste_lijst, ordernummer)

        # leegmaken vdps
        for file in vdp_csv:
            naam = f'vdps/{file}'
            if os.path.exists(naam):
                os.remove(naam)
            else:
                print("no files in dir vdps")

        # os.remove("lijst_in.csv")


        VDP_final = [x for x in os.listdir("VDP_map") if x.endswith(".csv")]
        print(VDP_final)

        wikkel_4_baans_tc(VDP_final, pad, Etiketten_Y, inloop)

    elif mes == 6:

        read_out_6(gesplitste_lijst, ordernummer)

        # leegmaken vdps
        for file in vdp_csv:
            naam = f'vdps/{file}'
            if os.path.exists(naam):
                os.remove(naam)
            else:
                print("no files in dir vdps")

        os.remove("lijst_in.csv")

        VDP_final = [x for x in os.listdir("VDP_map") if x.endswith(".csv")]
        print(VDP_final)

        wikkel_6_baans_tc(VDP_final, pad, Etiketten_Y, inloop)




    summary = [x for x in os.listdir("tmp") if x.endswith(".csv")]
    summary = sorted(summary)

    sum_lijst_vert = []
    count = 0

    for naam in summary:
        df = f'df{count}'
        print(df)
        df = pd.read_csv(f'tmp/{naam}', encoding="utf-8")
        #     df2 = pd.DataFrame([[f'{ordernummer}_baan_{count+1}']], dtype="str")
        df2 = pd.DataFrame([[f'{ordernummer}_baan_{count + 1} | {df.aantal.sum()} etiketten']], dtype="int")
        print(df.aantal.sum())
        sum_lijst_vert.append(df2)
        sum_lijst_vert.append(df)

        count += 1

        sam2 = pd.concat(sum_lijst_vert, axis=0).to_csv(f"{pad.parent}/{ordernummer}_summary.csv", ";")

    dir_names_lijst_to_be_cleaned = [
                                        "tmp",
                                        "file_out/vert",
                                        "file_out/hor",
                                        "file_out",
                                        "vdps",

    ]

    cleaning_paden_met_Dir_lijst = [Path(wdir, dirnaam) for dirnaam in dir_names_lijst_to_be_cleaned]

    for file_pad in cleaning_paden_met_Dir_lijst:
        cleaner(file_pad)

    for file_pad in cleaning_paden_met_Dir_lijst:
        file_pad.rmdir()
