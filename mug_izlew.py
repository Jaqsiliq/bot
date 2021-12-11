
from bos_sabaq_ati import bos_sabaq_ati
from pan_mugalimi import pan_mugalimi
from bos_nomer_orni import bos_nomer_orni
from sabaq_joqpa import sabaq_joqpa

def mug_izlew(ustaz):
    ustin = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
    hapte_sanlari_1 = [8, 16, 24, 32, 40]
    hapte_kunleri = ["<b>1️⃣-Dushanba:</b>\n", "<b>2️⃣-Seshanba:</b>\n", "<b>3️⃣-Chorshanba:</b>\n", "<b>4️⃣-Payshanba:</b>\n", "<b>5️⃣-Juma:</b>\n"]
    barligi = "<b> TATU NF Ustozlar </b>\n"
    k = 0
    mug = 0
    for x in hapte_sanlari_1:
        s = 1
        barligi += hapte_kunleri[k]
        k += 1
        for j in range(1, 5):
            for q in ustin:

                if sabaq_joqpa(x, q, 1) == 1:

                    a = str(pan_mugalimi(x, q, 1)).lower()

                    if a.find(ustaz) != -1:
                        barligi += str(s) + ") "
                        if q == 3:
                            barligi += '<b>1 KI (QQ) : </b>\n'

                        if q == 5:
                            barligi += '<b>1 AT (QQ) : </b>\n'

                        if q == 7:
                            barligi += '<b>1 DI (QQ) : </b>\n'

                        if q == 9:
                            barligi += '<b>1 KT (QQ) : </b>\n'

                        if q == 11:
                            barligi += '<b>1 Tel (QQ) : </b>\n'

                        if q == 13:
                            barligi += '<b>1 AX (QQ) : </b>\n'

                        if q == 15:
                            barligi += '<b>1 RI (QQ) : </b>\n'

                        if q == 17:
                            barligi += '<b>1 KI (O\'ZB) : </b>\n'

                        if q == 19:
                            barligi += '<b>1 AT (O\'ZB) : </b>\n'

                        if q == 21:
                            barligi += '<b>1 DI (O\'ZB) : </b>\n'

                        if q == 23:
                            barligi += '<b>1 KT (O\'ZB) : </b>\n'

                        if q == 25:
                            barligi += '<b>1 Tel (O\'ZB) : </b>\n'

                        if q == 27:
                            barligi += '<b>1 AX (O\'ZB)  : </b>\n'

                        if q == 29:
                            barligi += '<b>1 RI (O\'ZB) : </b>\n'

                        if q == 31:
                            barligi += '<b>1 KI (RUS) : </b>\n'

                        if q == 33:
                            barligi += '<b>1 AT (RUS) : </b>\n'

                        if q == 35:
                            barligi += '<b>1 DI (RUS) : </b>\n'

                        if q == 37:
                            barligi += '<b>1 KT (RUS) : </b>\n'

                        if q == 39:
                            barligi += '<b>1 Tel (RUS) : </b>\n'

                        if q == 41:
                            barligi += '<b>1 AX (RUS) : </b>\n'

                        if q == 43:
                            barligi += '<b>1 RI (RUS) : </b>\n'

                        barligi += "<b><i>" + bos_sabaq_ati(x, q, 1) + "</i></b>" + "\n" + pan_mugalimi(x, q,1) + bos_nomer_orni(x, q,1) + "\n"
                        mug = mug + 1
                        #print(a)


                #2-kurs
                if q <= 37:
                    if sabaq_joqpa(x, q, 2) == 1:

                        a = str(pan_mugalimi(x, q, 2)).lower()

                        if a.find(ustaz) != -1:
                            barligi += str(s) + ") "
                            if q == 3:
                                barligi += '<b>2 KI (QQ) : </b>\n'

                            if q == 5:
                                barligi += '<b>2 AT (QQ) : </b>\n'

                            if q == 7:
                                barligi += '<b>2 DI (QQ) : </b>\n'

                            if q == 9:
                                barligi += '<b>2 KT (QQ) : </b>\n'

                            if q == 11:
                                barligi += '<b>2 Tel (QQ) : </b>\n'

                            if q == 13:
                                barligi += '<b>2 AX (QQ) : </b>\n'

                            if q == 15:
                                barligi += '<b>2 KI (O\'ZB) : </b>\n'

                            if q == 17:
                                barligi += '<b>2 AT (O\'ZB) : </b>\n'

                            if q == 19:
                                barligi += '<b>2 DI (O\'ZB) : </b>\n'

                            if q == 21:
                                barligi += '<b>2 KT (O\'ZB) : </b>\n'

                            if q == 23:
                                barligi += '<b>2 Tel (O\'ZB) : </b>\n'

                            if q == 25:
                                barligi += '<b>2 AX (O\'ZB)  : </b>\n'

                            if q == 27:
                                barligi += '<b>2 KI (RUS) : </b>\n'

                            if q == 29:
                                barligi += '<b>2 AT (RUS) : </b>\n'

                            if q == 31:
                                barligi += '<b>2 DI (RUS) : </b>\n'

                            if q == 33:
                                barligi += '<b>2 KT (RUS) : </b>\n'

                            if q == 35:
                                barligi += '<b>2 Tel (RUS) : </b>\n'

                            if q == 37:
                                barligi += '<b>2 AX (RUS) : </b>\n'

                            barligi += bos_sabaq_ati(x, q, 2) + "\n" + pan_mugalimi(x, q, 2) + bos_nomer_orni(x, q,2) + "\n"
                            mug = mug + 1
                            # print(a)

                # 3-kurs
                if q <= 37:
                    if sabaq_joqpa(x-1, q, 3) == 1:

                        a = str(pan_mugalimi(x-1, q, 3)).lower()

                        if a.find(ustaz) != -1:
                            barligi += str(s) + ") "
                            if q == 3:
                                barligi += '<b>3 KI (QQ) : </b>\n'

                            if q == 5:
                                barligi += '<b>3 AT (QQ) : </b>\n'

                            if q == 7:
                                barligi += '<b>3 DI (QQ) : </b>\n'

                            if q == 9:
                                barligi += '<b>3 KT (QQ) : </b>\n'

                            if q == 11:
                                barligi += '<b>3 Tel (QQ) : </b>\n'

                            if q == 13:
                                barligi += '<b>3 AX (QQ) : </b>\n'

                            if q == 15:
                                barligi += '<b>3 KI (O\'ZB) : </b>\n'

                            if q == 17:
                                barligi += '<b>3 AT (O\'ZB) : </b>\n'

                            if q == 19:
                                barligi += '<b>3 DI (O\'ZB) : </b>\n'

                            if q == 21:
                                barligi += '<b>3 KT (O\'ZB) : </b>\n'

                            if q == 23:
                                barligi += '<b>3 Tel (O\'ZB) : </b>\n'

                            if q == 25:
                                barligi += '<b>3 AX (O\'ZB)  : </b>\n'

                            if q == 27:
                                barligi += '<b>3 KI (RUS) : </b>\n'

                            if q == 29:
                                barligi += '<b>3 AT (RUS) : </b>\n'

                            if q == 31:
                                barligi += '<b>3 DI (RUS) : </b>\n'

                            if q == 33:
                                barligi += '<b>3 KT (RUS) : </b>\n'

                            if q == 35:
                                barligi += '<b>3 Tel (RUS) : </b>\n'

                            if q == 37:
                                barligi += '<b>3 AX (RUS) : </b>\n'

                            barligi += bos_sabaq_ati(x-1, q, 3) + "\n" + pan_mugalimi(x-1, q,3) + bos_nomer_orni(x-1, q, 3) + "\n"
                            mug = mug + 1
                            # print(a)

                # 4-kurs
                if q <= 37:
                    if sabaq_joqpa(x - 1, q, 4) == 1:

                        a = str(pan_mugalimi(x - 1, q, 4)).lower()

                        if a.find(ustaz) != -1:
                            barligi += str(s) + ") "
                            if q == 3:
                                barligi += '<b>4 KI (QQ) : </b>\n'

                            if q == 5:
                                barligi += '<b>4 AT (QQ) : </b>\n'

                            if q == 7:
                                barligi += '<b>4 DI (QQ) : </b>\n'

                            if q == 9:
                                barligi += '<b>4 KT (QQ) : </b>\n'

                            if q == 11:
                                barligi += '<b>4 Tel (QQ) : </b>\n'

                            if q == 13:
                                barligi += '<b>4 AX (QQ) : </b>\n'

                            if q == 15:
                                barligi += '<b>4 KI (O\'ZB) : </b>\n'

                            if q == 17:
                                barligi += '<b>4 AT (O\'ZB) : </b>\n'

                            if q == 19:
                                barligi += '<b>4 DI (O\'ZB) : </b>\n'

                            if q == 21:
                                barligi += '<b>4 KT (O\'ZB) : </b>\n'

                            if q == 23:
                                barligi += '<b>4 Tel (O\'ZB) : </b>\n'

                            if q == 25:
                                barligi += '<b>4 AX (O\'ZB)  : </b>\n'

                            if q == 27:
                                barligi += '<b>4 KI (RUS) : </b>\n'

                            if q == 29:
                                barligi += '<b>4 AT (RUS) : </b>\n'

                            if q == 31:
                                barligi += '<b>4 DI (RUS) : </b>\n'

                            if q == 33:
                                barligi += '<b>4 KT (RUS) : </b>\n'

                            if q == 35:
                                barligi += '<b>4 Tel (RUS) : </b>\n'

                            if q == 37:
                                barligi += '<b>4 AX (RUS) : </b>\n'

                            barligi += bos_sabaq_ati(x - 1, q, 4) + "\n" + pan_mugalimi(x - 1, q,4) + bos_nomer_orni(x - 1, q, 4) + "\n"
                            mug = mug + 1
                            # print(a)
            x += 2
            s += 1
        barligi += "\n"
    return barligi


#print(mug_izlew("даулетназаров"))

