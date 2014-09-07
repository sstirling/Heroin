import csv
import json

stories = []

with open('../data/heroin.csv','rb') as file:
    rows = csv.reader(file)
    for row in rows:
        story = {}
        if row[0] == 'Timestamp':
            continue
        story['timestamp'] = row[0]
        story['name'] = row[1]
        story['age'] = row[2]
        story['gender'] = row[3]
        story['town'] = row[4]
        story['story'] = row[5]
        story['quote'] = row[6]
        story['category'] = row[7].lower()
        if story['category'] == 'significant other':
            story['category'] = 'significant_other'
        if row[8]:
            story['second_category'] = row[8]
    
        stories.append(story)

json = json.dumps(stories)
print json

output = open('../data/stories.json','wb')

output.write(json)

output.close()