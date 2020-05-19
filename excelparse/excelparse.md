# excelparse
Parse excel test.

## 0. excel notes
- excel: excel文件
- workbook: 工作簿
- sheet：工作表
- cell：单元格，存储数据对象

## 1. xlrd
### 1.1. read
| method | notes | 
| --- | --- | 
| open_workbook() | 打开指定的Excel文件，返回一个Book对象 | 
| Book.nsheets  | 返回Sheet的数目 | 
| Book.sheets() | 返回所有Sheet对象的list | 
| Book.sheet_by_index(index)   | 返回指定索引处的Sheet | 
| Book.sheet_names()  | 返回所有Sheet对象名字的list | 
| Book.sheet_by_name(name) | 根据指定Sheet对象名字返回Sheet | 

## 2. pandas