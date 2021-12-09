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

def sabaq_joqpa(x, q, kurs):
    if kurs == 1:
        bos_sabaq = 1
        if str(worksheet1.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 43):
                q = q - 1
                if str(worksheet1.cell(x, q))[:6] == 'number' or (str(worksheet1.cell_value(x, q)) == 'I' or str(worksheet1.cell_value(x, q)) == 'II' or str(worksheet1.cell_value(x, q)) == 'III' or str(worksheet1.cell_value(x, q)) == 'IV' or (''.join(str(worksheet1.cell_value(x, q)).split())) == 'с/з' or (''.join(str(worksheet1.cell_value(x, q)).split())).isdigit()):
                    bos_sabaq = 0
                    break
                elif str(worksheet1.cell(x, q))[:4] == 'text':
                    bos_sabaq = 1
                    break
                if q == 2:
                    break
        return bos_sabaq

    if kurs == 2:
        bos_sabaq = 1
        if str(worksheet2.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 37):
                q = q - 1
                if str(worksheet2.cell(x, q))[:6] == 'number' or (str(worksheet2.cell_value(x, q)) == 'I' or str(worksheet2.cell_value(x, q)) == 'II' or str(worksheet2.cell_value(x, q)) == 'III' or str(worksheet2.cell_value(x, q)) == 'IV' or (''.join(str(worksheet2.cell_value(x, q)).split())) == 'с/з' or (''.join(str(worksheet2.cell_value(x, q)).split())).isdigit()):
                    bos_sabaq = 0
                    break
                elif str(worksheet2.cell(x, q))[:4] == 'text':
                    bos_sabaq = 1
                    break
                if q == 2:
                    break
        return bos_sabaq

    if kurs == 3:
        bos_sabaq = 1
        if str(worksheet3.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 37):
                q = q - 1
                if str(worksheet3.cell(x, q))[:6] == 'number' or (str(worksheet3.cell_value(x, q)) == 'I' or str(worksheet3.cell_value(x, q)) == 'II' or str(worksheet3.cell_value(x, q)) == 'III' or str(worksheet3.cell_value(x, q)) == 'IV' or (''.join(str(worksheet3.cell_value(x, q)).split())) == 'с/з' or (''.join(str(worksheet3.cell_value(x, q)).split())).isdigit()):
                    bos_sabaq = 0
                    break
                elif str(worksheet3.cell(x, q))[:4] == 'text':
                    bos_sabaq = 1
                    break
                if q == 2:
                    break
        return bos_sabaq

    if kurs == 4:
        bos_sabaq = 1
        if str(worksheet4.cell(x, q)) == 'empty:\'\'':
            for i in range(1, 37):
                q = q - 1
                if str(worksheet4.cell(x, q))[:6] == 'number' or (str(worksheet4.cell_value(x, q)) == 'I' or str(worksheet4.cell_value(x, q)) == 'II' or str(worksheet4.cell_value(x, q)) == 'III' or str(worksheet4.cell_value(x, q)) == 'IV' or (''.join(str(worksheet4.cell_value(x, q)).split())) == 'с/з' or (''.join(str(worksheet4.cell_value(x, q)).split())).isdigit()):
                    bos_sabaq = 0
                    break
                elif str(worksheet4.cell(x, q))[:4] == 'text':
                    bos_sabaq = 1
                    break
                if q == 2:
                    break
        return bos_sabaq