import xlrd

class getParcelIDs():
    def importXlsx():
        xlsPath = ("SCOTT COUNTY IA.xlsx")  
        wb = xlrd.open_workbook(xlsPath) 
        sheet = wb.sheet_by_index(0) 
        num_cols = sheet.nrows - 1
        parcels = []
        for i in range(1,num_cols):
            parcels.append(sheet.cell_value(i, 0))
        # postcodes.extend('Postcode')
        return parcels
    def checkDuplicate(inputList):
        results = [] 
        for item in inputList: 
            if item not in results: 
                results.append(item)
        return results 
