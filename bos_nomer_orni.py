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

def bos_nomer_orni(x, q, kurs):
    if kurs == 1:
        q2 = q + 1
        juwap = ''
        if str(worksheet1.cell(x, q2)) == 'empty:\'\'':
            for i in range(1, 45 - q2):

                if str(worksheet1.cell(x, q2))[:6] == 'number':
                    break
                elif str(worksheet1.cell(x, q2))[:4] == 'text' and ((''.join(str(worksheet1.cell_value(x, q2)).split())) == 'с/з' or (''.join(str(worksheet1.cell_value(x, q2)).split())).isdigit()):
                    break
                q2 = q2 + 1
        if str(worksheet1.cell(x, q2))[:6] == 'number':
            juwap += " <i>(" + str(int(worksheet1.cell_value(x, q2))) + " aud)</i>"
        elif str(worksheet1.cell(x, q2))[:4] == 'text' and (''.join(str(worksheet1.cell_value(x, q2)).split())) != 'с/з':
            juwap += " <i>(" + str(worksheet1.cell_value(x, q2)) + " aud)</i>"
        elif (''.join(str(worksheet1.cell_value(x, q2)).split())) == 'с/з':
            juwap += " <i>(" + str(worksheet1.cell_value(x, q2)) + ")</i>"
        return juwap

    if kurs == 2:
        q2 = q + 1
        juwap = ''
        if str(worksheet2.cell(x, q2)) == 'empty:\'\'':
            for i in range(1, 39 - q2):

                if str(worksheet2.cell(x, q2))[:6] == 'number':
                    break
                elif str(worksheet2.cell(x, q2))[:4] == 'text' and ((''.join(str(worksheet2.cell_value(x, q2)).split())) == 'с/з' or (''.join(str(worksheet2.cell_value(x, q2)).split())).isdigit()):
                    break
                q2 = q2 + 1
        if str(worksheet2.cell(x, q2))[:6] == 'number':
            juwap += " <i>(" + str(int(worksheet2.cell_value(x, q2))) + " aud)</i>"
        elif str(worksheet2.cell(x, q2))[:4] == 'text' and (''.join(str(worksheet2.cell_value(x, q2)).split())) != 'с/з':
            juwap += " <i>(" + str(worksheet2.cell_value(x, q2)) + " aud)</i>"
        elif (''.join(str(worksheet2.cell_value(x, q2)).split())) == 'с/з':
            juwap += " <i>(" + str(worksheet2.cell_value(x, q2)) + ")</i>"
        return juwap

    if kurs == 3:
        q2 = q + 1
        juwap = ''
        if str(worksheet3.cell(x, q2)) == 'empty:\'\'':
            for i in range(1, 39 - q2):

                if str(worksheet3.cell(x, q2))[:6] == 'number':
                    break
                elif str(worksheet3.cell(x, q2))[:4] == 'text' and ((''.join(str(worksheet3.cell_value(x, q2)).split())) == 'с/з' or (''.join(str(worksheet3.cell_value(x, q2)).split())).isdigit()):
                    break
                q2 = q2 + 1
        if str(worksheet3.cell(x, q2))[:6] == 'number':
            juwap += " <i>(" + str(int(worksheet3.cell_value(x, q2))) + " aud)</i>"
        elif str(worksheet3.cell(x, q2))[:4] == 'text' and (''.join(str(worksheet3.cell_value(x, q2)).split())) != 'с/з':
            juwap += " <i>(" + str(worksheet3.cell_value(x, q2)) + " aud)</i>"
        elif (''.join(str(worksheet3.cell_value(x, q2)).split())) == 'с/з':
            juwap += " <i>(" + str(worksheet3.cell_value(x, q2)) + ")</i>"
        return juwap

    if kurs == 4:
        q2 = q + 1
        juwap = ''
        if str(worksheet4.cell(x, q2)) == 'empty:\'\'':
            for i in range(1, 39 - q2):

                if str(worksheet4.cell(x, q2))[:6] == 'number':
                    break
                elif str(worksheet4.cell(x, q2))[:4] == 'text' and ((''.join(str(worksheet4.cell_value(x, q2)).split())) == 'с/з' or (''.join(str(worksheet4.cell_value(x, q2)).split())).isdigit()):
                    break
                q2 = q2 + 1
        if str(worksheet4.cell(x, q2))[:6] == 'number':
            juwap += " <i>(" + str(int(worksheet4.cell_value(x, q2))) + " aud)</i>"
        elif str(worksheet4.cell(x, q2))[:4] == 'text' and (''.join(str(worksheet4.cell_value(x, q2)).split())) != 'с/з':
            juwap += " <i>(" + str(worksheet4.cell_value(x, q2)) + " aud)</i>"
        elif (''.join(str(worksheet4.cell_value(x, q2)).split())) == 'с/з':
            juwap += " <i>(" + str(worksheet4.cell_value(x, q2)) + ")</i>"
        return juwap
