from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors

import gen
# from reportlab.lib.styles import getSampleStyleSheet

from gen import *
from load import *
from paragraph_styles import *
from page_number import *
from title_list import *
from eq import *
from in_dat import *
import var1 as v1
import var2 as v2
import var3 as v3
import line as ln

# styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    'report.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='Проектирование электрической части КЭС 5600 МВт')

sp_10 = Spacer(0, 10)
sp_15 = Spacer(0, 15)
sp_20 = Spacer(0, 20)
sp_1 = Spacer(0, 1 * cm)
sp_25 = Spacer(0, 25)
sp_30 = Spacer(0, 30)
sp_50 = Spacer(0, 50)
sp_2 = Spacer(0, 2 * cm)
s_80 = Spacer(0, 80)
s_100 = Spacer(0, 100)
s_110 = Spacer(0, 110)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
s_150 = Spacer(0, 150)
cpb = CondPageBreak(10)

f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_130, fac, gr, st, tchr, mk, s_130, sity]),
     Paragraph('Выбор выключателей и разъединителей', style=st_b),
     Paragraph('Выбор выключателя вцепи генератора', style=st_b),
     Paragraph('1. По напряжению установки:', style=s_m),
     fml(f'$U_{{ном._\u0020выкл}} = U_{{ном._\u0020ген}}; \\quad '
         f'U_{{ном._\u0020выкл}} = {gen.u_g}$'),
     Paragraph('2. По току утяжеленного (послеаварийного) режима установки:', style=s_m),
     fml(f'$I_{{ном._\u0020выкл}} \u2265 I_{{утж}}$'),
     sp_20,
     fml(f'$I_{{ном._\u0020выкл}} \u2265 I_{{утж}} = {1.05} I_{{г.\u0020_ном}} = '
         f'{1.05} \\dfrac {{ S_{{г.\u0020_ном}} }} {{ {{\\sqrt{3} U_{{г_\u0020ном.}} }}$; \\quad '
         f'I_{{утж}} = {1.05} \\cdot \\dfrac{{{gen.s_g:.2f}}} {{\\sqrt{3}{gen.u_g:.2f} }} = {gen.i_g_w:.2f}$ кА'),
     Paragraph('Предварительно выбираем генераторный выключатель FKG1. Параметры выключателя:', style=s_m),
     Table(data = [[Paragraph('Тип', s_m), fml(f'$U_ном$, МВт'), fml(f'$U_Г$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
     fml(f'$Q_Г$, МВА'), fml(f'$I_Г$, МВА')],
     [Paragraph('Воздушный', s_m), fml(f'${u_s}$'), fml(f'${cos_g}$'), fml(f'${s_g}$'),
     fml(f'${q_g:.1f}$'), fml(f'${i_g}$')]], colWidths=70, rowHeights=20, spaceBefore=5,
     spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1,colors.black)]),


     ]
