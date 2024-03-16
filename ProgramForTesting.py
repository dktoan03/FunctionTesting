with open("BoundaryValueAnalysis.txt", "r") as file_object:
    file_content = file_object.read()
pairs_BoundaryValueAnalysis = eval(file_content)

with open("DecisionTableTesting.txt", "r") as file_object:
    file_content = file_object.read()
pairs_DecisionTableTesting = eval(file_content)

for IMDB, HOURSTART in pairs_BoundaryValueAnalysis:
    if (IMDB < 0) or (IMDB > 10) or (HOURSTART < 0) or (HOURSTART > 24):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", -1)
    elif (IMDB < 6) or (IMDB < 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 0)
    elif ((IMDB < 8.5) and (HOURSTART >= 12 and HOURSTART <= 16)) or (IMDB > 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 1)
    else:
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 2)

for IMDB, HOURSTART in pairs_DecisionTableTesting:
    if (IMDB < 0) or (IMDB > 10) or (HOURSTART < 0) or (HOURSTART > 24):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", -1)
    elif (IMDB < 6) or (IMDB < 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 0)
    elif ((IMDB < 8.5) and (HOURSTART >= 12 and HOURSTART <= 16)) or (IMDB > 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 1)
    else:
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 2)