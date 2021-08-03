import pathlib
import csv
import os

from pathlib import Path

search_path = Path('/Users/joeychou/Documents/OneDrive - ジェネシスヘルスケア株式会社/ドキュメント/Ganesha_web02_backup/old')

i = 0
data = []
with open('/Users/joeychou/Downloads/missing_samples.txt') as source_file:
    source_reader = csv.reader(source_file)
    for kit_code in source_reader:
        print(f'kit code {kit_code[0]}')
        for textFileObj in search_path.glob(filename[0:4]+'*Phenotype.csv.over'):
            if os.stat(textFileObj).st_size != 0:
                with open(textFileObj) as t:
                    reader = csv.DictReader(t)
                    kit_id,unit_id,level_id,population_id,score,odds = reader.fieldnames
                    k = 0
                    for row in reader:
                        if kit_code[0] in row[kit_id]:
                            k = k + 1
                            d = {
                                    'kit_id': kit_code[0],
                                    'unit_id': row[unit_id],
                                    'level_id': row[level_id],
                                    'population_id': row[population_id],
                                    'score': row[score],
                                    'odds': row[odds]
                                }
                            data.append(d)
                    if k > 0:
                        print(f'Total {str(k)} units are found in {textFileObj}!')

fieldnames = ['kit_id','unit_id','level_id','population_id','score','odds']
with open('/Users/joeychou/Downloads/missing_Phenotype.csv', 'w', newline='') as destination_file:
    destination_writer = csv.DictWriter(destination_file, fieldnames=fieldnames)
    destination_writer.writeheader()
    destination_writer.writerows(data)

source_file.close()
destination_file.close()
print(f'Total {str(i)} kits are found!')
