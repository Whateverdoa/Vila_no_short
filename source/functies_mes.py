import pandas as pd


def file_splitter(file_in: pd.DataFrame, opb, afwijking):

    aantal_files_in_datadrame_file_in = len(file_in)
    a = 0

    begin_eind_lijst = []
    be_LIJST = []

    for num in range(aantal_files_in_datadrame_file_in):
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

    return begin_eind_lijst


def read_out_4(lissst, ordernum):
    """builds  and concats 4files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]

        color_1 = f"VDP_{index + 1}"


        file_1 = pd.read_csv(f"vdps/{a}", ";", dtype="str")
        file_2 = pd.read_csv(f"vdps/{b}", ";", dtype="str")

        file_3 = pd.read_csv(f"vdps/{c}", ";", dtype="str")
        file_4 = pd.read_csv(f"vdps/{d}", ";", dtype="str")

        samengevoeg_4 = pd.concat([file_1, file_2, file_3, file_4], axis=1)

        samengevoeg_4.columns = [
            "omschrijving_1",
            "barcode_1",
            "aantal_1",
            "beeld_1",
            "omschrijving_2",
            "barcode_2",
            "aantal_2",
            "beeld_2",
            "omschrijving_3",
            "barcode_3",
            "aantal_3",
            "beeld_3",
            "omschrijving_4",
            "barcode_4",
            "aantal_4",
            "beeld_4"
        ]

        samengevoeg_4.fillna(
            {
                "beeld_1": "stans.pdf",
                "beeld_2": "stans.pdf",
                "beeld_3": "stans.pdf",
                "beeld_4": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_4.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")


def wikkel_4_baans_tc(input_vdp_lijst, padth, data_uit_vdp, inloop):
    """last step voor VDP adding in en uitloop"""

    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{padth.parent}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;sluit_barcode_1;aantal_1;pdf_1;omschrijving_2;sluit_barcode_2;aantal_2;pdf_2;omschrijving_3;sluit_barcode_3;aantal_3;pdf_3;omschrijving_4;sluit_barcode_4;aantal_4;pdf_4\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg

            target.writelines(readline[1:data_uit_vdp])

            target.writelines(
                "0;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf\n"
                * (inloop - data_uit_vdp)
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf\n"
                * (inloop - 10)
            )  # uitloop

            target.writelines(readline[1:10])


def read_out_6(lissst, ordernum):
    """builds  and concats 4files over axis 1"""
    for index in range((len(lissst))):
        print(index)
        a = lissst[index][0]
        b = lissst[index][1]
        c = lissst[index][2]
        d = lissst[index][3]
        e = lissst[index][4]
        f = lissst[index][5]

        color_1 = f"VDP_{index + 1}"
        color_2 = f"{index}b"

        file_1 = pd.read_csv(f"vdps/{a}", ";" ,dtype="str")
        file_2 = pd.read_csv(f"vdps/{b}", ";" ,dtype="str")

        file_3 = pd.read_csv(f"vdps/{c}", ";",dtype="str")
        file_4 = pd.read_csv(f"vdps/{d}", ";",dtype="str")

        file_5 = pd.read_csv(f"vdps/{e}", ";",dtype="str")
        file_6 = pd.read_csv(f"vdps/{f}", ";",dtype="str")

        samengevoeg_4 = pd.concat(
            [file_1, file_2, file_3, file_4, file_5, file_6], axis=1
        )

        samengevoeg_4.columns = [
            "omschrijving_1",
            "barcode_1",
            "aantal_1",
            "beeld_1",
            "omschrijving_2",
            "barcode_2",
            "aantal_2",
            "beeld_2",
            "omschrijving_3",
            "barcode_3",
            "aantal_3",
            "beeld_3",
            "omschrijving_4",
            "barcode_4",
            "aantal_4",
            "beeld_4",
            "omschrijving_5",
            "barcode_5",
            "aantal_5",
            "beeld_5",
            "omschrijving_6",
            "barcode_6",
            "aantal_6",
            "beeld_6",
        ]

        samengevoeg_4.fillna(
            {
                "beeld_1": "stans.pdf",
                "beeld_2": "stans.pdf",
                "beeld_3": "stans.pdf",
                "beeld_4": "stans.pdf",
                "beeld_5": "stans.pdf",
                "beeld_6": "stans.pdf",
            },
            inplace=True,
        )

        samengevoeg_4.to_csv(f"VDP_map/{ordernum}_{color_1}.csv", ";")



# todo onderste wikkel aanpassen


def wikkel_6_baans_tc(input_vdp_lijst, padth, data_uit_vdp, inloop, mes):
    """last step voor VDP adding in en uitloop"""


    for index in range(len(input_vdp_lijst)):
        file_naam = f"{input_vdp_lijst[index]}"

        with open(f"VDP_map/{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        with open(f"{padth.parent}/def_{file_naam}", "w", encoding="utf-8") as target:
            target.writelines(
                "id;omschrijving_1;sluit_barcode_1;aantal_1;pdf_1;omschrijving_2;sluit_barcode_2;aantal_2;pdf_2;omschrijving_3;sluit_barcode_3;aantal_3;pdf_3;omschrijving_4;sluit_barcode_4;aantal_4;pdf_4;omschrijving_5;sluit_barcode_5;aantal_5;pdf_5;omschrijving_6;sluit_barcode_6;aantal_6;pdf_6\n"
            )
            # regel staat zo omdat ik kolomnaam id nog niet erin krijg , dit is opgelost. moet hhet alleen nog overal gaan gebruiken.

            target.writelines(readline[1:data_uit_vdp])

            target.writelines(
                "0;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf\n"
                * (inloop - data_uit_vdp)
            )  # inloop

            target.writelines(readline[1:])  # bestand

            target.writelines(
                "0;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf;;;;stans.pdf\n" * (inloop - 10)
            )  # uitloop

            target.writelines(readline[1:10])

# todo: deze?

def kol_naam_lijst_builder(mes_waarde=1):
    kollomnaamlijst = []

    for count in range(1, mes_waarde + 1):
        # 5 = len (list) of mes
        omschrijving_sluit = f"omschrijving_sluit_{count}"
        sluit_barcode = f"sluit_barcode_{count}"
        beeld = f"pdf_{count}"
        aantal = f"aantal_{count}"

        kollomnaamlijst.append(omschrijving_sluit)
        kollomnaamlijst.append(sluit_barcode)
        kollomnaamlijst.append(beeld)
        kollomnaamlijst.append(aantal)

    # return ["id"] + kollomnaamlijst omschrijving_sluit' 'sluit_barcode' 'beeld' 'aantal
    return kollomnaamlijst


def lees_per_lijst(lijst_met_posix_paden, mes_waarde):
    """1 lijst in len(lijst) namen uit
    input lijst met posix paden"""
    count = 1
    concatlist = []
    for posix_pad_naar_file in lijst_met_posix_paden:
        # print(posix_pad_naar_file)
        naam = f'file{count:>{0}{4}}'
        # print(naam)
        naam = pd.read_csv(posix_pad_naar_file)
        concatlist.append(naam)
        count += 1
    kolomnamen = kol_naam_lijst_builder(mes_waarde)
    lijst_over_axis_1 = pd.concat(concatlist, axis=1)
    lijst_over_axis_1.columns = [kolomnamen]

    # return lijst_over_axis_1.to_csv("test2.csv", index=0)
    return lijst_over_axis_1


def horizontaal_samenvoegen(opgebroken_posix_lijst, map_uit, mes):
    count = 1
    for lijst_met_posix in opgebroken_posix_lijst:
        vdp_hor_stap = f'vdp_hor_stap_{count:>{0}{4}}.csv'
        vdp_hor_stap = map_uit/ vdp_hor_stap
        # print(vdp_hor_stap)
        df = lees_per_lijst(lijst_met_posix, mes)
        # print(df.tail(5))

        lees_per_lijst(lijst_met_posix, mes).to_csv(vdp_hor_stap, index=0)

        count += 1
    return 0


def stapel_df_baan(naam,lijstin, ordernummer, map_uit):
    stapel_df = []
    for lijst_naam in lijstin:
        # print(lijst_naam)
        to_append_df = pd.read_csv(
            f"{lijst_naam}", ",", dtype="str", index_col=0)
        stapel_df.append(to_append_df)
    pd.concat(stapel_df, axis=0).to_csv(f"{map_uit}/{naam}_{ordernummer}.csv", ",")
    return pd.DataFrame(stapel_df)


def kolom_naam_gever_voor_4_kolommen(mes=1):
    """supplies a specific string  met de oplopende kolom namen num_1, pdf_1, omschrijving_1 etc"""

    def list_to_string(functie):
        kolom_namen = ""
        for kolomnamen in functie:
            kolom_namen += kolomnamen + ","
        return kolom_namen[:-1] + "\n"

    kollomnaamlijst = []

    for count in range(1, mes + 1):
        # 5 = len (list) of mes
        omschrijving_sluit = f"omschrijving_sluit_{count}"
        sluit_barcode = f"sluit_barcode_{count}"
        beeld = f"pdf_{count}"
        aantal = f"aantal_{count}"

        kollomnaamlijst.append(omschrijving_sluit)
        kollomnaamlijst.append(sluit_barcode)
        kollomnaamlijst.append(beeld)
        kollomnaamlijst.append(aantal)

    namen = list_to_string(kollomnaamlijst)

    return namen


def wikkel_n_baans_tc(input_vdp_posix_lijst, etiketten_Y, in_loop, mes, pad_VDP_DEF):
    """last step voor VDP adding in en uitloop"""

    inlooplijst = (",0,,stans.pdf" * mes)
    inlooplijst = inlooplijst + "\n" # -1 removes empty column in final file

    for file_naam in input_vdp_posix_lijst:
        with open(f"{file_naam}", "r", encoding="utf-8") as target:
            readline = target.readlines()

        nieuwe_vdp_naam = pad_VDP_DEF / file_naam.name
        with open(nieuwe_vdp_naam, "w", encoding="utf-8") as target:
            target.writelines(kolom_naam_gever_voor_4_kolommen(mes))

            target.writelines(readline[1:etiketten_Y + 1])
            # target.writelines(readline[16:(etikettenY+etikettenY-8)])

            target.writelines(
                (inlooplijst) * in_loop)  # inloop
            print("inloop maken")
            target.writelines(readline[1:])  # bestand

            target.writelines(
                (inlooplijst) * in_loop)  # inloop  # uitloop
            print("uitloop maken")
            target.writelines(readline[-etiketten_Y:])

    return inlooplijst



def kol_fill_na_dict_builder(mes=1):
    """{"pdf_1": "stans.pdf", "pdf_2": "stans.pdf"}"""

    keys = [f'pdf_{i + 1}' for i in range(mes)]
    values = ['stans.pdf' for i in range(mes)]
    fillna_dict = dict(zip(keys, values))

    return fillna_dict


