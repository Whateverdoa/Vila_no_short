import pytest
from pathlib import Path
import pandas as pd
from source.functies_mes import file_splitter, kol_naam_lijst_builder, kolom_naam_gever_voor_4_kolommen, kol_fill_na_dict_builder, wikkel_n_baans_tc
from source.newrolltest import file_name_maker_met_pad
from source.standard_pad_module import paden_dict, pad_naam_lijst

# file_in = pd.read_csv((paden_dict["file_in"] / "202011726_inschiet_test.csv"), delimiter=";")

stringlijst = ['omschrijving_sluit_1', 'sluit_barcode_1', 'pdf_1', 'aantal_1']

kolomlijst2 = 'omschrijving_sluit_1,sluit_barcode_1,pdf_1,aantal_1\n'

dikt_to_test =  {
                "pdf_1": "stans.pdf",
                "pdf_2": "stans.pdf",
                "pdf_3": "stans.pdf",
                "pdf_4": "stans.pdf",
            }

padvoortest= paden_dict["pad_VDP_map"]

mes=4


def test_kol_naam_lijst_builder():
    expected = stringlijst
    namen = kol_naam_lijst_builder(1)
    assert namen == expected


def test_kolom_naam_gever_voor_4_kolommen():
    expected = kolomlijst2
    namen = kolom_naam_gever_voor_4_kolommen(1)
    assert namen == expected


def test_kol_fill_na_dict_builder():
    expected = dikt_to_test
    namen = kol_fill_na_dict_builder(4)
    assert namen == expected

file= padvoortest.glob("*csv")
print(file)

def test_wikkel_n_baans():

    expected = (",0,,stans.pdf" * mes) +"\n"
    namen = wikkel_n_baans_tc(file, 10, 10, 4, padvoortest)
    assert namen == expected

# def test_file_name_maker_pad():
#     expected = [r"C:\Users\Dhr. Ten Hoonte\PycharmProjects\Werk_projekten\Vila_no_short\testing_map\VDP_map\mike_00001.csv"]
#     namen = file_name_maker_met_pad(1,padvoortest,"mike")
#     assert namen == expected

# def test_splitter():
#     expected = []
#     namen = file_splitter(file_in, 14333, -333 )
#     assert namen == expected


