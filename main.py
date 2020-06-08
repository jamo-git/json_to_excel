from getjsondata import GetJsonData
from save_excel import ExcelBook

USERJSONFILE = "./json/users.json"
XLSXFILE = "./xlsx/users.xlsx"


def handleJson(url):
    users = GetJsonData(url)
    try:
        entriesjson = users.loadJsonFromFile(USERJSONFILE)
    except Exception as e:
        print(f"Error got: {e}")
        users.download()
        users.saveJsonToFile(USERJSONFILE)
        entriesjson = users.getJson()

    return entriesjson


def makeExcelOfJson(entries, columns, jsondata):
    excel = ExcelBook(None, None)
    excel.initiateXlsx(XLSXFILE)

    counter = 0
    for entry in entries:
        excel.insertData(f"{columns[counter]}1", entry, True)
        counter += 1

    row_counter = 2
    for data in jsondata:
        column_count = 0
        for entry in entries:
            print(f"{columns[column_count]}{row_counter+2}->{data[entry]}")
            excel.insertData(f"{columns[column_count]}{row_counter+2}", data[entry])
            column_count += 1
        row_counter += 1

    excel.closeXlsx()


if __name__ == "__main__":
    jsondata = handleJson("https://jsonplaceholder.typicode.com/users")

    entries = ["id", "name", "username", "email", "phone", "website"]
    columns = ["A", "B", "C", "D", "E", "F"]

    makeExcelOfJson(entries, columns, jsondata)
