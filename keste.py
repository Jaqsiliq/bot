
from bos_sabaq_ati import bos_sabaq_ati
from pan_mugalimi import pan_mugalimi
from bos_nomer_orni import bos_nomer_orni
from sabaq_joqpa import sabaq_joqpa

def keste(topar, kurs):

    ustin = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]
    hapte_sanlari_1 = [8, 16, 24, 32, 40]
    hapte_sanlari_2 = [8, 16, 24, 32, 40]
    hapte_sanlari_3 = [7, 15, 23, 31, 39]
    hapte_sanlari_4 = [7, 15, 23, 31, 39]
    hapte_kunleri = ["<b>1️⃣-Dushanba:</b>\n", "<b>2️⃣-Seshanba:</b>\n", "<b>3️⃣-Chorshanba:</b>\n", "<b>4️⃣-Payshanba:</b>\n", "<b>5️⃣-Juma:</b>\n"]
    q = ustin[0]
    barligi = ""
    k = 0
# 1 - kurs
    if topar == '1 KI (qq)':
        q = ustin[0]
        barligi = '<b>1 KI (QQ) KESTESI: </b>\n'

    if topar == '1 AT (qq)':
        q = ustin[1]
        barligi = '<b>1 AT (QQ) KESTESI: </b>\n'

    if topar == '1 DI (qq)':
        q = ustin[2]
        barligi = '<b>1 DI (QQ) KESTESI: </b>\n'

    if topar == '1 KT (qq)':
        q = ustin[3]
        barligi = '<b>1 KT (QQ) KESTESI: </b>\n'

    if topar == '1 Tel (qq)':
        q = ustin[4]
        barligi = '<b>1 Tel (QQ) KESTESI: </b>\n'

    if topar == '1 AX (qq)':
        q = ustin[5]
        barligi = '<b>1 AX (QQ) KESTESI: </b>\n'

    if topar == '1 RI (qq)':
        q = ustin[6]
        barligi = '<b>1 RI (QQ) KESTESI: </b>\n'

    if topar == '1 KI (o\'zb)':
        q = ustin[7]
        barligi = '<b>1 KI (O\'ZB) KESTESI: </b>\n'

    if topar == '1 AT (o\'zb)':
        q = ustin[8]
        barligi = '<b>1 AT (O\'ZB) KESTESI: </b>\n'

    if topar == '1 DI (o\'zb)':
        q = ustin[9]
        barligi = '<b>1 DI (O\'ZB) KESTESI: </b>\n'

    if topar == '1 KT (o\'zb)':
        q = ustin[10]
        barligi = '<b>1 KT (O\'ZB) KESTESI: </b>\n'

    if topar == '1 Tel (o\'zb)':
        q = ustin[11]
        barligi = '<b>1 Tel (O\'ZB) KESTESI: </b>\n'

    if topar == '1 AX (o\'zb)':
        q = ustin[12]
        barligi = '<b>1 AX (O\'ZB)  KESTESI: </b>\n'

    if topar == '1 RI (o\'zb)':
        q = ustin[13]
        barligi = '<b>1 RI (O\'ZB) KESTESI: </b>\n'

    if topar == '1 KI (rus)':
        q = ustin[14]
        barligi = '<b>1 KI (RUS) KESTESI: </b>\n'

    if topar == '1 AT (rus)':
        q = ustin[15]
        barligi = '<b>1 AT (RUS) KESTESI: </b>\n'

    if topar == '1 DI (rus)':
        q = ustin[16]
        barligi = '<b>1 DI (RUS) KESTESI: </b>\n'

    if topar == '1 KT (rus)':
        q = ustin[17]
        barligi = '<b>1 KT (RUS) KESTESI: </b>\n'

    if topar == '1 Tel (rus)':
        q = ustin[18]
        barligi = '<b>1 Tel (RUS) KESTESI: </b>\n'

    if topar == '1 AX (rus)':
        q = ustin[19]
        barligi = '<b>1 AX (RUS) KESTESI: </b>\n'

    if topar == '1 RI (rus)':
        q = ustin[20]
        barligi = '<b>1 RI (RUS) KESTESI: </b>\n'

# 2 - kurs

    if topar == '2 KI (qq)':
        q = ustin[0]
        barligi = '<b>2 KI (QQ) KESTESI: </b>\n'

    if topar == '2 AT (qq)':
        q = ustin[1]
        barligi = '<b>2 AT (QQ) KESTESI: </b>\n'

    if topar == '2 DI (qq)':
        q = ustin[2]
        barligi = '<b>2 DI (QQ) KESTESI: </b>\n'

    if topar == '2 KT (qq)':
        q = ustin[3]
        barligi = '<b>2 KT (QQ) KESTESI: </b>\n'

    if topar == '2 Tel (qq)':
        q = ustin[4]
        barligi = '<b>2 Tel (QQ) KESTESI: </b>\n'

    if topar == '2 AX (qq)':
        q = ustin[5]
        barligi = '<b>2 AX (QQ) KESTESI: </b>\n'

    if topar == '2 KI (o\'zb)':
        q = ustin[6]
        barligi = '<b>2 KI (O\'ZB) KESTESI: </b>\n'

    if topar == '2 AT (o\'zb)':
        q = ustin[7]
        barligi = '<b>2 AT (O\'ZB) KESTESI: </b>\n'

    if topar == '2 DI (o\'zb)':
        q = ustin[8]
        barligi = '<b>2 DI (O\'ZB) KESTESI: </b>\n'

    if topar == '2 KT (o\'zb)':
        q = ustin[9]
        barligi = '<b>2 KT (O\'ZB) KESTESI: </b>\n'

    if topar == '2 Tel (o\'zb)':
        q = ustin[10]
        barligi = '<b>2 Tel (O\'ZB) KESTESI: </b>\n'

    if topar == '2 AX (o\'zb)':
        q = ustin[11]
        barligi = '<b>2 AX (O\'ZB)  KESTESI: </b>\n'

    if topar == '2 KI (rus)':
        q = ustin[12]
        barligi = '<b>2 KI (RUS) KESTESI: </b>\n'

    if topar == '2 AT (rus)':
        q = ustin[13]
        barligi = '<b>2 AT (RUS) KESTESI: </b>\n'

    if topar == '2 DI (rus)':
        q = ustin[14]
        barligi = '<b>2 DI (RUS) KESTESI: </b>\n'

    if topar == '2 KT (rus)':
        q = ustin[15]
        barligi = '<b>2 KT (RUS) KESTESI: </b>\n'

    if topar == '2 Tel (rus)':
        q = ustin[16]
        barligi = '<b>2 Tel (RUS) KESTESI: </b>\n'

    if topar == '2 AX (rus)':
        q = ustin[17]
        barligi = '<b>2 AX (RUS) KESTESI: </b>\n'

# 3 - kurs

    if topar == '3 KI (qq)':
        q = ustin[0]
        barligi = '<b>3 KI (QQ) KESTESI: </b>\n'

    if topar == '3 AT (qq)':
        q = ustin[1]
        barligi = '<b>3 AT (QQ) KESTESI: </b>\n'

    if topar == '3 DI (qq)':
        q = ustin[2]
        barligi = '<b>3 DI (QQ) KESTESI: </b>\n'

    if topar == '3 KT (qq)':
        q = ustin[3]
        barligi = '<b>3 KT (QQ) KESTESI: </b>\n'

    if topar == '3 Tel (qq)':
        q = ustin[4]
        barligi = '<b>3 Tel (QQ) KESTESI: </b>\n'

    if topar == '3 AX (qq)':
        q = ustin[5]
        barligi = '<b>3 AX (QQ) KESTESI: </b>\n'

    if topar == '3 KI (o\'zb)':
        q = ustin[6]
        barligi = '<b>3 KI (O\'ZB) KESTESI: </b>\n'

    if topar == '3 AT (o\'zb)':
        q = ustin[7]
        barligi = '<b>3 AT (O\'ZB) KESTESI: </b>\n'

    if topar == '3 DI (o\'zb)':
        q = ustin[8]
        barligi = '<b>3 DI (O\'ZB) KESTESI: </b>\n'

    if topar == '3 KT (o\'zb)':
        q = ustin[9]
        barligi = '<b>3 KT (O\'ZB) KESTESI: </b>\n'

    if topar == '3 Tel (o\'zb)':
        q = ustin[10]
        barligi = '<b>3 Tel (O\'ZB) KESTESI: </b>\n'

    if topar == '3 AX (o\'zb)':
        q = ustin[11]
        barligi = '<b>3 AX (O\'ZB)  KESTESI: </b>\n'

    if topar == '3 KI (rus)':
        q = ustin[12]
        barligi = '<b>3 KI (RUS) KESTESI: </b>\n'

    if topar == '3 AT (rus)':
        q = ustin[13]
        barligi = '<b>3 AT (RUS) KESTESI: </b>\n'

    if topar == '3 DI (rus)':
        q = ustin[14]
        barligi = '<b>3 DI (RUS) KESTESI: </b>\n'

    if topar == '3 KT (rus)':
        q = ustin[15]
        barligi = '<b>3 KT (RUS) KESTESI: </b>\n'

    if topar == '3 Tel (rus)':
        q = ustin[16]
        barligi = '<b>3 Tel (RUS) KESTESI: </b>\n'

    if topar == '3 AX (rus)':
        q = ustin[17]
        barligi = '<b>3 AX (RUS) KESTESI: </b>\n'

# 4 - kurs

    if topar == '4 KI (qq)':
        q = ustin[0]
        barligi = '<b>4 KI (QQ) KESTESI: </b>\n'

    if topar == '4 AT (qq)':
        q = ustin[1]
        barligi = '<b>4 AT (QQ) KESTESI: </b>\n'

    if topar == '4 DI (qq)':
        q = ustin[2]
        barligi = '<b>4 DI (QQ) KESTESI: </b>\n'

    if topar == '4 KT (qq)':
        q = ustin[3]
        barligi = '<b>4 KT (QQ) KESTESI: </b>\n'

    if topar == '4 Tel (qq)':
        q = ustin[4]
        barligi = '<b>4 Tel (QQ) KESTESI: </b>\n'

    if topar == '4 AX (qq)':
        q = ustin[5]
        barligi = '<b>4 AX (QQ) KESTESI: </b>\n'

    if topar == '4 KI (o\'zb)':
        q = ustin[6]
        barligi = '<b>4 KI (O\'ZB) KESTESI: </b>\n'

    if topar == '4 AT (o\'zb)':
        q = ustin[7]
        barligi = '<b>4 AT (O\'ZB) KESTESI: </b>\n'

    if topar == '4 DI (o\'zb)':
        q = ustin[8]
        barligi = '<b>4 DI (O\'ZB) KESTESI: </b>\n'

    if topar == '4 KT (o\'zb)':
        q = ustin[9]
        barligi = '<b>4 KT (O\'ZB) KESTESI: </b>\n'

    if topar == '4 Tel (o\'zb)':
        q = ustin[10]
        barligi = '<b>4 Tel (O\'ZB) KESTESI: </b>\n'

    if topar == '4 AX (o\'zb)':
        q = ustin[11]
        barligi = '<b>4 AX (O\'ZB)  KESTESI: </b>\n'

    if topar == '4 KI (rus)':
        q = ustin[12]
        barligi = '<b>4 KI (RUS) KESTESI: </b>\n'

    if topar == '4 AT (rus)':
        q = ustin[13]
        barligi = '<b>4 AT (RUS) KESTESI: </b>\n'

    if topar == '4 DI (rus)':
        q = ustin[14]
        barligi = '<b>4 DI (RUS) KESTESI: </b>\n'

    if topar == '4 KT (rus)':
        q = ustin[15]
        barligi = '<b>4 KT (RUS) KESTESI: </b>\n'

    if topar == '4 Tel (rus)':
        q = ustin[16]
        barligi = '<b>4 Tel (RUS) KESTESI: </b>\n'

    if topar == '4 AX (rus)':
        q = ustin[17]
        barligi = '<b>4 AX (RUS) KESTESI: </b>\n'


    if kurs == 1:
        for x in hapte_sanlari_1:
            s = 1
            barligi += hapte_kunleri[k]
            k += 1
            for j in range(1, 5):

                if sabaq_joqpa(x, q, 1) == 1:
                    barligi += str(s) + ")" + bos_sabaq_ati(x, q, 1) + "\n" + pan_mugalimi(x, q, 1) + bos_nomer_orni(x, q, 1) + "\n"
                x += 2
                s += 1
            barligi += "\n"
        return barligi

    if kurs == 2:

        for x in hapte_sanlari_2:
            s = 1
            barligi += hapte_kunleri[k]
            k += 1
            for j in range(1, 5):

                if sabaq_joqpa(x, q, 2) == 1:
                    barligi += str(s) + ")" + bos_sabaq_ati(x, q, 2) + "\n" + pan_mugalimi(x, q, 2) + bos_nomer_orni(x, q, 2) + "\n"
                x += 2
                s += 1
            barligi += "\n"
        return barligi

    if kurs == 3:

        for x in hapte_sanlari_3:
            s = 1
            barligi += hapte_kunleri[k]
            k += 1
            for j in range(1, 5):

                if sabaq_joqpa(x, q, 3) == 1:
                    barligi += str(s) + ")" + bos_sabaq_ati(x, q, 3) + "\n" + pan_mugalimi(x, q, 3) + bos_nomer_orni(x, q, 3) + "\n"
                x += 2
                s += 1
            barligi += "\n"
        return barligi

    if kurs == 4:

        for x in hapte_sanlari_4:
            s = 1
            barligi += hapte_kunleri[k]
            k += 1
            for j in range(1, 5):

                if sabaq_joqpa(x, q, 4) == 1:
                    barligi += str(s) + ")" + bos_sabaq_ati(x, q, 4) + "\n" + pan_mugalimi(x, q, 4) + bos_nomer_orni(x, q, 4) + "\n"
                x += 2
                s += 1
            barligi += "\n"
        return barligi


#print(keste('1 RI (rus)'))
