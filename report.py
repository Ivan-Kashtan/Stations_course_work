# Курсовая станции
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.platypus.flowables import ParagraphAndImage, Spacer, KeepTogether, CondPageBreak, Image
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

from var1 import *

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
s_110 = Spacer(0, 120)
s_120 = Spacer(0, 120)
s_130 = Spacer(0, 130)
s_150 = Spacer(0, 150)
cpb = CondPageBreak(10)

# data = [[fml()(f'$P_г$, МВт'), fml()(f'$S_г$, МВА'), fml()(f'$U_{{н.г}}$, кВ'),
#              Paragraph('Схема соединения обмоток', style=s_m),],
#             [fml()(f'${p_g}$'), fml()(f'${s_g_c}$'), fml()(f'${u_g}$'), Paragraph('Y/Y', style=s_m),]]

f = [KeepTogether([mn, t_u, un, s_80, kaf, s_80, tp, title, var, s_120, fac, gr, st, tchr, mk, s_110, sity]),
     Paragraph('Задание', style=s_b),
     Paragraph('Разработать структурную схему КЭС на газомазутном топливе. Рассмотреть возможные варианты '
               'структурной схемы электростанции и для каждого из них выбрать номинальные параметры основного '
               'силового оборудования', style=s_m),
     Paragraph('Исходные данные:', style=s_b),
     Paragraph('Установленная мощность, МВт', style=st_0_10),
     fml(f'$S = {p_st}$'),
     # Paragraph('Число генераторов', style=s_f_20),
     # fml()(f'$n_г = {n_g}$'),
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
     # fml()(f'$k_о = {k_s}$'),
     # Paragraph('Коэффициент летнего минимума', style=s_f_20),
     # fml()(f'$k_{{л.min}} = {k_min}$'),
     # Paragraph('Коэффициент летнего максимума', style=s_f_20),
     # fml()(f'$k_{{л.max}} = {k_sum_max}$'),
     # Paragraph('Число часов использования максимума нагрузки', style=s_f_20),
     # fml()(f'$T_{{max}} = {t_max}$'),
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
     # Table(data = [[fml()(f'$P_г$, МВт'), fml()(f'$S_г$, МВА'), fml()(f'$U_{{н.г}}$, кВ'),
     #         Paragraph('Схема соединения обмоток', style=s_m), fml()(f'${{x\'\'}}_d$, о.е.'),
     #                fml()(f'${{x\'}}_d$, о.е.'), fml()(f'$x_d$, о.е.'), fml()(f'$\\cos \\phi$, о.е.')],
     #        [fml()(f'${p_g}$'), fml()(f'${s_g_c}$'), fml()(f'${u_g}$'), Paragraph('Y/Y', style=s_m), fml()(f'${x_d__}$'),
     #         fml()(f'${x_d_}$'), fml()(f'${x_d}$'), fml()(f'${cos_g}$')]],
     #       style=[('GRID', (0,0), (-1,-1), 1,colors.black)], hAlign='CENTER')
# colWidths=50, rowHeights=20, spaceBefore=10, spaceAfter=20,
# Table(data, colWidths=[1.9*cm] + [None] * (len(data[-1])- 1),
     #       style=[('GRID', (0,0), (-1,-1), 1,colors.black)], hAlign='CENTER')
     # Table(data = [[fml()(f'$P_Г$, МВт'), fml()(f'$U_{{Г}}$, кВ'), fml()(f'$\\cos \\phi$, о.е.'), fml()(f'$S_Г$, МВА'),
     #         fml()(f'$Q_г = S_г \\cdot \\sin\\phi_г$, о.е.'), fml()(f'$I_г$, кА'), fml()(f'${{x\'\'}}_d$, о.е.'),
     #                fml()(f'${{x\'}}_d$, о.е.'), fml()(f'$x_d$, о.е.')],
     #        [fml()(f'${p_g}$'), fml()(f'${u_g}$'), fml()(f'${s_g}$'), fml()(f'${cos_g}$'), fml()(f'${q_g}$'), fml()(f'${i_g}$'),
     #         fml()(f'${x_d__}$'), fml()(f'${x_d_}$'), fml()(f'${x_d}$')]],
     #       style=[('GRID', (0,0), (-1,-1), 1, colors.black)], hAlign='CENTER'),
           Table(data = [[fml(f'$P_Г$, МВт'), fml(f'$U_Г$, кВ'), fml(f'$\\cos \\phi$, о.е.'), fml(f'$S_Г$, МВА'),
                          fml(f'$Q_Г$, МВА'), fml(f'$I_Г$, МВА')],
                         [fml(f'${p_g}$'), fml(f'${u_g}$'), fml(f'${cos_g}$'), fml(f'${s_g}$'),
                          fml(f'${q_g:.1f}$'), fml(f'${i_g}$')]], colWidths=70, rowHeights=20, spaceBefore=5,
                 spaceAfter=5, style=[('GRID', (0,0), (-1,-1), 1,colors.black)]),
     # , ('ALIGN', (0, 0), (-1, -1), "CENTER") выравнивание элементов в таблице по ширине
     Paragraph('Мощности нагрузки потребителей', style=s_b),
     Paragraph('Зимний период', style=st_i_0_3),
     Paragraph('Максимальная активная мощность нагрузки в зимний период', style=st_0_10),
     fml(f'$P_{{нг_\u0020max_\u0020з}} = n_{{нг}}P_{{нг}}K_{{о}};$ где $k_о = {k_s}$ - коэффициент одновременности'),
     sp_15,
     fml(f'$P_{{нг_\u0020max_\u0020з}} = {n_ld} \\cdot {p_ld} \\cdot {k_s} = {p_ld_max_w:.0f}$ МВт'),
     Paragraph('Максимальная реактивная мощность нагрузки в зимний период', style=s_f_10),
     fml(f'$Q_{{нг_\u0020max_\u0020з}} = P_{{нг_max_з}}tg\\phi_{{нг}}; \\quad'
         f'Q_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\cdot {tg_ld:.2f} = {q_ld_max_w:.0f}$ Мвар'),
     Paragraph('Максимальная полная мощность нагрузки в зимний период', style=st_5_20),
     fml(f'$S_{{нг_\u0020max_\u0020з}} = \\dfrac {{S_{{нг_max_з}}}} {{cos \\phi_{{нг}}}}; \\quad'
         f'S_{{нг_\u0020max_\u0020з}} = {p_ld_max_w:.0f} \\div {cos_ld} = {s_ld_max_w:.0f}$ МВ\u00B7А'),
     Paragraph('Максимальная нагрузка в летний период', style=st_i_10_5),
     Paragraph('Активная мощность нагрузки', style=st_0_10),
     fml(f'$P_{{нг_\u0020max_\u0020л}} = P_{{нг_\u0020max_\u0020з}}K_{{max_\u0020л}};$ '
         f'где $K_{{max_\u0020л}} = {k_max_sm}$ - коэффициент летнего максимума'),
     sp_15,
     fml(f'$P_{{нг_\u0020max_\u0020л}} = {p_ld_max_w:.0f} \\cdot {k_max_sm} = {p_ld_max_s:.0f}$ МВт'),
     Paragraph('Реактивная мощность нагрузки', style=s_f_10),
     fml(f'$Q_{{нг_\u0020max_\u0020л}} = Q_{{нг_\u0020max_\u0020з}} K_{{max_\u0020л}}; \\quad'
         f'Q_{{нг_\u0020max_\u0020л}} = {q_ld_max_w:.0f} \\cdot {k_max_sm} = {q_ld_max_s:.0f}$ Мвар'),
     Paragraph('Полная мощность нагрузки', style=s_f_10),
     fml(f'$S_{{нг_\u0020max_\u0020л}} = S_{{нг_\u0020max_\u0020з}} k_{{max_\u0020л}}; \\quad'
         f'S_{{нг_\u0020max_\u0020л}} = {s_ld_max_w:.0f} \\cdot {k_max_sm} = {s_ld_max_s:.0f}$ МВ\u00B7А'),
     Paragraph('Минимальная нагрузка в летний период', style=st_i_5_5),
     Paragraph('Активная мощность нагрузки', style=st_0_10),
     fml(f'$P_{{нг_\u0020min_\u0020л}} = P_{{нг_\u0020max_\u0020з}}K_{{min_\u0020л}};$ '
         f'где $K_{{min_\u0020л}} = {k_min_sm}$ - коэффициент летнего минимума'),
     sp_20,
     fml(f'$P_{{нг_\u0020min_\u0020л}} = {p_ld_max_w:.0f} \\cdot {k_min_sm} = {p_ld_min_sm:.0f}$ МВт'),
     Paragraph('Реактивная мощность нагрузки', style=s_f_10),
     fml(f'$Q_{{нг_\u0020min_\u0020л}} = Q_{{нг_\u0020max_\u0020з}} K_{{min_\u0020л}}; \\quad'
         f'Q_{{нг_\u0020min_\u0020л}} = {q_ld_max_w:.0f} \\cdot {k_min_sm} = {q_ld_min_sm:.0f}$ Мвар'),
     Paragraph('Полная мощность нагрузки', style=s_f_10),
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
         f'S_{{Г_с.н.}} = {k_s_n} \\cdot {s_g} = {s_s_n:.1f}$ МВ\u00B7А'),
     Paragraph('Номинальные мощности агрегатов с вычетом мощности с.н.', style=s_m),
     Paragraph('Номинальная активная мощность агрегатов с вычетом мощности с.н.', style=st_0_10),
     fml(f'${{P\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_\u0020ном}}; \\quad '
         f'{{P\'}}_{{Г_с.н.}} = {1 - k_s_n:.2f} \\cdot {p_g} = {p_g_:.1f}$ МВт'),
     Paragraph('Номинальная реактивная мощность агрегатов с вычетом мощности с.н. ', style=st_0_10),
     fml(f'${{Q\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})P_{{Г_\u0020ном}}; \\quad '
         f'{{Q\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {q_g:.1f} = {q_g_:.1f}$ Мвар'),
     Paragraph('Номинальная полная мощность агрегатов с вычетом мощности с.н. ', style=st_0_10),
     fml(f'${{S\'}}_{{Г_\u0020ном}} = (1-k_{{с.н.}})S_{{Г_\u0020ном}}; \\quad '
         f'{{S\'}}_{{Г_\u0020ном}} = {1-k_s_n:.2f} \\cdot {s_g} = {s_g_:.1f}$ МВ\u00B7А'),
     Paragraph('Выбор трансформаторов блоков по номинальной мощности осуществляется по условию:', style=s_f_10),
     fml(f'$S_{{ТБ}} \u2265 {{S\'}}_{{Г_\u0020ном}} = {s_g_:.1f}$ МВ$\\cdot$А'),
     Paragraph('Выбираем трансформаторы типа ТНЦ-100000/500 для блоков, подключаемых к РУСН и 7×ОРЦ-417000/750 '
               'для блоков, подключаемых к РУВН', style=st_5_5),  # С. 160 Неклепаев
     Paragraph('Необходимая номинальная мощность рабочих трансформаторов собственных нужд', style=s_f_10),
     fml(f'$S_{{Т_\u0020с.н.}} \u2265 {{S}}_{{Г_\u0020с.н.}} = {s_s_n:.1f}$ МВ$\\cdot$А'),
     Paragraph('Выбираем трансформаторы  2×ТРДНС-40000/35 с номинальным напряжением стороны ВН 24 кВ, '
               'а стороны НН - 6,3 кВ.', style=st_5_5),  # с. 134 Неклепаев
     Paragraph('Выбор варианта структурной схемы', style=s_b),
     Paragraph('Минимальное число блоков, подключенных к РУСН для питания потребителей', style=st_0_10),
     fml(f'$N_{{1_\u0020min}} = \\dfrac {{S_{{нг_\u0020max_\u0020з}}}} {{S\'_{{Г_\u0020ном}}}}; \\quad '  # {{\u0020 ном.}}
         f'N_{{1_\u0020min}} = {s_ld_max_w} \\div {s_g_} = {n1_c:.1f} \u2248 {n1}$'),
     # fml(f'$N_{{1_\u0020min}} = \\dfrac {{P_{{нг_\u0020max_\u0020з}}}} {{P\\}}$'),  # {{\u0020 ном.}}
     #     f'N_{{1_\u0020min}} = {s_ld_max_w} \\div {s_g_} = {n1_c:.1f} \u2248 {n1}$'),
          Paragraph('Вариант 1', style=st_i_10_5),
     Paragraph('К стороне СН подключено минимальное число генераторов, к автотрансформаторам связи генераторы '
               'не подключены.', style=st_0_10),
     Image(r'C:\Users\kasht\Documents\Учёба\6 семестр\Станции\Курсовая\Компас\Схемы\1 вар. из примера.png',
           width=15*cm, height=10*cm, kind='proportional'),
     Paragraph('Рис. 1 - 1 вариант структурной схемы КЭС', style=s_c_t),
     Paragraph('Выбор автотрансформаторов связи', style=st_0_10),
     Paragraph('Режим 1', style=st_i_0_3),
     Paragraph('Передача максимального перетока избыточной мощности из стороны СН в сеть РУВН:', style=st_0_10),
     fml(f'$P_1 = P_{{изб_\u0020max}} = N_1 {{P\'}}_{{г_\u0020ном.}} - P_{{нг_\u0020л_min}}; \\quad'
         f'P_1 = {n1} \\cdot {p_g_:.1f} - {p_ld_min_sm:.1f} = {p1:.1f}$ МВт'),
     sp_15,
     fml(f'$Q_1 = Q_{{изб_\u0020max}} = N_1 {{Q\'}}_{{Г_\u0020 ном.}} - Q_{{нг_\u0020л_min}}; \\quad'
         f'Q_1 = {n1} \\cdot {q_g_:.1f} - {q_ld_min_sm:.1f} = {q1:.1f}$ МВар'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 1_\u0020расч}} = \\dfrac {{1}} {{2}} \\sqrt {{P_1^2 + Q_1^2}}; \\ quad'
         f'S_{{АТ_\u0020 1_\u0020расч}} = \u221a ({p1:.1f} \u00b8 + {q1:.1f} \u00b8) \\div 2 = {s1:.1f}$ МВ\u00B7А'),
     sp_15,
     fml(f'$S_{{АТ_\u0020 1_\u0020расч}} = \\dfrac {{1}} {{2}} \\sqrt {{P_1^2 + Q_1^2}}; \\ quad'
         f'S_{{АТ_\u0020 1_\u0020расч}} = \u221a ({p1} \u00b8 + {q1} \u00b8) \\div 2 = {s1:.1f}$ МВ\u00B7А'),
     sp_15,

     # Paragraph('Номинальная активная мощность', style=s_m),
     # .setStyle([('LEADING', 10)]),
     # Paragraph('https://ciu.nstu.ru/kaf/persons/676/a/file_get/293101?nomenu=1', style=s_m)]
     ]
doc.build(f, onLaterPages=addPageNumber)
