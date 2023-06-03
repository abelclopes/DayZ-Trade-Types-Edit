
def ReadFileTrde():
    file1 = open('TraderConfig.txt', 'r')
    Lines = file1.readlines()

    count = 0
    tempTradeName = ""
    tempCatName = ""
    dblines = []
    # Strips the newline character
    for line in Lines:
        count += 1
        if '<Trader>' in line and '<Category>' not in line:
            tempTradeName = line.replace("<Trader>","").strip('\n').strip('\t')
            tempCatName = ""
            print("TRADER: {}".format(tempTradeName))
            continue

        if '<Trader>' not in line and '<Category>' in line:
            tempCatName = line.replace("<Category>","").strip('\n').strip('\t')
            print("TRADER: {}, Category : {}".format(tempTradeName, tempCatName))
            continue
        if '<Trader>' not in line and '<Category>' not in line:
            ctitem = line.split(",")
            listCtitem =""
            ic = 0
            for item in ctitem:
                ic += 1
                if item.strip('\n').strip('\t') == "":
                    item = "*"
                if ic == 1:
                    listCtitem =  "{}".format(item.strip('\n').strip('\t'))
                if ic > 1:
                    listCtitem = "{};{}".format(listCtitem, item.strip().strip('\n').strip('\t'))

            newLine = "{};{};{};{};".format(count, tempTradeName, tempCatName, listCtitem)
            dblines.append(newLine)
            print(newLine)
            continue
      #  print("Line{}: {}".format(count, line.strip()))
    GerarCvs(dblines)
def GerarCvs(lines = []):
    # Open File
    resultFyle = open("output.csv", 'w')

    # Write data to file
    for r in lines:
        resultFyle.write(r + "\n")
    resultFyle.close()
