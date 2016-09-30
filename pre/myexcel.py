# -*- coding: utf-8 -*-
import xlrd
import xlwt
from xlutils.copy import copy
class myexcel:
    # myexcel_dir="F:\study\excel"
    # def __init__(self,path=myexcel_dir):
    #   self.path=path

    def read_data(self,row,column):
        paramer=xlrd.open_workbook("./data/test.xls")
        paramer_sheet =paramer.sheets()[0]
        paramer_rows =paramer_sheet.nrows
        data=paramer_sheet.cell_value(row,column)
        #data.append(paramer_sheet.cell_value(row,column))
        return data

    def get_rows(self):
        paramer=xlrd.open_workbook("./data/test.xls")
        paramer_sheet =paramer.sheets()[0]
        paramer_rows =paramer_sheet.nrows
        return paramer_rows

    def write_data(self,name,data):
        oldWb = xlrd.open_workbook("./data/test.xls")
        paramer_sheet =oldWb.sheets()[0]
        paramer_rows =paramer_sheet.nrows
        newwb=copy(oldWb)
        new_sheet=newwb.get_sheet(0)
        new_sheet.write(paramer_rows,0,name)
        new_sheet.write(paramer_rows,1,data)
        newwb.save('./data/test.xls')

    # def read_casedata(self):
    #   data=[]
    #   paramer=xlrd.open_workbook("F:\study\python2\\report_test\\test.xls")
    #   paramer_sheet =paramer.sheets()[0]
    #   paramer_rows =paramer_sheet.nrows
    #   print paramer_rows

    #   for row in range(0,paramer_rows):
    #       data.append(paramer_sheet.cell_value(row,1))
    #   return data

    # def read_casename(self):
    #   data=[]
    #   paramer=xlrd.open_workbook("F:\study\python2\\report_test\\test.xls")
    #   paramer_sheet =paramer.sheets()[0]
    #   paramer_rows =paramer_sheet.nrows
    #   print paramer_rows

    #   for row in range(0,paramer_rows):
    #       data.append(paramer_sheet.cell_value(row,0))
    #   return data
        
if __name__ == '__main__':
    print"中文"
    my=myexcel()
    x=my.read_data(1,1+2)
    print x






