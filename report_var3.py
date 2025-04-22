from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak, Image
from reportlab.lib.units import cm
from reportlab.lib import colors

from eq import fml
from page_number import addPageNumber
from paragraph_styles import *
# from report import sp_15, sp_20, sp_25

from gen import tg_g
from var3 import *

doc = SimpleDocTemplate(
    'var3.pdf',
    pagesize=A4,
    rightMargin=1 * cm, leftMargin=3 * cm,
    topMargin=1 * cm, bottomMargin=1.5 * cm, title='3-й вариант схемы')

sp_15 = Spacer(0, 15)
sp_20 = Spacer(0, 20)
sp_25 = Spacer(0, 25)

f = [Paragraph('Вариант 3', style=st_i_10_5),
     Paragraph('К стороне СН подключено 3 генератора, к автотрансформаторам связи подключены 2 генератора',
               style=st_0_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\3 вар. из примера 2.png',
           width=15*cm, height=10*cm, kind='proportional'),
     Paragraph('Рис. 3 - 3 вариант структурной схемы КЭС', style=s_c_t),
     # Paragraph('Выбор автотрансформаторов связи', style=st_0_10),
     Paragraph('Режим 1', style=st_i_0_3),
     Paragraph('Передача максимального перетока избыточной мощности из стороны СН в сеть РУВН:', style=st_0_25),
     fml(f'$P_1 = \\dfrac {{P_{{изб_\u0020max}}}} {{2}} + {{P\'}}_{{г_\u0020ном.}}; \\quad'
         f'P_1 = \\dfrac {{{p1:.1f}}} {{2}} + {{{p_g:.1f}}}; = {p1:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_1 = Q_{{изб_\u0020max}} = N_1 {{Q\'}}_{{Г_\u0020 ном.}} - Q_{{нг_\u0020л_\u0020min}}; \\quad'
         f'Q_1 = {n1_c} \\cdot {q_g_:.1f} - {q_ld_min_sm:.1f} = {q1:.1f}$ МВар'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 1_\u0020расч}} = \\dfrac {{1}} {{2}} \\sqrt {{P_1^2 + Q_1^2}}; \\quad'
         f'S_{{АТ_\u0020 1_\u0020расч}} = \u221a ({p1:.1f}^2 + {q1:.1f}^2) \\div 2 = {s1:.1f}$ МВ\u00B7А'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 1_\u0020ном}} \u2265 S_{{АТ_\u0020 1_\u0020расч}}$'),

     Paragraph('Режим 2', style=st_i_10_2),
     Paragraph('Аварийное отключение одного из автотрансформаторов связи при максимальном избытке мощности '
               'на стороне СН', style=st_0_10),
     fml(f'$P_2 = P_{{изб_\u0020max}} + 2 P\'_{{г_\u0020 ном}} - P_{{ав._\u0020рез.}}; \\quad P_2 = {p1:.1f} + 2\\cdot '
         f'{p_g_}- {p_r} = {p2:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_2 = Q_{{изб_\u0020max}} - P_{{ав._\u0020рез.}} \\tan(\\phi_{{г_\u0020ном}}); \\quad'
         f'Q_2 = {q1:.1f} - {p_r:.1f} \\cdot {tg_g:.2f} = {q2:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 2_\u0020расч}} = \\dfrac {{\\sqrt{{P_2^2 + Q_2^2}}}} {{k_{{ав_\u0020рез}}}}; \\quad'
         f'S_{{АТ_\u0020 2_\u0020расч}} = \u221a({p2:.1f}^2 + {q2:.1f}^2) \\div 2 = {s2:.1f}$ МВ\u00B7А'),
     sp_25,
     # \u00b8 - верхний индекс 2
     fml(f'$S_{{АТ_\u0020 2_\u0020ном}} \u2265 S_{{АТ_\u0020 2_\u0020расч}}$'),

     Paragraph('Режим 3', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН в режиме '
               'зимнего максимума нагрузки', style=st_0_10),
     fml(f'$P_3 = P_{{нг_\u0020з_\u0020max}} - \\left (N_1 - 1 \\right) {{P\'}}_{{г_\u0020ном}} + P_{{с.н.}}; \\quad '
         f'P_3 = {p_ld_max_w:.1f} - {n1_c - 1} \\cdot {p_g_:.1f} + {p_s_n:.1f} = {p3:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_3 = Q_{{нг_\u0020 з_\u0020 max}} - \\left (N_1 - 1 \\right) {{Q\'}}_{{г_\u0020ном}} + Q_{{с.н.}}; \\quad'
         f'Q_3 = {q_ld_max_w:.1f} - {n1_c - 1} \\cdot {q_g_:.1f} + {q_s_n:.1f} = {q3:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 3_\u0020 расч}} = \\dfrac {{\\sqrt{{P_3^2 + Q_3^2}}}} {{2}}; \\quad'
         f'S_{{АТ_\u0020 3_\u0020 расч}} = \u221a({p3:.1f}^2 + {q3:.1f}^2) \\div {2} = {s3:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 3_\u0020ном}} \u2265 S_{{АТ_\u0020 3_\u0020расч}}$'),

     Paragraph('Режим 4', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН в режиме летнего минимума '
               'нагрузки во время планового ремонта другого блока на стороне СН', style=st_0_10),
     fml(f'$P_4 = P_{{нг_\u0020л_\u0020max}} - \\left (N_1 - 2 \\right) {{P\'}}_{{г_\u0020ном}} + 2 P_{{с.н.}}; \\quad '
         f'P_4 = {p_ld_max_s:.1f} - ({n1_c} - 2) \\cdot {p_g_:.1f} + 2 \\cdot {p_s_n:.1f} = {p4:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_4 = Q_{{нг_\u0020 л_\u0020 max}} - \\left (N_1 - 2 \\right) '
         f'{{Q\'}}_{{г_\u0020 ном}} + 2Q_{{с.н.}}; \\quad'
         f'Q_4 = {q_ld_max_w:.1f} - ({n1_c} - 2) \\cdot {q_g_:.1f} + {q_s_n:.1f} = {q4:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 4_\u0020 расч}} = \\dfrac {{\\sqrt{{P_4^2 + Q_4^2}}}} {{2}}; \\quad'
         f'S_{{АТ_\u0020 4_\u0020 расч}} = \u221a({p4:.1f}^2 + {q4:.1f}^2) \\div {2} = {s4:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 4_\u0020ном}} \u2265 S_{{АТ_\u0020 4_\u0020расч}}$'),

     Paragraph('Режим 5', style=st_i_5_2),
     Paragraph('Возможный трансформаторный режим передачи мощности из стороны НН в сторону СН', style=st_0_20),
     fml(f'$S_{{АТ_\u0020 5_\u0020 расч}} = \\dfrac {{{{S\'}}_{{г_\u0020 ном}}}} {{k_{{выг}}}}; \\quad'
         f'S_{{АТ_\u0020 5_\u0020 расч}} = {s_g_:.1f} \\div {k_p:.2f} = {s5:.1f}$ МВ\u00B7А'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 5_\u0020ном}} \u2265 S_{{АТ_\u0020 5_\u0020расч}}$'),
     # Paragraph('Номинальная мощность обмотки НН', style=st_0_20),
     # fml(f'$S_{{АТ_\u0020 5_\u0020 расч}} = \\dfrac {{{{S\'}}_{{г_\u0020 ном}}}} {{k_{{выг}}}}; \\quad'),

     # Paragraph('Критерием выбора окончательного варианта структурной схемы является КЭС выбираем вариант ',
     #           st_10_3),
     Paragraph('Автотрансформаторы связи выбирается по режиму с наибольшим перетоком мощности, при этом '
               'номинальная мощность обмотки НН должна быть больше мощности генератора за вычетом мощности с.н.',
               st_10_3),
     ]

doc.build(f, onLaterPages=addPageNumber)