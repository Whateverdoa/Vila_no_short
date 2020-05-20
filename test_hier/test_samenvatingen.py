from samenvatingen import summary_tekst_file

test_lijst = ["mike"]

def test_summary_tekst_file():
    arglijst = summary_tekst_file("test","test",*test_lijst)
    expected = "mike"

    assert arglijst == expected


