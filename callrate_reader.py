import pathlib
import csv
import os

from pathlib import Path

search_path = Path('/Users/joeychou/Documents/OneDrive - ジェネシスヘルスケア株式会社/ドキュメント/Ganesha_web02_backup/old')

i = 0
callrate_data = []
genotype_data = []
phenotype_data =[]
filename = ''

def write_into_csv(file_path, fieldnames, data):
    with open(file_path, 'w', newline='') as destination_file:
        destination_writer = csv.DictWriter(destination_file, fieldnames=fieldnames)
        destination_writer.writeheader()
        destination_writer.writerows(data)
    destination_file.close()

with open('/Users/joeychou/Downloads/missing_samples.txt') as source_file:
    source_reader = csv.reader(source_file)
    for kit_code in source_reader:
        print(f'kit code {kit_code[0]}')
        for textFileObj in search_path.glob('*CallRate*.over'):
            if os.stat(textFileObj).st_size != 0:
                with open(textFileObj) as t:
                    reader = csv.DictReader(t)
                    sampleCode, ChipCallrate, ProductCallrate, Status, StatusID = reader.fieldnames
                    for row in reader:
                        if kit_code[0] in row[sampleCode]:
                            i = i + 1
                            print(textFileObj)
                            print(kit_code[0]+","+row[ChipCallrate]+","+row[ProductCallrate]+","+row[Status]+","+row[StatusID])
                            d = {
                                    'SampleCode': kit_code[0],
                                    'ChipCallrate': row[ChipCallrate],
                                    'ProductCallrate': row[ProductCallrate],
                                    'Status': row[Status],
                                    'StatusID': row[StatusID]
                                }
                            callrate_data.append(d)
                            filename = os.path.basename(textFileObj)
                            print(filename[0:4])

        for textFileObj in search_path.glob(filename[0:4]+'*Genotype.csv.over'):
            if os.stat(textFileObj).st_size != 0:
                with open(textFileObj) as t:
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
                            genotype_data.append(d)
                    if j > 0:
                        print(f'Total {str(j)} genes are found in {textFileObj}!')

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
                            phenotype_data.append(d)
                    if k > 0:
                        print(f'Total {str(k)} units are found in {textFileObj}!')

write_into_csv('/Users/joeychou/Downloads/missing_CallRate.csv', ['SampleCode','ChipCallrate','ProductCallrate','Status','StatusID'], callrate_data)
write_into_csv('/Users/joeychou/Downloads/missing_Genotype.csv', ['kit_id','NEWGHnumber','allele'], genotype_data)
write_into_csv('/Users/joeychou/Downloads/missing_Phenotype.csv', ['kit_id','unit_id','level_id','population_id','score','odds'], phenotype_data)

source_file.close()
print(f'Total {str(i)} kits are found!')
