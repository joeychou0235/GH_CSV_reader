import pathlib
import csv
import os

from pathlib import Path

search_path = Path('/Users/joeychou/Documents/OneDrive - ジェネシスヘルスケア株式会社/ドキュメント/Ganesha_web02_backup/old')

i = 0
data = []
with open('/Users/joeychou/Downloads/missing_samples2.txt') as source_file:
    source_reader = csv.reader(source_file)
    for kit_code in source_reader:
        print(f'kit code {kit_code[0]}')
        for textFileObj in search_path.glob('*Genotype.csv.over'):
            if os.stat(textFileObj).st_size != 0:
                with open(textFileObj) as t:
                    i = i + 1
                    reader = csv.DictReader(t)
                    kit_id, NEWGHnumber, allele = reader.fieldnames
                    j = 0
                    for row in reader:
                        if kit_code[0] in row[kit_id]:
                            j = j + 1
                            d = {
                                    'kit_id': kit_code[0],
                                    'NEWGHnumber': row[NEWGHnumber],
                                    'allele': row[allele]
                                }
                            data.append(d)
                    if j > 0:
                        print(f'Total {str(j)} genes are found in {textFileObj}!')

fieldnames = ['kit_id','NEWGHnumber','allele']
with open('/Users/joeychou/Downloads/missing_Genotype.csv', 'w', newline='') as destination_file:
    destination_writer = csv.DictWriter(destination_file, fieldnames=fieldnames)
    destination_writer.writeheader()
    destination_writer.writerows(data)

source_file.close()
destination_file.close()
print(f'Total {str(i)} kits are found!')
