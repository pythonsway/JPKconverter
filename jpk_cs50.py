import os
import glob
import re
import csv

kaper = "kaper\\"
# plikiKaper = [os.path.join(kaper,plik) for plik in os.listdir(kaper) if fil.endswith(".txt")]

# NazwyTxt = ["Eksport_RejestrSprzedazy*.txt", "Eksport_RejestrZakupu*.txt"]
nazwyTxt = (("SprzKaper", "Eksport_RejestrSprzedazy*.txt", 13, -7),
            ("ZakKaper", "Eksport_RejestrZakupu*.txt", 17, -7))
# plikiKaper = [glob.glob(kaper + nazwa) for txt, nazwa, start, end in nazwyTxt]
plikiKaper = glob.glob(kaper + "*.txt")
# offile=open("output.csv", "wb")
print(nazwyTxt)
print(plikiKaper)

# for plik in plikiKaper:
#     with open(plik, 'r') as f:
#         content = f.readlines()
#         lines_of_data = content.splitlines()
#         writer=csv.writer(offile,delimiter='|',quotechar='"',quoting=csv.QUOTE_ALL)
#         writer.writerows(map(lambda line:re.split("\s\s\s\s+",line.strip()),lines_of_data))

# with open('test.txt', 'r') as f:
#     content = f.readlines()
#     output_line = "".join([line.split(':')[1].replace('\n',';').strip() for line in content[0:4]])
#     print(output_line)

for plik in plikiKaper:

    with open(plik, "r") as in_text, open(plik + ".csv", "w", newline='') as out_csv:
        in_reader = csv.reader(in_text, delimiter='|')
        out_writer = csv.writer(out_csv, delimiter=';',
                                quoting=csv.QUOTE_MINIMAL)
        for row in in_reader:
            stripped = [item.strip() for item in row]
            out_writer.writerow(stripped)


# def picklines(thefile, whatlines):
#     return [x for i, x in enumerate(thefile) if i in whatlines]


# def main():
#     pass


# if __name__ == '__main__':
#     main()
