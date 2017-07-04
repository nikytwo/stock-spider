
if __name__ == '__main__':
    f = open('../stock_list/stock.txt')
    stockList = set()
    for line in f:
        if line == "\n":
            continue
        if line.startswith('3'):
            continue
        stockList.add(line.replace("\n",""))

    for s in stockList:
        print s
