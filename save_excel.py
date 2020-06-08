import xlsxwriter


class ExcelBook:
    def __init__(self, workbook, worksheet):
        self.workbook = workbook
        self.worksheet = worksheet

    def initiateXlsx(self, filename):
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()

    def insertData(self, location, data, bold=False):
        if bold:
            bold = self.workbook.add_format({"bold": True})
            self.worksheet.write(location, data, bold)
        else:
            self.worksheet.write(location, data)

    def closeXlsx(self):
        self.workbook.close()
