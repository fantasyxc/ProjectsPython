import xlrd

def readexcel1():
    excel_path = "demo.xlsx"

    # open excel file
    excel_workbook = xlrd.open_workbook(excel_path, encoding_override="utf-8")

    # read sheet list
    all_sheet = excel_workbook.sheets()
    # print(all_sheet)


    for each_sheet in all_sheet:
        print(each_sheet)
        print("sheet名称为：", each_sheet.name) # sheet名称

    for i in range(len(all_sheet)):
        each_sheet_by_index = excel_workbook.sheet_by_index(i)
        print("table name is: {0}, type is: {1}.".format(each_sheet_by_index, type(each_sheet_by_index)))
        print("sheet name is: ", each_sheet_by_index.name)

def readexcel2():
    excel_path = "demo.xlsx"
    excel = xlrd.open_workbook(excel_path, encoding_override="utf-8")

    print("sheet number is: {0}".format(excel.nsheets))

    all_sheet = excel.sheet_names()
    print(all_sheet)

    for each_sheet_by_name in all_sheet:
        print("table name is: {0}, type is: {1}".format(each_sheet_by_name, type(each_sheet_by_name)))



if __name__ == "__main__":
    # print('readexcel1')
    # readexcel1()

    print('readexcel2')
    readexcel2()
