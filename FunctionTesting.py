pairs_BoundaryValueAnalysis = [(-0.1, 12), (0, 12), (0.1, 12), (5, 12), (5.9, 12), (6, 12), 
(6.1, 12), (8.4, 12), (8.5, 12), (8.6, 12), (9.9, 12), (10, 12), (10.1, 12), (5, -1), 
(5, 0), (5, 1), (5, 11), (5, 12), (5, 13), (5, 15), (5, 16), (5, 17), 
(5, 19), (5, 20), (5, 21), (5, 22), (5, 23), (5, 24), (5, 25)]

pairs_DecisionTableTesting = [(-1, 12), (11, 12), (5, -1), (5, 25), (3, 6), (3, 14), (3, 18),
(3, 22), (7, 6), (7, 18), (7, 14), (9, 6), (9, 18), (7, 22), (9, 14), (9, 22)]

for IMDB, HOURSTART in pairs_BoundaryValueAnalysis:
    if (IMDB < 0) or (IMDB > 10) or (HOURSTART < 0) or (HOURSTART > 24):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", -1)
    elif (IMDB < 6) or (IMDB < 8.5 and ( HOURSTART <12 or ( HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 0)
    elif ((IMDB < 8.5) and ( HOURSTART >= 12 and HOURSTART <= 16)) or (IMDB > 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 1)      
    else:
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 2) 

for IMDB, HOURSTART in pairs_DecisionTableTesting:
    if (IMDB < 0) or (IMDB > 10) or (HOURSTART < 0) or (HOURSTART > 24):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", -1)
    elif (IMDB < 6) or (IMDB < 8.5 and ( HOURSTART <12 or ( HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 0)
    elif ((IMDB < 8.5) and ( HOURSTART >= 12 and HOURSTART <= 16)) or (IMDB > 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 1)      
    else:
        print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 2) 
