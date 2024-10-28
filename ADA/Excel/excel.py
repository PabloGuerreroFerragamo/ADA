from openpyxl import Workbook
from openpyxl.styles import Font
import time

book = Workbook()#inicializamos nuestro workboock
sheet = book.active#sheet es la hoja activa

sheet['A1']=5 #cuadrante A1
sheet['A2']=10

book.save('prueba_escritura.xlsx')

