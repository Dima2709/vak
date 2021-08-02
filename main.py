import random as rd
slovar = {}
st = ['']
s = ''
for i in range(1000):
    while str(s) in st:
             s = rd.randint(10000,99999)
    st.append(str(s))
st = st[1:]
for i in st:
    slovar[i] = {}
for i in st:
    slovar[i]['age'] = rd.randint(18, 70)
    slovar[i]['sex'] = rd.choice(['ж', 'м'])
    slovar[i]['contry'] = rd.choice(['rf','kz','rb','uk'])
    slovar[i]['mounth'] = rd.choice(['april', 'june', 'may', 'mart'])
    slovar[i]['zp'] = rd.randint(15000,120000)
    slovar[i]['point'] = rd.randint(0,10)
class vakcina:
    def __init__(self):
        print('Hello')
    def sred(self, dct):
        sm = []
        for i in list(dct.keys()):
            sm.append(dct[i]['age'])
        print('Средний возраст прошедших вакцинацию', sum(sm)/len(sm))
    def women(self, dct):
        count = 0
        for i in (dct.keys()):
            if dct[i]['sex'] == 'ж':
                count +=1
        print(count, 'Женщин прошли вакцинацию')
    def men(self,dct):
        count = 0
        for i in (dct.keys()):
            if dct[i]['sex'] == 'м':
                count += 1
        print(count, 'Мужчин прошли вакцинацию')
    def sred_mes(self, dct):
        sm = {}
        for i in list(dct.keys()):
            sm[dct[i]['mounth']] = []
        for i in list(dct.keys()):
            sm[dct[i]['mounth']].append(dct[i]['age'])
        for i in list(sm.keys()):
            print('Средний возраст в', i, sum(sm[i])/len(sm[i]))
    def sred_voz(self, dct):
        sm = {}
        for i in list(dct.keys()):
            sm[dct[i]['sex']] = []
        for i in list(dct.keys()):
            sm[dct[i]['sex']].append (dct[i]['age'])
        for i in list(sm.keys()):
            print('Средний возраст у', i, sum(sm[i])/len(sm[i]))
    def voz_loyl(self, dct):
        a1 = []
        a2 = []
        a3 = []
        a4 = []
        poi = []
        ag = []
        ab = []
        for i in list(dct.keys()):
            poi.append (dct[i]['point'])
        for i in list(dct.keys()):
            ag.append(dct[i]['age'])
        for i in range(len(poi)):
            if poi[i] >= 5:
                ab.append(ag[i])
        for i in ab:
            if i >= 18 and i < 30:
                a1.append(i)
            elif i >= 30 and i < 45:
                a2.append(i)
            elif i >= 45 and i < 60:
                a3.append(i)
            elif i >= 60:
                a4.append(i)
        if len(a1) > len(a2) and len(a1) > len(a4) and len(a1) > len(a3):
            print('Самые лояльные люди в возрасте от 18 до 30 лет')
        elif len(a2) > len(a1) and len(a2) > len(a3) and len(a2) > len(a4):
            print('Самые лояльные люди в возрасте от 30 до 45 лет')
        elif len(a3) > len(a1) and len(a3) > len(a2) and len(a3) > len(a4):
            print('Самые лояльные люди в возрасте от 45 до 60 лет')
        elif len(a4) > len(a1) and len(a4) > len(a2) and len(a4) > len(a3):
            print('Самые лояльные люди в возрасте от 60 лет')
        else:
            print('Данные разнятся')
    def mes_vak(self, dct):
        ms = {}
        for i in list(dct.keys()):
            ms[dct[i]['mounth']] = []
        for i in list(dct.keys()):
            ms[dct[i]['mounth']].append(dct[i]['age'])
        for i in list(ms.keys()):
            print ('В', i , len (ms[i]))
    def ino(self, dct):
        ms = {}
        for i in list(dct.keys()):
            ms[dct[i]['mounth']] = []
        for i in list(dct.keys()):
            ms[dct[i]['mounth']].append(dct[i]['contry'])
        for i in list(ms.keys()):
            count = 0
            for j in ms[i]:
                if j != 'rf':
                    count += 1
            a = count/len(ms[i])
            print(i, int(a*100), '% иностранных граждан')
    def rus(self, dct):
        ms = {}
        for i in list(dct.keys()):
            ms[dct[i]['mounth']] = []
        for i in list(dct.keys()):
            ms[dct[i]['mounth']].append(dct[i]['contry'])
        for i in list(ms.keys()):
            count = 0
            for j in ms[i]:
                if j == 'rf':
                    count += 1
            a = count/len(ms[i])
            print(i, int(a*100), '% российских граждан')
    def zp_loyl(self, dct):
        sm = {}
        for i in list(dct.keys()):
            sm[dct[i]['point']] = []
        for i in list(dct.keys()):
            sm[dct[i]['point']].append(dct[i]['zp'])
        lst = [i for i in list(sm.keys())]
        lst.sort()
        for i in lst:
            print(i, int(sum(sm[i])/len(sm[i])))


stk = vakcina()
stk.sred(slovar)
stk.women(slovar)
stk.men(slovar)
stk.sred_mes(slovar)
stk.sred_voz(slovar)
stk.voz_loyl(slovar)
stk.mes_vak(slovar)
stk.ino(slovar)
stk.rus(slovar)
stk.zp_loyl(slovar)