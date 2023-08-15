import csv

class CsvUtil():
    def __init__(self,filepath):
        self.filepath=filepath
    def list_data(self):
        #读取csv文件
        value_rows=[]
        with open(self.filepath,"r",encoding="utf-8") as f:
            f_csv=csv.reader(f)
            next(f_csv)
            for i in f_csv:
                value_rows.append(i)
        return value_rows
