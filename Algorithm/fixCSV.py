import csv, re
f = open('train_data.csv',  encoding="utf8")
print("opened file")
reader = csv.reader(f)
print("read file")
writer = csv.writer(open("train_data_fixed.csv", "w"), lineterminator = '\n')
print("opened writer")
for row in reader:
    row[0] = re.sub(r'[^a-zA-Z0-9\s]', '', row[0])
    row[1] = re.sub(r'[^a-zA-Z0-9\s]', '', row[1])
    # merge all but last two elements of row into row[0]
    if len(row) > 2:
        while not row[1] in ["Left"," Left", "Right", " Right", " Auth", "Auth", " Center", "Center", "Liberal", " Liberal"]:
            row[0] = ''.join(row[1])
            print(row[0])
            row.pop(1)
    # check if row[1] contains """ and if so, merge into row[0]
    # deletes all commas in row[0]
    # remove unicode character u3000
    row[0] = re.sub(u'\u3000', '', row[0])
    # remove unicode character u202f
    row[0] = re.sub(u'\u202f', '', row[0])
    # remove all emojis
    row[0] = re.sub(r'[^\x00-\x7F]+', '', row[0])
    row[0] = re.sub(r'\"', '', row[0])
    print(row)
    if len(row) < 4:
        writer.writerow(row)