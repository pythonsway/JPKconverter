import csv
import glob
import os
import re
import time

kaper = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'kaper'))
schemat = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'schemat'))
plikiKaper0 = glob.glob(kaper + '\\*.txt')
plikiKaper = [[plikiKaper0[0], 13, -6, [1, 9, 7, 8, 4, 2, 3, 13, 14]],
              [plikiKaper0[1], 17, -6, [1, 10, 7, 8, 4, 2, 3, 14, 15]]]
plikSchemat = glob.glob(schemat + '\\*.csv')


def main():
    """ Generates pre-prepared 'JPK.csv' """
    for plik in plikiKaper:
        with open(plik[0], 'r') as in_text, open(plik[0] + '.csv', 'w', newline='') as out_csv:
            in_reader = list(csv.reader(in_text, delimiter='|'))
            out_writer = csv.writer(out_csv, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            rNip = re.compile(r'(\d{3})(?:-)(\d{2,3})(?:-)(\d{2})(?:-)(\d{2,3})')
            rKs = re.compile(r'(\d+)\s(\d+)')
            for row in in_reader[plik[1]:plik[2]]:
                stripped = [i.strip() for i in row]
                reordered = [stripped[i] for i in plik[3]]
                noNip = [rNip.sub(r'\1\2\3\4', i) for i in reordered]
                noKs = [rKs.sub(r'\1\2', i) for i in noNip]
                brak = ['BRAK' if not i else i for i in noKs]
                out_writer.writerow(brak)
    time.sleep(1)
    interestingFiles = glob.glob(kaper + '\\*.csv')
    with open(kaper + '\\JPK-.csv', 'w', newline='', encoding='utf-8') as csvAll, \
            open(plikSchemat[0], 'r', newline='', encoding='utf-8') as csvSchemat:
        inSchemat = csv.reader(csvSchemat)
        inSchemat4 = [row for idx, row in enumerate(inSchemat) if idx in range(4)]
        csvAllIn = csv.writer(csvAll)
        csvAllIn.writerows(inSchemat4)
        tabulator = (';' * 12)
        for out_csv in interestingFiles:
            with open(out_csv, 'r') as intersetingFile:
                for row in intersetingFile:
                    csvAll.write(tabulator + row)
            csvAll.write(tabulator + ';;' + 'VAT23 K_19-20 i K_45-46' + (';' * (68 - 15)) + '\n')
            tabulator = (';' * 51)
    print('Done.')
    time.sleep(2)


if __name__ == '__main__':
    main()
