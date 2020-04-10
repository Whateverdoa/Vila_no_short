import pandas as pd
from pathlib import Path
from source.standard_pad_module import *

# noshort_rolls_met_4_kolommen = pd.read_csv(r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Werk_projekten\Vila_no_short\source\file_in\202011726_inschiet.csv", ";", dtype="str")
# print(noshort_rolls_met_4_kolommen.head())


# print(noshort_rolls_met_4_kolommen.columns.values)

# omschrijving_sluit = noshort_rolls_met_4_kolommen.omschrijving_sluit[0]
# sluit_barcode = noshort_rolls_met_4_kolommen.sluit_barcode[0]
# beeld = noshort_rolls_met_4_kolommen.beeld[0]
# aantal_etiketten = noshort_rolls_met_4_kolommen.aantal[0]
#
# rol1 = pd.DataFrame([(omschrijving_sluit, sluit_barcode, beeld, aantal_etiketten)] * int(aantal_etiketten), columns =[1, 2, 3, 4], dtype="str")


def file_name_maker_met_pad(
    amount_of_rolls, posix_destination_pad, filename: "str", exp=".csv"
):
    """a list comprehension to supply names for csv files
    give a start naam and it will generate a list  of names for the amount of rolls """

    man_fac_name_with_path_lijst = []
    for naam in range(amount_of_rolls):
        manufactored_name_with_path = (
            f"{Path(posix_destination_pad / filename)}_{naam+1:>{0}{5}}{exp}"
        )
        # print(manufactored_name_with_path)
        man_fac_name_with_path_lijst.append(manufactored_name_with_path)

    return man_fac_name_with_path_lijst


def rollen_maker(
    basis_csv_bestand_in,
    posix_destination_pad,
    wikkel: int,
    filename: "str",
    exp=".csv",
):

    noshort_rolls_met_4_kolommen = pd.read_csv(
        Path(basis_csv_bestand_in), ";", dtype="str"
    )
    lengte_van_data_frame = len(noshort_rolls_met_4_kolommen)
    print(noshort_rolls_met_4_kolommen.columns.values)

    def file_name_maker_met_pad():
        """a list comprehension to supply names for csv files
        give a start naam and it will generate a list  of names for the amount of rolls """

        man_fac_name_with_path_lijst = []
        for naam in range(lengte_van_data_frame):
            manufactored_name_with_path = (
                f"{posix_destination_pad / filename}_{naam + 1:>{0}{5}}{exp}"
            )
            # print(manufactored_name_with_path)
            man_fac_name_with_path_lijst.append(manufactored_name_with_path)

        return man_fac_name_with_path_lijst

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

    csv_namen = file_name_maker_met_pad()

    for i in range(lengte_van_data_frame):
        omschrijving_sluit = noshort_rolls_met_4_kolommen.omschrijving_sluit[i]
        sluit_barcode = noshort_rolls_met_4_kolommen.sluit_barcode[i]
        beeld = noshort_rolls_met_4_kolommen.beeld[i]
        aantal_etiketten = noshort_rolls_met_4_kolommen.aantal[i]

        csv_naam = csv_namen[i]

        llor = noshort_rolls_4kolommen(
            omschrijving_sluit, sluit_barcode, beeld, aantal_etiketten, wikkel
        )
        llor.to_csv(csv_naam)

    return csv_namen

# testing and running defs

inschiet_file = Path(paden_dict["pad_file_in"] /"202011726_inschiet_met_rolnummer.csv")

destination = paden_dict["pad_tmp"]


rollen_maker(inschiet_file, destination, 4, "tmp1")





