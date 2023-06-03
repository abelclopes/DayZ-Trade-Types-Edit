
class ConvertCsvToTraderFIle:

    @staticmethod
    def csvtotxt(filename):    
        csv_reader = open(filename, 'r')
        lines = csv_reader.readlines()
        tradename: str = ""
        catName = ""
        count = 0

        tradeNames = []

        for row in lines:
            count += 1
            if count == 1:
                continue
            linhaAtual = row.split(";")
            line1 = "<Trader>{}".format(linhaAtual[1])
            if tradename == line1:
                continue

            if 'Trader;Category' and count > 1:

                line = "<Trader>{}".format(linhaAtual[1])
                tradename = line
                tradeNames.append(linhaAtual[1])
                continue
            else:
                continue

        newFile: [str] = []
        for tn in tradeNames:

            trad = "<Trader>{}".format(tn)
            print(trad)
            newFile.append(trad)
            for line in lines:
                linha = line.split(";")
                cat = "\t<Category>{}".format(linha[2])
                if line == "":
                    continue

                if linha[1] == tn:
                    if catName == cat and len(linha) >= 6:
                        newItemLine = "\t\t{},{},{},{}".format(linha[3],linha[4],linha[5],linha[6])
                        newFile.append(newItemLine)
                    else:
                        catName = "\t<Category>{}".format(linha[2])
                        newFile.append(catName)
                    continue
                else:
                    continue


        print(newFile)
        resultFyle = open("trade.txt", 'w')

        for r in newFile:
            resultFyle.write(r + "\n")
        resultFyle.close()
