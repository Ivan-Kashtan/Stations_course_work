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
    text = str(page_num)
    # canvas.drawRightString(20*cm, 2*cm, text)
    # canvas.textsize = 12
    # canvas.fonts = 'Times-Roman'
    canvas.drawString(12*cm, 1*cm, text)


# styles = getSampleStyleSheet()
doc = SimpleDocTemplate(
    'rpt2.pdf',
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

f = [Paragraph('Мощности нагрузок потребителей', style=st_b),
     Paragraph('Зимний период', style=st_i_0_3),
     Paragraph('Максимальная активная мощность нагрузки в зимний период', style=st_0_10),
     fml(f'$P_{{нг_\u0020max_\u0020з}} = n_{{нг}}P_{{нг}}K_{{о}};$ где $k_о = {k_s}$ - коэффициент одновременности'),
     sp_15,
     fml(f'$P_{{нг_\u0020max_\u0020з}} = {n_ld} \\cdot {p_ld} \\cdot {k_s} = {p_ld_max_w:.0f}$ МВт'),
     Paragraph('Максимальная реактивная мощность нагрузки в зимний период', style=st_5_10),
     fml(f'$Q_{{нг_\u0020max_\u0020з}} = P_{{нг_max_з}}tg\\phi_{{нг}}; \\quad'
     f'Q_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\cdot {tg_ld:.2f} = {q_ld_max_w:.0f}$ Мвар'),
     Paragraph('Максимальная полная мощность нагрузки в зимний период', style=st_5_20),
     fml(f'$S_{{нг_\u0020max_\u0020з}} = \\dfrac {{S_{{нг_\u0020max_\u0020з}}}} {{cos \\phi_{{нг}}}}; \\quad'
     f'S_{{нг_\u0020max_\u0020з}} = \\dfrac {{{p_ld_max_w:.0f}}} {{{cos_ld}}} = {s_ld_max_w:.0f}$ МВ\u00B7А'),
     Paragraph('Максимальная нагрузка в летний период', style=st_i_10_5),
     Paragraph('Активная мощность нагрузки', style=st_0_10),
     fml(f'$P_{{нг_\u0020max_\u0020л}} = P_{{нг_\u0020max_\u0020з}} K_{{max_\u0020л}};$ '
     f'где $K_{{max_\u0020л}} = {k_max_sm}$ - коэффициент летнего максимума'),
     sp_15,
     fml(f'$P_{{нг_\u0020max_\u0020л}} = {p_ld_max_w:.0f} \\cdot {k_max_sm} = {p_ld_max_s:.0f}$ МВт'),
     Paragraph('Реактивная мощность нагрузки', style=st_5_10),
     fml(f'$Q_{{нг_\u0020max_\u0020л}} = Q_{{нг_\u0020max_\u0020з}} K_{{max_\u0020л}}; \\quad'
     f'Q_{{нг_\u0020max_\u0020л}} = {q_ld_max_w:.0f} \\cdot {k_max_sm} = {q_ld_max_s:.0f}$ Мвар'),
     Paragraph('Полная мощность нагрузки', style=st_5_10),
     fml(f'$S_{{нг_\u0020max_\u0020л}} = S_{{нг_\u0020max_\u0020з}} k_{{max_\u0020л}}; \\quad'
     f'S_{{нг_\u0020max_\u0020л}} = {s_ld_max_w:.0f} \\cdot {k_max_sm} = {s_ld_max_s:.0f}$ МВ\u00B7А'),
     Paragraph('Минимальная нагрузка в летний период', style=st_i_5_5),
     Paragraph('Активная мощность нагрузки', style=st_0_10),
     fml(f'$P_{{нг_\u0020min_\u0020л}} = P_{{нг_\u0020max_\u0020з}}K_{{min_л}};$ '
     f'где $K_{{min_\u0020л}} = {k_min_sm}$ - коэффициент летнего минимума'),
     sp_15,
     fml(f'$P_{{нг_\u0020min_\u0020л}} = {p_ld_max_w:.0f} \\cdot {k_min_sm} = {p_ld_min_sm:.0f}$ МВт'),
     Paragraph('Реактивная мощность нагрузки', style=st_5_10),
     fml(f'$Q_{{нг_\u0020min_\u0020л}} = Q_{{нг_\u0020max_\u0020з}} K_{{min_\u0020л}}; \\quad'
     f'Q_{{нг_min_л}} = {q_ld_max_w:.0f} \\cdot {k_min_sm} = {q_ld_min_sm:.0f}$ Мвар'),
     Paragraph('Полная мощность нагрузки', style=st_5_10),
     fml(f'$S_{{нг_\u0020min_\u0020л}} = S_{{нг_\u0020max_\u0020з}} k_{{min_\u0020л}}; \\quad'
     f'S_{{нг_\u0020min_\u0020л}} = {s_ld_max_w:.0f} \\cdot {k_min_sm} = {s_ld_min_sm:.0f}$ МВ\u00B7А'),

     Paragraph('Мощности собственных нужд', style=st_b_10_2),
     Paragraph('Активная мощность с.н. агрегатов', style=st_0_10),
     fml(f'$P_{{Г\u0020с.н.}} = k_{{с.н.}}P_{{Г\u0020ном}}; \\quad$ где $k_{{с.н.}}={k_s_n}$ - доля расхода на с.н.'),
     sp_15,
     fml(f'$P_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {p_g} = {p_s_n:.1f}$ МВт'),
     Paragraph('Реактивная мощность с.н. агрегатов', style=st_5_10),
     fml(f'$Q_{{Г_\u0020с.н.}} = k_{{с.н.}}P_{{Г_\u0020ном}}; \\quad '
     f'Q_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {p_g} = {q_s_n:.1f}$ Мвар'),
     Paragraph('Полная мощность с.н. агрегата', style=st_5_10),
     fml(f'$S_{{Г_\u0020с.н.}} = k_{{с.н.}}S_{{Г_\u0020ном}}; \\quad '
     f'S_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {s_g} = {s_s_n:.1f}$ МВ\u00B7А'),
     Paragraph('Номинальные мощности агрегатов с вычетом мощности с.н.', style=st_i_5_2),
     Paragraph('Номинальная активная мощность агрегатов с вычетом мощности с.н.', style=st_0_10),
     fml(f'${{P\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_\u0020ном}}; \\quad '
     f'{{P\'}}_{{Г_\u0020с.н.}} = {1 - k_s_n:.2f} \\cdot {p_g} = {p_g_:.1f}$ МВт'),
     Paragraph('Номинальная реактивная мощность агрегатов с вычетом мощности с.н. ', style=st_5_10),
     fml(f'${{Q\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_ном}}; \\quad '
     f'{{Q\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {q_g:.1f} = {q_g_:.1f}$ Мвар'),
     Paragraph('Номинальная полная мощность агрегатов с вычетом мощности с.н. ', style=st_5_10),
     fml(f'${{S\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})S_{{Г_ном}}; \\quad '
     f'{{S\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {s_g} = {s_g_:.1f}$ МВ\u00B7А'),
     Paragraph('Выбор трансформаторов блоков по номинальной мощности осуществляется по условию:', style=st_5_10),
     fml(f'$S_{{ТБ}} \u2265 {{S\'}}_{{Г_\u0020ном}} = {s_g_:.1f}$ МВ\u00B7А'),
     # Paragraph('Выбираем трансформатор типа ТЦ-100000/330-69У1  номинальным напряжением стороны НН 24 кВ для '
     #           'блоков подключенных к РУСН.', style=st_5_5),
     # , и напряжением ВН 750 кВ, если блок подключается к РУВН. c. 157 Неклепаев
     Paragraph('Выбираем трансформаторы типа ТНЦ-100000/330 c номинальным напряжением стороны НН 24 кВ для блоков, '
     'подключаемых к РУСН и 7×ОРЦ-417000/750 для блоков, подключаемых к РУВН.', style=st_5_5),
     # С. 160 Неклепаев
     Paragraph('Необходимая номинальная мощность рабочих трансформаторов собственных нужд:', style=st_0_10),
     fml(f'$S_{{Т_\u0020с.н._\u0020ном}} \u2265 S_{{Г_\u0020ном}} = {s_s_n:.1f}$'),
     Paragraph('Выбираем трансформаторы типа 2×ТРДНС-40000/35 с номинальным напряжением '
     'стороны ВН 24 кВ, а стороны НН - 6,3 кВ', st_5_5),
     ]
     # с. 134 Неклепаев
doc.build(f, onLaterPages=p_n)
