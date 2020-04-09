""""this module generates the directories and paths """

from pathlib import Path

# working directory
wdir = Path.cwd()
# lijst met variable namen om naar de paden te verwijzen
pad_naam_lijst = ["pad_sum",
                  "pad_tmp",

                  "verticaal",
                  "horizontaal"
                  "pad_VDP_map",
                  "pad_file_in",
                  "pad_naar_vdps"]

# lijst met alle te gebruiken directories
dir_names_lijst = ["summary",
                   "tmp",
                   "file_out/vert",
                   "file_out/hor",
                   "VDP_map",
                   "file_in",
                   "vdps"]

# list comprehension om alle paden te maken
paden_met_Dir_lijst = [Path(wdir,dirnaam) for dirnaam in dir_names_lijst]

# list comprehension om alle Directories naar de paden te maken
dir_maak_comp_lijst = [dir_to_build.mkdir(parents=True, exist_ok=True) for dir_to_build in paden_met_Dir_lijst]

# dict voor snel opzoeken paden
paden_dict = dict(zip(pad_naam_lijst,paden_met_Dir_lijst))

print(paden_dict)

def cleaner(pad):

    dir_to_empty = sorted(Path(pad).glob('*.csv'))

    for file in dir_to_empty:
        file.unlink()
        # pad.rmdir()  # test of dit werkt eerst csv weg dan dir

    return 0


