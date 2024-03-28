def Test(PAIR):
    for IMDB, HOURSTART, ISFAVORITE in PAIR:
        if (IMDB < 0) or (IMDB > 10) or (HOURSTART < 0) or (HOURSTART > 24):
            print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", -1)
        elif (not ISFAVORITE) or (IMDB < 6) or (IMDB < 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
            print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 0)
        elif ((IMDB < 8.5) and (HOURSTART >= 12 and HOURSTART <= 16)) or (IMDB > 8.5 and (HOURSTART < 12 or (HOURSTART > 16 and HOURSTART < 20))):
            print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 1)
        else:
            print(f"IMDB = {IMDB}, HOURSTART = {HOURSTART}", "output = ", 2)

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Chuyển đổi dòng thành tuple và chạy hàm Test
                # Đây là cách đơn giản, nhưng cẩn thận với dữ liệu đầu vào không tin cậy
                pair = eval(line.strip())
                Test(pair)
    except FileNotFoundError:
        print("File not found!")

main('BoundaryValueAnalysis.txt')
main('ControlFlowTesting.txt')
main('DataFlowTesting.txt)
main('DecisionTableTesting.txt')
