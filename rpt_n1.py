from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors
# from reportlab.lib.styles import getSampleStyleSheet

from gen import *
from load import *
from paragraph_styles import *
# from page_number import *
from title_list import *
from eq import *
from in_dat import *
# import var1 as v1
# import var2 as v2
# import var3 as v3
# import line as ln

def p_n(canvas, doc):
    # номера страниц
    page_num = canvas.getPageNumber()
    text = str(page_num - 1)
    # canvas.drawRightString(20*cm, 2*cm, text)
    # canvas.textsize = 12
    # canvas.fonts = 'Times-Roman'
    canvas.drawString(12*cm, 1*cm, text)

# styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    'rpt1.pdf',
    pagesize=A4,
    rightMargin=1*cm, leftMargin=3*cm,
    topMargin=1*cm, bottomMargin=1.5*cm, title='Проектирование электрической части КЭС 5600 МВт')

sp_10 = Spacer(0, 10)
sp_15 = Spacer(0, 15)
sp_20 = Spacer(0, 20)
sp_1 = Spacer(0, 1*cm)
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
     Paragraph('Задание', style=st_b),
     Paragraph('Разработать структурную схему КЭС. Рассмотреть возможные варианты структурной схемы электростанции'
               ' и для каждого из них выбрать номинальные параметры основного силового оборудования', style=s_m),
     Paragraph('Исходные данные', style=st_b),
     Paragraph('Установленная мощность, МВт', style=st_0_10),
     fml(f'$S = {p_st}$'),
     Paragraph('Генераторы, число и ном. мощность (МВт), расход на СН', style=s_f_10),
     fml(f'${n_g} \\times {p_g}, {k_s_n*100:.0f}\\%$'),
     # Paragraph(f'Коэффициенты мощности (cos φ) генераторов, механизмов собственных нужд и '
     #           f'источников аварийного резерва энергосистемы одинаковые и равны 0.85'),
     Paragraph('Нагрузки потребителей', style=st_i_5_5),
     Paragraph('Номинальное напряжение потребителей, кВ', style=s_f_10),
     fml(f'$U = {u_ld}$'),
     # Paragraph('Число потребителей и максимальная мощность в зимний период, МВт', style=st_5_20),
     Paragraph('Число потребителей и максимальная мощность, МВт', style=s_f_10),
     fml(f'${n_ld} \\times {p_ld}$'),
     Paragraph('Коэффициент мощности потребителей, о. е.', style=s_f_10),
     fml(f'$cos\\phi = {cos_ld}$'),
     Paragraph('Номинальное напряжение системы (стороны ВН), кВ', style=s_f_10),
     fml(f'$U = {u_s}$'),
     Paragraph('Длина линий связи, км', style=s_f_10),
     fml(f'$L = {l_ln}$'),
     Paragraph('Мощность аварийного резерва, МВт', style=s_f_10),
     fml(f'$S_{{ав.рез.}} = {s_r}$'),
     Paragraph('Выбор генератора', style=st_b_10_2),
     # Paragraph('Выбираем генератор Т3В-800-2У3 со следующими электрическими параметрами:', style=s_m),
     Paragraph('Выбираем генератор ТВВ-800-2ЕКУ3 со следующими параметрами:', style=s_m),
     Table(data = [[fml(f'$P_Г$, МВт'), fml(f'$U_Г$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
     fml(f'$Q_Г$, МВА'), fml(f'$I_Г$, МВА')],
     [fml(f'${p_g}$'), fml(f'${u_g}$'), fml(f'${cos_g}$'), fml(f'${s_g}$'),
     fml(f'${q_g:.1f}$'), fml(f'${i_g}$')]], colWidths=70, rowHeights=20, spaceBefore=5,
     spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1,colors.black)]),
     # , ('ALIGN', (0, 0), (-1, -1), "CENTER") выравнивание элементов в таблице по ширине
     ]

doc.build(f, onLaterPages=p_n)
