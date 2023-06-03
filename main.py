# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

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
            listCtitem =[]
            ic = 0
            for item in ctitem:
                ic += 1
                if item.strip('\n').strip('\t') == "":
                    item = "*"
                listCtitem[ic] = item.strip('\n').strip('\t')

            ctitem = "{};{};{};{}".format(listCtitem[0],listCtitem[1],listCtitem[2],listCtitem[3])
            newLine = "{};{};{};{};".format(count, tempTradeName, tempCatName, ctitem)
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ReadFileTrde()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
