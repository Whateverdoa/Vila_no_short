"""summary  def"""
from pathlib import Path
from tabulate import tabulate



def summary_tekst_file(order_num,pad_uit_parent,*args):


    summary_values_from_arg = []
    for arg in args:
        summary_values_from_arg.append(arg)

    sum_filename_out = f'{order_num}_sum.txt'

    pad_en_file = Path(pad_uit_parent).joinpath(sum_filename_out)

    with open(pad_en_file, 'w', encoding='utf-8') as summary:
        print(f'ordernummer: {order_num}', file=summary)
        print(f'aantal gemaakte vdp\'s = {summary_values_from_arg[8]}')
        print(f'gebruikte csv file = {summary_values_from_arg[13]}', file=summary)
        print("_" * 50, file=summary)

        print(
            f'totaal van lijst is {summary_values_from_arg[0]} en het gemiddelde over {summary_values_from_arg[1] * summary_values_from_arg[2]} banen is {summary_values_from_arg[3]}',
            file=summary)
        print(f'de default afwijking over het gemiddelde is : {summary_values_from_arg[4]}', file=summary)
        print("_" * 50, file=summary)

        print(f'mes: {summary_values_from_arg[5]}', file=summary)
        print(f"aantal vdp's: {summary_values_from_arg[1]}", file=summary)


        print(f'wikkel = {summary_values_from_arg[7]} etiket(ten)', file=summary)
        print(f'extra etiketten per rol = {summary_values_from_arg[8]}', file=summary)

        print(f'inloop en uitloop: {summary_values_from_arg[9]}', file=summary)
        print(f"Y waarde = {summary_values_from_arg[10]}", file=summary)
        print("_" * 50, file=summary)
        print(f'aantal rollen : {summary_values_from_arg[6]} : zie excel print voor rol specificaties', file=summary)
        print("rol __ aantal per rol. NB  index begint hier  bij 0 (dus plus 1 op het einde) ", file=summary)
        # print(summary_values_from_arg[11], file=summary)
        print("", file=summary)
        print(tabulate(summary_values_from_arg[11], headers='keys', tablefmt='psql'),file=summary)
        print("_" * 50, file=summary)
        print("")



        print("aantal staat voor en elke rol op sluit etiket", file=summary)

        print(f'gemaakte files staan in lokatie {pad_uit_parent}', file=summary)
