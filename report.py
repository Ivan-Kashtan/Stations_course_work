# Курсовая станции
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak
from reportlab.lib.units import cm
from reportlab.lib import colors
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
sp_50 = Spacer(0, 50)
sp_2 = Spacer(0, 2 * cm)
s_80 = Spacer(0, 80)
s_100 = Spacer(0, 100)
s_110 = Spacer(0, 110)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
s_150 = Spacer(0, 150)
cpb = CondPageBreak(10)

# data = [[fml(f'$P_г$, МВт'), fml(f'$S_г$, МВА'), fml(f'$U_{{н.г}}$, кВ'),
#              Paragraph('Схема соединения обмоток', style=s_m),],
#             [fml(f'${p_g}$'), fml(f'${s_g_c}$'), fml(f'${u_g}$'), Paragraph('Y/Y', style=s_m),]]
# KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_120, fac, gr, st, tchr, mk, s_110, sity])
f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_120, fac, gr, st, tchr, mk, s_110, sity]),
     Paragraph('Задание', style=s_b),
     Paragraph('Разработать структурную схему КЭС на газомазутном топливе. Рассмотреть возможные варианты '
         'структурной схемы электростанции и для каждого из них выбрать номинальные параметры основного '
         'силового оборудования', style=s_m),
     Paragraph('Исходные данные:', style=s_b),
     Paragraph('Установленная мощность, МВт', style=st_0_10),
     fml(f'$S = {p_st}$'),
     Paragraph('Число генераторов', style=s_f_10),
# fml(f'$n_г = {n_g}$'),
     Paragraph('Генераторы, число и ном. мощность (МВт), расход на СН', style=s_f_10),
     fml(f'${n_g} \\times {p_g}, {k_s_n*100:.0f}\\%$'),
     Paragraph(f'Коэффициенты мощности (cos φ) генераторов, механизмов собственных нужд и '
               f'источников аварийного резерва энергосистемы одинаковые и равны 0.85'),
     Paragraph('Нагрузки потребителей', style=st_i_5_5),
     Paragraph('Номинальное напряжение потребителей, кВ', style=s_f_10),
     fml(f'$U = {u_ld}$'),
     Paragraph('Число потребителей и максимальная мощность в зимний период, МВт', style=st_5_20),
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
     Paragraph('Выбираем генератор Т3В-800-2У3 со следующими электрическими параметрами:', style=s_m),
     Paragraph('Выбираем генератор ТВВ-800-2ЕКУ3 со следующими параметрами:', style=s_b),
     Table(data = [[fml(f'$P_Г$, МВт'), fml(f'$U_Г$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
     fml(f'$Q_Г$, МВА'), fml(f'$I_Г$, МВА')],
     [fml(f'${p_g}$'), fml(f'${u_g}$'), fml(f'${cos_g}$'), fml(f'${s_g}$'),
     fml(f'${q_g:.1f}$'), fml(f'${i_g}$')]], colWidths=70, rowHeights=20, spaceBefore=5,
     spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1,colors.black)]),
     # , ('ALIGN', (0, 0), (-1, -1), "CENTER") выравнивание элементов в таблице по ширине
     Paragraph('Мощности нагрузок потребителей', style=s_b),
     Paragraph('Зимний период', style=st_i_0_3),
     Paragraph('Максимальная активная мощность нагрузки в зимний период', style=st_0_10),
     fml(f'$P_{{нг_\u0020max_\u0020з}} = n_{{нг}}P_{{нг}}K_{{о}};$ где $k_о = {k_s}$ - коэффициент одновременности'),
     sp_15,
     fml(f'$P_{{нг_\u0020max_\u0020з}} = {n_ld} \\cdot {p_ld} \\cdot {k_s} = {p_ld_max_w:.0f}$ МВт'),
     Paragraph('Максимальная реактивная мощность нагрузки в зимний период', style=st_5_10),
     fml(f'$Q_{{нг_\u0020max_\u0020з}} = P_{{нг_max_з}}tg\\phi_{{нг}}; \\quad'
     f'Q_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\cdot {tg_ld:.2f} = {q_ld_max_w:.0f}$ Мвар'),
     Paragraph('Максимальная полная мощность нагрузки в зимний период', style=st_5_20),
     fml(f'$S_{{нг_\u0020max_\u0020з}} = \\dfrac {{S_{{нг_max_з}}}} {{cos \\phi_{{нг}}}}; \\quad'
     f'S_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\div {cos_ld} = {s_ld_max_w:.0f}$ МВ\u00B7А'),
     Paragraph('Максимальная нагрузка в летний период', style=st_i_10_5),
     Paragraph('Активная мощность нагрузки', style=st_0_10),
     fml(f'$P_{{нг_\u0020max_\u0020л}} = P_{{нг_max_з}}K_{{max_л}};$ '
     f'где $K_{{max_\u0020л}} = {k_max_sm}$ - коэффициент летнего максимума'),
     sp_15,
     fml(f'$P_{{нг_\u0020max_\u0020л}} = {p_ld_max_w:.0f} \\cdot {k_max_sm} = {p_ld_max_s:.0f}$ МВт'),
     Paragraph('Реактивная мощность нагрузки', style=st_5_10),
     fml(f'$Q_{{нг_\u0020max_\u0020л}} = Q_{{нг_\u0020max_\u0020з}} K_{{max_\u0020л}}; \\quad'
     f'Q_{{нг_\u0020max_\u0020л}} = {q_ld_max_w:.0f} \\cdot {k_max_sm} = {q_ld_max_s:.0f}$ Мвар'),
     Paragraph('Полная мощность нагрузки', style=st_5_10),
     fml(f'$S_{{нг_\u0020max_\u0020л}} = S_{{нг_max_з}} k_{{max_л}}; \\quad'
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
     Paragraph('Мощности собственных нужд', style=s_b),
     Paragraph('Активная мощность с.н. агрегатов', style=st_0_10),
     fml(f'$P_{{Г\u0020с.н.}} = k_{{с.н.}}P_{{Г\u0020ном}}; \\quad$ где $k_{{с.н.}}={k_s_n}$ - доля расхода на с.н.'),
     sp_15,
     fml(f'$P_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {p_g} = {p_s_n:.1f}$ МВт'),
     Paragraph('Реактивная мощность с.н. агрегатов', style=st_0_10),
     fml(f'$Q_{{Г_\u0020с.н.}} = k_{{с.н.}}P_{{Г_\u0020ном}}; \\quad '
     f'Q_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {p_g} = {q_s_n:.1f}$ Мвар'),
     Paragraph('Полная мощность с.н. агрегата', style=st_0_10),
     fml(f'$S_{{Г_\u0020с.н.}} = k_{{с.н.}}S_{{Г\u0020ном}}; \\quad '
     f'S_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {s_g} = {s_s_n:.1f}$ МВ\u00B7А'),
     Paragraph('Номинальные мощности агрегатов с вычетом мощности с.н.', style=st_i_5_2),
     Paragraph('Номинальная активная мощность агрегатов с вычетом мощности с.н.', style=st_0_10),
     fml(f'${{P\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_ном}}; \\quad '
     f'{{P\'}}_{{Г_\u0020с.н.}} = {1 - k_s_n:.2f} \\cdot {p_g} = {p_g_:.1f}$ МВт'),
     Paragraph('Номинальная реактивная мощность агрегатов с вычетом мощности с.н. ', style=st_0_10),
     fml(f'${{Q\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_ном}}; \\quad '
     f'{{Q\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {q_g:.1f} = {q_g_:.1f}$ Мвар'),
     Paragraph('Номинальная полная мощность агрегатов с вычетом мощности с.н. ', style=st_0_10),
     fml(f'${{S\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})S_{{Г_ном}}; \\quad '
     f'{{S\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {s_g} = {s_g_:.1f}$ МВ\u00B7А'),
     Paragraph('Выбор трансформаторов блоков по номинальной мощности осуществляется по условию:', style=st_5_10),
     fml(f'$S_{{ТБ}} \u2265 {{S\'}}_{{Г_\u0020ном}} = {s_g_:.1f}$ МВ\u00B7А'),
     # Paragraph('Выбираем трансформатор типа ТЦ-100000/330-69У1  номинальным напряжением стороны НН 24 кВ для '
     #           'блоков подключенных к РУСН.', style=st_5_5),
     # , и напряжением ВН 750 кВ, если блок подключается к РУВН. c. 157 Неклепаев
     Paragraph('Выбираем трансформаторы типа ТЦН-100000/330 c номинальным напряжением стороны НН 24 кВ для блоков, '
     'подключаемых к РУСН и 7×ОРЦ-417000/750 для блоков, подключаемых к РУВН.', style=st_5_5),
     # С. 160 Неклепаев
     Paragraph('Необходимая номинальная мощность рабочих трансформаторов собственных нужд:', style=st_5_10),
     fml(f'$S_{{Т_\u0020с.н._\u0020ном}} \u2265 S_{{Г_\u0020ном}} = {s_s_n:.1f}$'),
     Paragraph('Выбираем трансформаторы типа 2×ТРДНС-40000/35 с номинальным напряжением '
     'стороны ВН 24 кВ, а стороны НН - 6,3 кВ', style=st_5_5),
     # с. 134 Неклепаев

     Paragraph('Выбор варианта структурной схемы', style=s_b),
     Paragraph('Минимальное число блоков, подключенных к РУСН для питания потребителей', style=st_0_20),
     fml(f'$N_{{1_\u0020min}} = \\dfrac {{S_{{нг_\u0020max_\u0020з}}}} {{S\'_{{Г_\u0020ном}}}}; \\quad '  # {{\u0020 ном.}}
         f'N_{{1_\u0020min}} = {s_ld_max_w:.1f} \\div {s_g_:.1f} = {n1_:.1f} \u2248 {n1}$'),
     # fml(f'$N_{{1_\u0020min}} = \\dfrac {{P_{{нг_\u0020max_\u0020з}}}} {{P\\}}$'),  # {{\u0020 ном.}}
     #     f'N_{{1_\u0020min}} = {s_ld_max_w} \\div {s_g_} = {n1_c:.1f} \u2248 {n1}$'),
     Paragraph('Вариант 1', style=st_i_15_2),
     Paragraph('К стороне СН подключено минимальное число генераторов, к автотрансформаторам связи генераторы '
               'не подключены.', style=st_0_3),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\1 вар. из примера.png',
           width=15 * cm, height=10 * cm, kind='proportional'),
     Paragraph('Рис. 1 - 1-й вариант структурной схемы КЭС', style=s_cntr),
     Paragraph('Выбор автотрансформаторов связи', style=st_i_0_3),
     Paragraph('Режим 1', style=st_i_0_3),
     Paragraph('Передача максимального перетока избыточной мощности из стороны СН в сеть РУВН:', style=st_0_10),
     fml(f'$P_1 = P_{{изб_\u0020max}} = N_1 {{P\'}}_{{г_\u0020ном.}} - P_{{нг_\u0020л_\u0020min}}; \\quad'
         f'P_1 = {n1} \\cdot {p_g_:.1f} - {p_ld_min_sm:.1f} = {v1.p1:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_1 = Q_{{изб_\u0020max}} = N_1 {{Q\'}}_{{Г_\u0020 ном.}} - Q_{{нг_\u0020л_min}}; \\quad'
         f'Q_1 = {n1} \\cdot {q_g_:.1f} - {q_ld_min_sm:.1f} = {v1.q1:.1f}$ МВар'),
     sp_20,
     fml(f'$S_{{АТ_\u00201_\u0020расч}} = \\dfrac {{1}} {{2}} \\sqrt {{P_1^2 + Q_1^2}}; \\quad'
         f'S_{{АТ_\u00201_\u0020расч}} = \u221a ({v1.p1:.1f}^2 + {v1.q1:.1f}^2) \\div 2 = {v1.s1:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 1_\u0020ном}} \u2265 S_{{АТ_\u0020 1_\u0020 расч}}$'),
     Paragraph('Режим 2', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из автотрансформаторов связи при максимальном избытке мощности '
               'на стороне СН', style=st_0_10),
     fml(f'$P_2 = P_{{изб_\u0020max}} - P_{{ав._\u0020рез.}}; \\quad P_2 = {v1.p1:.1f} - {p_r} = {v1.p2:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_2 = Q_{{изб_\u0020max}} - P_{{ав._\u0020рез.}} tan(\\phi_{{г_\u0020ном}}); \\quad'
         f'Q_2 = {v1.q1:.1f} - {p_r:.1f} \\cdot {tg_g:.2f} = {v1.q2:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 2_\u0020 расч}} = \\dfrac {{\\sqrt{{P_2^2 + Q_2^2}}}} {{k_{{ав_\u0020рез}}}}; \\quad'
         f'S_{{АТ_\u0020 2_\u0020 расч}} = \u221a({v1.p2:.1f}^2 + {v1.q2:.1f}^2) \\div 2 = {v1.s2:.1f}$ МВ\u00B7А'),
     sp_20,
     # \u00b8 - верхний индекс 2
     fml(f'$S_{{АТ_\u0020 2_\u0020ном}} \u2265 S_{{АТ_\u0020 2_\u0020 расч}}$'),
     Paragraph('Режим 3', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН в режиме '
               'зимнего максимума нагрузки', style=st_0_10),
     fml(f'$P_3 = P_{{нг_\u0020з_\u0020max}} - \\left (N_1 - 1 \\right) {{P\'}}_{{г_\u0020ном}} + P_{{с.н.}}; \\quad '
         f'P_3 = {p_ld_max_w:.1f} - {n1 - 1} \\cdot {p_g_:.1f} + {p_s_n:.1f} = {v1.p3:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_3 = Q_{{нг_\u0020 з_\u0020 max}} - \\left (N_1 - 1 \\right) {{Q\'}}_{{г_\u0020ном}} + Q_{{с.н.}}; \\quad'
         f'Q_3 = {q_ld_max_w:.1f} - {n1 - 1} \\cdot {q_g_:.1f} + {q_s_n:.1f} = {v1.q3:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 3_\u0020 расч}} = \\dfrac {{\\sqrt{{P_3^2 + Q_3^2}}}} {{2}}; \\quad'
         f'S_{{АТ_\u0020 3_\u0020 расч}} = \u221a({v1.p3:.1f}^2 + {v1.q3:.1f}^2) \\div {2} = {v1.s3:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 3_\u0020ном}} \u2265 S_{{АТ_\u0020 3_\u0020расч}}$'),
     Paragraph('Режим 4', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН (ГРУ) в режиме летнего минимума '
               'нагрузки во время планового ремонта другого блока на стороне СН', style=st_0_10),
     fml(f'$P_4 = P_{{нг_\u0020л_\u0020max}} - \\left (N_1 - 2 \\right) {{P\'}}_{{г_\u0020ном}} + 2 P_{{с.н.}}; \\quad '
         f'P_4 = {p_ld_max_s:.1f} - {n1 - 2} \\cdot {p_g_:.1f} + 2 \\cdot {p_s_n:.1f} = {v1.p4:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_4 = Q_{{нг_\u0020 л_\u0020 max}} - \\left (N_1 - 2 \\right) '
         f'{{Q\'}}_{{г_\u0020 ном}} + 2Q_{{с.н.}}; \\quad'
         f'Q_4 = {q_ld_max_w:.1f} - {n1 - 2} \\cdot {q_g_:.1f} + {q_s_n:.1f} = {v1.q4:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 4_\u0020 расч}} = \\dfrac {{\\sqrt{{P_4^2 + Q_4^2}}}} {{2}}; \\quad'
         f'S_{{АТ_\u0020 4_\u0020 расч}} = \u221a({v1.p4:.1f}^2 + {v1.q4:.1f}^2) \\div {2} = {v1.s4:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 4_\u0020ном}} \u2265 S_{{АТ_\u0020 4_\u0020 расч}}$'),
     Paragraph('Автотрансформаторы связи выбирается по режиму с наибольшим перетоком мощности', st_10_3),
     Paragraph('Выбираем 7×АОДЦТН-333000/750/330 с номинальным напряжением обмотки НН 15,75 кВ', st_0_3),
     # с. 241 Файбисович, 162 Неклепаев

Paragraph('Вариант 2', style=st_i_10_5),
     Paragraph('К стороне СН подключено 4 генератора, к автотрансформаторам связи генераторы не подключены.',
               style=st_0_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\2 вар. из примера.png',
           width=15*cm, height=10*cm, kind='proportional'),
     Paragraph('Рис. 2 - 2-й вариант структурной схемы КЭС', style=s_c_t),
     # Paragraph('Выбор автотрансформаторов связи', style=st_0_3),
     Paragraph('Режим 1', style=st_i_0_3),
     Paragraph('Передача максимального перетока избыточной мощности из стороны СН в сеть РУВН:', style=st_0_10),
     fml(f'$P_1 = P_{{изб_\u0020max}} = N_{{1\u0020}} {{P\'}}_{{г_\u0020ном.}} - P_{{нг_\u0020л_min}}; \\quad'
         f'P_1 = {v2.n1_c} \\cdot {p_g_:.1f} - {p_ld_min_sm:.1f} = {v2.p1:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_1 = Q_{{изб_\u0020max}} = N_1 {{Q\'}}_{{Г_\u0020 ном.}} - Q_{{нг_\u0020л_min}}; \\quad'
         f'Q_1 = {v2.n1_c} \\cdot {q_g_:.1f} - {q_ld_min_sm:.1f} = {v2.q1:.1f}$ МВар'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 1_\u0020расч}} = \\dfrac {{1}} {{2}} \\sqrt {{P_1^2 + Q_1^2}}; \\quad'
         f'S_{{АТ_\u0020 1_\u0020расч}} = \u221a \\left({v2.p1:.1f}^2 + {v2.q1:.1f}^2\\right) \\div 2 = {v2.s1:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 1_\u0020ном}} \u2265 S_{{АТ_\u0020 1_\u0020расч}}$'),

     Paragraph('Режим 2', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из автотрансформаторов связи при максимальном избытке мощности '
               'на стороне СН (ГРУ)', style=st_0_10),
     fml(f'$P_2 = P_{{изб_\u0020max}} - P_{{ав._\u0020рез.}}; \\quad P_2 = {v2.p1:.1f} - {p_r} = {v2.p2:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_2 = Q_{{изб_\u0020max}} - P_{{ав._\u0020рез.}} \\tan(\\phi_{{г_\u0020ном}}); \\quad'
         f'Q_2 = {v2.q1:.1f} - {p_r:.1f} \\cdot {tg_g:.2f} = {v2.q2:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 2_\u0020расч}} = \\dfrac {{\\sqrt{{P_2^2 + Q_2^2}}}} {{k_{{ав_\u0020рез}}}}; \\quad'
         f'S_{{АТ_\u0020 2_\u0020расч}} = \u221a({v2.p2:.1f}^2 + {v2.q2:.1f}^2) \\div 2 = {v2.s2:.1f}$ МВ\u00B7А'),
     sp_15,
     # \u00b8 - верхний индекс 2
     fml(f'$S_{{АТ_\u0020 2_\u0020ном}} \u2265 S_{{АТ_\u0020 2_\u0020расч}}$'),

     Paragraph('Режим 3', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН в режиме '
               'зимнего максимума нагрузки', style=st_0_10),
     fml(f'$P_3 = P_{{нг_\u0020з_\u0020max}} - \\left (N_1 - 1 \\right) {{P\'}}_{{г_\u0020ном}} + P_{{с.н.}}; \\quad '
         f'P_3 = {p_ld_max_w:.1f} - {v2.n1_c - 1} \\cdot {p_g_:.1f} + {p_s_n:.1f} = {v2.p3:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_3 = Q_{{нг_\u0020 з_\u0020 max}} - \\left (N_1 - 1 \\right) {{Q\'}}_{{г_\u0020ном}} + Q_{{с.н.}}; \\quad'
         f'Q_3 = {q_ld_max_w:.1f} - {v2.n1_c - 1} \\cdot {q_g_:.1f} + {q_s_n:.1f} = {v2.q3:.1f}$ МВар'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 3_\u0020 расч}} = \\dfrac {{1}} {{2}} \\sqrt{{P_3^2 + Q_3^2}};\\quad'
         f'S_{{АТ_\u0020 3_\u0020 расч}} = \u221a({v2.p3:.1f}^2 + {v2.q3:.1f}^2) \\div {2} = {v2.s3:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 3_\u0020ном}} \u2265 S_{{АТ_\u0020 3_\u0020расч}}$'),

     Paragraph('Режим 4', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН (ГРУ) в режиме летнего минимума '
               'нагрузки во время планового ремонта другого блока на стороне СН', style=st_0_10),
     fml(f'$P_4 = P_{{нг_\u0020л_\u0020max}} - \\left (N_1 - 2 \\right) {{P\'}}_{{г_\u0020ном}} + 2 P_{{с.н.}}; \\quad '
         f'P_4 = {p_ld_max_s:.1f} - {v2.n1_c - 2} \\cdot {p_g_:.1f} + 2 \\cdot {p_s_n:.1f} = {v2.p4:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_4 = Q_{{нг_\u0020 л_\u0020 max}} - \\left (N_1 - 2 \\right) '
         f'{{Q\'}}_{{г_\u0020 ном}} + 2Q_{{с.н.}}; \\quad'
         f'Q_4 = {q_ld_max_w:.1f} - {v2.n1_c - 2} \\cdot {q_g_:.1f} + {q_s_n:.1f} = {v2.q3:.1f}$ МВар'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 4_\u0020 расч}} = \\dfrac {{1}} {{2}} \\sqrt{{P_4^2 + Q_4^2}}; \\quad'
         f'S_{{АТ_\u0020 4_\u0020 расч}} = \u221a({v2.p4:.1f}^2 + {v2.q4:.1f}^2) \\div {2} = {v2.s4:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 4_\u0020ном}} \u2265 S_{{АТ_\u0020 4_\u0020расч}}$'),
Paragraph('Вариант 3', style=st_i_10_5),
     Paragraph('К стороне СН подключено 3 генератора, к автотрансформаторам связи подключены 2 генератора',
               style=st_0_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\3 вар. из примера.png',
           width=15*cm, height=10*cm, kind='proportional'),
     Paragraph('Рис. 3 - 3 вариант структурной схемы КЭС', style=s_c_t),
     # Paragraph('Выбор автотрансформаторов связи', style=st_0_10),
     Paragraph('Режим 1', style=st_i_0_3),
     Paragraph('Передача максимального перетока избыточной мощности из стороны СН в сеть РУВН:', style=st_0_25),
     fml(f'$P_1 = \\dfrac {{P_{{изб_\u0020max}}}} {{2}} + {{P\'}}_{{г_\u0020ном.}}; \\quad'
         f'P_1 = {v3.n1_c} \\cdot {p_g_:.1f} - {p_ld_min_sm:.1f} = {v3.p1:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_1 = Q_{{изб_\u0020max}} = N_1 {{Q\'}}_{{Г_\u0020 ном.}} - Q_{{нг_\u0020л_\u0020min}}; \\quad'
         f'Q_1 = {v3.n1_c} \\cdot {q_g_:.1f} - {q_ld_min_sm:.1f} = {v3.q1:.1f}$ МВар'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 1_\u0020расч}} = \\dfrac {{1}} {{2}} \\sqrt {{P_1^2 + Q_1^2}}; \\quad'
         f'S_{{АТ_\u0020 1_\u0020расч}} = \u221a ({v3.p1:.1f}^2 + {v3.q1:.1f}^2) \\div 2 = {v3.s1:.1f}$ МВ\u00B7А'),
     sp_20,
     fml(f'$S_{{АТ_\u0020 1_\u0020ном}} \u2265 S_{{АТ_\u0020 1_\u0020расч}}$'),

     Paragraph('Режим 2', style=st_i_10_2),
     Paragraph('Аварийное отключение одного из автотрансформаторов связи при максимальном избытке мощности '
               'на стороне СН', style=st_0_10),
     fml(f'$P_2 = P_{{изб_\u0020max}} - P_{{ав._\u0020рез.}}; \\quad P_2 = {v3.p1:.1f} - {p_r} = {v3.p2:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_2 = Q_{{изб_\u0020max}} - P_{{ав._\u0020рез.}} \\tan(\\phi_{{г_\u0020ном}}); \\quad'
         f'Q_2 = {v3.q1:.1f} - {p_r:.1f} \\cdot {tg_g:.2f} = {v3.q2:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 2_\u0020расч}} = \\dfrac {{\\sqrt{{P_2^2 + Q_2^2}}}} {{k_{{ав_\u0020рез}}}}; \\quad'
         f'S_{{АТ_\u0020 2_\u0020расч}} = \u221a({v3.p2:.1f}^2 + {v3.q2:.1f}^2) \\div 2 = {v3.s2:.1f}$ МВ\u00B7А'),
     sp_25,
     # \u00b8 - верхний индекс 2
     fml(f'$S_{{АТ_\u0020 2_\u0020ном}} \u2265 S_{{АТ_\u0020 2_\u0020расч}}$'),

     Paragraph('Режим 3', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН в режиме '
               'зимнего максимума нагрузки', style=st_0_10),
     fml(f'$P_3 = P_{{нг_\u0020з_\u0020max}} - \\left (N_1 - 1 \\right) {{P\'}}_{{г_\u0020ном}} + P_{{с.н.}}; \\quad '
         f'P_3 = {p_ld_max_w:.1f} - {v3.n1_c - 1} \\cdot {p_g_:.1f} + {p_s_n:.1f} = {v3.p3:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_3 = Q_{{нг_\u0020 з_\u0020 max}} - \\left (N_1 - 1 \\right) {{Q\'}}_{{г_\u0020ном}} + Q_{{с.н.}}; \\quad'
         f'Q_3 = {q_ld_max_w:.1f} - {v3.n1_c - 1} \\cdot {q_g_:.1f} + {q_s_n:.1f} = {v3.q3:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 3_\u0020 расч}} = \\dfrac {{\\sqrt{{P_3^2 + Q_3^2}}}} {{2}}; \\quad'
         f'S_{{АТ_\u0020 3_\u0020 расч}} = \u221a({v3.p3:.1f}^2 + {v3.q3:.1f}^2) \\div {2} = {v3.s3:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 3_\u0020ном}} \u2265 S_{{АТ_\u0020 3_\u0020расч}}$'),

     Paragraph('Режим 4', style=st_i_5_2),
     Paragraph('Аварийное отключение одного из генераторов (блоков) на стороне СН в режиме летнего минимума '
               'нагрузки во время планового ремонта другого блока на стороне СН', style=st_0_10),
     fml(f'$P_4 = P_{{нг_\u0020л_\u0020max}} - \\left (N_1 - 2 \\right) {{P\'}}_{{г_\u0020ном}} + 2 P_{{с.н.}}; \\quad '
         f'P_4 = {p_ld_max_s:.1f} - ({v3.n1_c} - 2) \\cdot {p_g_:.1f} + 2 \\cdot {p_s_n:.1f} = {v3.p4:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_4 = Q_{{нг_\u0020 л_\u0020 max}} - \\left (N_1 - 2 \\right) '
         f'{{Q\'}}_{{г_\u0020 ном}} + 2Q_{{с.н.}}; \\quad'
         f'Q_4 = {q_ld_max_w:.1f} - ({v3.n1_c} - 2) \\cdot {q_g_:.1f} + {q_s_n:.1f} = {v3.q4:.1f}$ МВар'),
     sp_25,
     fml(f'$S_{{АТ_\u0020 4_\u0020 расч}} = \\dfrac {{\\sqrt{{P_4^2 + Q_4^2}}}} {{2}}; \\quad'
         f'S_{{АТ_\u0020 4_\u0020 расч}} = \u221a({v3.p4:.1f}^2 + {v3.q4:.1f}^2) \\div {2} = {v3.s4:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 4_\u0020ном}} \u2265 S_{{АТ_\u0020 4_\u0020расч}}$'),

     Paragraph('Режим 5', style=st_i_5_2),
     Paragraph('Возможный трансформаторный режим передачи мощности из стороны НН в сторону СН', style=st_0_20),
     fml(f'$S_{{АТ_\u0020 5_\u0020 расч}} = \\dfrac {{{{S\'}}_{{г_\u0020 ном}}}} {{k_{{выг}}}}; \\quad'
         f'S_{{АТ_\u0020 5_\u0020 расч}} = {s_g_:.1f} \\div {v3.k_p:.2f} = {v3.s5:.1f}$ МВ\u00B7А'),
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
'''
f = [Paragraph('Задание', style=s_b),
     Paragraph('Разработать структурную схему КЭС на газомазутном топливе. Рассмотреть возможные варианты '
         'структурной схемы электростанции и для каждого из них выбрать номинальные параметры основного '
         'силового оборудования', style=s_m),
Paragraph('Исходные данные:', style=s_b),
Paragraph('Установленная мощность, МВт', style=st_0_10),

fml(f'$S = {p_st}$'),
Paragraph('Число генераторов', style=s_f_10),
# fml(f'$n_г = {n_g}$'),
Paragraph('Генераторы, число и ном. мощность (МВт), расход на СН', style=s_f_10),
fml(f'${n_g} \\times {p_g}, {k_s_n*100:.0f}\\%$'),
# Paragraph(f'Коэффициенты мощности (cos φ) генераторов, механизмов собственных нужд и '
#           f'источников аварийного резерва энергосистемы одинаковые и равны 0.85'),
# Paragraph('Нагрузки потребителей', style=st_i_5_5),
Paragraph('Номинальное напряжение потребителей, кВ', style=s_f_10),
fml(f'$U = {u_ld}$'),
# Paragraph('Число потребителей и максимальная мощность в зимний период, МВт', style=s_f_20),
Paragraph('Число потребителей и максимальная мощность, МВт', style=s_f_10),
fml(f'${n_ld} \\times {p_ld}$'),
Paragraph('Коэффициент мощности потребителей, о. е.', style=s_f_10),
fml(f'$cos\\phi = {cos_ld}$'),
# Paragraph('Коэффициент одновременности', style=s_f_20),
# fml(f'$k_о = {k_s}$'),
# Paragraph('Коэффициент летнего минимума', style=s_f_20),
# fml(f'$k_{{л.min}} = {k_min}$'),
# Paragraph('Коэффициент летнего максимума', style=s_f_20),
# fml(f'$k_{{л.max}} = {k_sum_max}$'),
# Paragraph('Число часов использования максимума нагрузки', style=s_f_20),
# fml(f'$T_{{max}} = {t_max}$'),
# Paragraph('Система (сторона ВН)', style=st_i_5_5),
Paragraph('Номинальное напряжение системы (стороны ВН), кВ', style=s_f_10),
fml(f'$U = {u_s}$'),
Paragraph('Длина линий связи, км', style=s_f_10),
fml(f'$L = {l_ln}$'),
Paragraph('Мощность аварийного резерва, МВт', style=s_f_10),
fml(f'$S_{{ав.рез.}} = {s_r}$'),
Paragraph('Выбор генератора', style=st_b_10_2),
Paragraph('Выбираем генератор Т3В-800-2У3 со следующими электрическими параметрами:', style=s_m),
# Paragraph('Выбираем генератор ТВВ-800-2ЕКУ3 со следующими параметрами:', style=s_b),
# Table(data, colWidths=[1.9*cm] + [None] * (len(data[-1])- 1),
#       style=[('GRID', (0,0), (-1,-1), 1,colors.black)], hAlign='CENTER')
# Table(data = [[fml(f'$P_г$, МВт'), fml(f'$S_г$, МВА'), fml(f'$U_{{н.г}}$, кВ'),
#         Paragraph('Схема соединения обмоток', style=s_m), fml(f'${{x\'\'}}_d$, о.е.'),
#                fml(f'${{x\'}}_d$, о.е.'), fml(f'$x_d$, о.е.'), fml(f'$\\cos \\phi$, о.е.')],
#        [fml(f'${p_g}$'), fml(f'${s_g_c}$'), fml(f'${u_g}$'), Paragraph('Y/Y', style=s_m), fml(f'${x_d__}$'),
#         fml(f'${x_d_}$'), fml(f'${x_d}$'), fml(f'${cos_g}$')]],
#       style=[('GRID', (0,0), (-1,-1), 1,colors.black)], hAlign='CENTER')
# colWidths=50, rowHeights=20, spaceBefore=10, spaceAfter=20,
# Table(data, colWidths=[1.9*cm] + [None] * (len(data[-1])- 1),
#       style=[('GRID', (0,0), (-1,-1), 1,colors.black)], hAlign='CENTER')
# Table(data = [[fml(f'$P_Г$, МВт'), fml(f'$U_{{Г}}$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
#         fml(f'$Q_г = S_г \\cdot \\sin\\phi_г$, о.е.'), fml(f'$I_г$, кА'), fml(f'${{x\'\'}}_d$, о.е.'),
#                fml(f'${{x\'}}_d$, о.е.'), fml(f'$x_d$, о.е.')],
#        [fml(f'${p_g}$'), fml(f'${u_g}$'), fml(f'${s_g}$'), fml(f'${cos_g}$'), fml(f'${q_g}$'), fml(f'${i_g}$'),
#         fml(f'${x_d__}$'), fml(f'${x_d_}$'), fml(f'${x_d}$')]],
#       style=[('GRID', (0,0), (-1,-1), 1, colors.black)], hAlign='CENTER'),

      Table(data = [[fml(f'$P_Г$, МВт'), fml(f'$U_Г$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
                     fml(f'$Q_Г$, МВА'), fml(f'$I_Г$, МВА')],
                    [fml(f'${p_g}$'), fml(f'${u_g}$'), fml(f'${cos_g}$'), fml(f'${s_g}$'),
                     fml(f'${q_g:.1f}$'), fml(f'${i_g}$')]], colWidths=70, rowHeights=20, spaceBefore=5,
            spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1,colors.black)]),
# , ('ALIGN', (0, 0), (-1, -1), "CENTER") выравнивание элементов в таблице по ширине

Paragraph('Мощности нагрузок потребителей', style=s_b),
Paragraph('Зимний период', style=st_i_0_3),
Paragraph('Максимальная активная мощность нагрузки в зимний период', style=st_0_10),
fml(f'$P_{{нг_\u0020max_\u0020з}} = n_{{нг}}P_{{нг}}K_{{о}};$ где $k_о = {k_s}$ - коэффициент одновременности'),
sp_15,
fml(f'$P_{{нг_\u0020max_\u0020з}} = {n_ld} \\cdot {p_ld} \\cdot {k_s} = {p_ld_max_w:.0f}$ МВт'),
Paragraph('Максимальная реактивная мощность нагрузки в зимний период', style=st_5_10),
fml(f'$Q_{{нг_\u0020max_\u0020з}} = P_{{нг_max_з}}tg\\phi_{{нг}}; \\quad'
    f'Q_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\cdot {tg_ld:.2f} = {q_ld_max_w:.0f}$ Мвар'),
Paragraph('Максимальная полная мощность нагрузки в зимний период', style=st_5_20),
fml(f'$S_{{нг_\u0020max_\u0020з}} = \\dfrac {{S_{{нг_max_з}}}} {{cos \\phi_{{нг}}}}; \\quad'
    f'S_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\div {cos_ld} = {s_ld_max_w:.0f}$ МВ\u00B7А'),
Paragraph('Максимальная нагрузка в летний период', style=st_i_10_5),
Paragraph('Активная мощность нагрузки', style=st_0_10),
fml(f'$P_{{нг_\u0020max_\u0020л}} = P_{{нг_max_з}}K_{{max_л}};$ '
    f'где $K_{{max_\u0020л}} = {k_max_sm}$ - коэффициент летнего максимума'),
sp_15,
fml(f'$P_{{нг_\u0020max_\u0020л}} = {p_ld_max_w:.0f} \\cdot {k_max_sm} = {p_ld_max_s:.0f}$ МВт'),
Paragraph('Реактивная мощность нагрузки', style=st_5_10),
fml(f'$Q_{{нг_\u0020max_\u0020л}} = Q_{{нг_\u0020max_\u0020з}} K_{{max_\u0020л}}; \\quad'
    f'Q_{{нг_\u0020max_\u0020л}} = {q_ld_max_w:.0f} \\cdot {k_max_sm} = {q_ld_max_s:.0f}$ Мвар'),
Paragraph('Полная мощность нагрузки', style=st_5_10),
fml(f'$S_{{нг_\u0020max_\u0020л}} = S_{{нг_max_з}} k_{{max_л}}; \\quad'
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
Paragraph('Мощности собственных нужд', style=s_b),
Paragraph('Активная мощность с.н. агрегатов', style=st_0_10),
fml(f'$P_{{Г\u0020с.н.}} = k_{{с.н.}}P_{{Г\u0020ном}}; \\quad$ где $k_{{с.н.}}={k_s_n}$ - доля расхода на с.н.'),
sp_15,
fml(f'$P_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {p_g} = {p_s_n:.1f}$ МВт'),
Paragraph('Реактивная мощность с.н. агрегатов', style=st_0_10),
fml(f'$Q_{{Г_\u0020с.н.}} = k_{{с.н.}}P_{{Г_\u0020ном}}; \\quad '
    f'P_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {q_g} = {q_s_n:.1f}$ Мвар'),
Paragraph('Полная мощность с.н. агрегата', style=st_0_10),
fml(f'$S_{{Г_\u0020с.н.}} = k_{{с.н.}}S_{{Г\u0020ном}}; \\quad '
    f'S_{{Г_\u0020с.н.}} = {k_s_n} \\cdot {s_g} = {s_s_n:.1f}$ МВ\u00B7А'),
Paragraph('Номинальные мощности агрегатов с вычетом мощности с.н.', style=s_m),
Paragraph('Номинальная активная мощность агрегатов с вычетом мощности с.н.', style=st_0_10),
fml(f'${{P\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_ном}}; \\quad '
    f'{{P\'}}_{{Г_\u0020с.н.}} = {1 - k_s_n:.2f} \\cdot {p_g} = {p_g_:.1f}$ МВт'),
Paragraph('Номинальная реактивная мощность агрегатов с вычетом мощности с.н. ', style=st_0_10),
fml(f'${{Q\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_ном}}; \\quad '
    f'{{Q\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {q_g:.1f} = {q_g_:.1f}$ Мвар'),
Paragraph('Номинальная полная мощность агрегатов с вычетом мощности с.н. ', style=st_0_10),
fml(f'${{S\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})S_{{Г_ном}}; \\quad '
    f'{{S\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {s_g} = {s_g_:.1f}$ МВ\u00B7А'),
Paragraph('Выбор трансформаторов блоков по номинальной мощности осуществляется по условию:', style=st_5_10),
fml(f'$S_{{ТБ}} \u2265 {{S\'}}_{{Г_\u0020ном}} = {s_g_:.1f}$ МВ\u00B7А'),
# Paragraph('Выбираем трансформатор типа ТЦ-100000/330-69У1  номинальным напряжением стороны НН 24 кВ для '
#           'блоков подключенных к РУСН.', style=st_5_5),
# , и напряжением ВН 750 кВ, если блок подключается к РУВН. c. 157 Неклепаев
Paragraph('Выбираем трансформаторы типа ТНЦ-100000/500 c номинальным напряжением стороны НН 24 кВ для блоков, '
          'подключаемых к РУСН и 7×ОРЦ-417000/750 для блоков, подключаемых к РУВН', style=st_5_5),
# С. 160 Неклепаев
'''
'''
Table(data = [[fml(f'$P_Г$, МВт'), fml(f'$U_{{Г}}$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
               fml(f'$Q_г = S_г \\cdot \\sin\\phi_г$, о.е.'), fml(f'$I_г$, кА'), fml(f'${{x\'\'}}_d$, о.е.'),
               fml(f'${{x\'}}_d$, о.е.'), fml(f'$x_d$, о.е.')],
              [fml(f'${p_g}$'), fml(f'${u_g}$'), fml(f'${s_g}$'), fml(f'${cos_g}$'), fml(f'${q_g}$'), fml(f'${i_g}$'),
               fml(f'${x_d__}$'), fml(f'${x_d_}$'), fml(f'${x_d}$')]],
      style=[('GRID', (0,0), (-1,-1), 1, colors.black)], hAlign='CENTER'),

Paragraph('Необходимая номинальная мощность рабочих трансформаторов собственных нужд:', style=st_5_10),
fml(f'$S_{{Т_\u0020с.н._\u0020ном}} \u2265 S_{{Г_\u0020ном}} = {s_s_n:.1f}$'),
Paragraph('Выбираем трансформаторы типа 2×ТРДНС-40000/35 с номинальным напряжением '
          'стороны ВН 24 кВ, а стороны НН - 6,3 кВ', style=st_5_5),
# с. 134 Неклепаев

# .setStyle([('LEADING', 10)]),
# Paragraph('https://ciu.nstu.ru/kaf/persons/676/a/file_get/293101?nomenu=1', style=s_m)]
# '''
# ]

doc.build(f, onLaterPages=addPageNumber)
# doc.build(f)
