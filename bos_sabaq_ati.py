import confyg_1
import xlrd
workbook1 = xlrd.open_workbook(confyg_1.fayl_ati_1)
worksheet1 = workbook1.sheet_by_name(confyg_1.list_ati_1)
workbook2 = xlrd.open_workbook(confyg_1.fayl_ati_2)
worksheet2 = workbook2.sheet_by_name(confyg_1.list_ati_2)
workbook3 = xlrd.open_workbook(confyg_1.fayl_ati_3)
worksheet3 = workbook3.sheet_by_name(confyg_1.list_ati_3)
workbook4 = xlrd.open_workbook(confyg_1.fayl_ati_4)
worksheet4 = workbook4.sheet_by_name(confyg_1.list_ati_4)

def bos_sabaq_ati(x, q, kurs):

    if kurs == 1:
        if str(worksheet1.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 9):
                q = q - 1
                if str(worksheet1.cell(x, q))[:4] == 'text':
                    break
        juwap = str(''.join(str(worksheet1.cell_value(x, q)).split()))
        return juwap

    if kurs == 2:
        if str(worksheet2.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 9):
                q = q - 1
                if str(worksheet2.cell(x, q))[:4] == 'text':
                    break
        juwap = str(''.join(str(worksheet2.cell_value(x, q)).split()))
        return juwap

    if kurs == 3:
        if str(worksheet3.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 9):
                q = q - 1
                if str(worksheet3.cell(x, q))[:4] == 'text':
                    break
        juwap = str(''.join(str(worksheet3.cell_value(x, q)).split()))
        return juwap

    if kurs == 4:
        if str(worksheet4.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 9):
                q = q - 1
                if str(worksheet4.cell(x, q))[:4] == 'text':
                    break
        juwap = str(''.join(str(worksheet4.cell_value(x, q)).split()))
        return juwap
