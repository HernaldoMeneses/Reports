
import conect as cc
#
list_CodFornec = ['3026', '3114','3809' ]
report_list_322_06 = []
report_list_322_17 = []
report_list_227 = []
report_others = ['324_P2']
for item in list_CodFornec:
    #report_list_322_06 = ['322_17_F-3809', '322_06_F-3114']
    new = ''
    new = '322_06_F-' + item
    report_list_322_06.append(new)
    new = ''
    new = '322_17_F-' + item
    report_list_322_17.append(new)
    new = ''
    new = '227_F-' + item
    report_list_227.append(new)

report_list_322 = report_list_322_06 + report_list_322_17    
report_list = report_list_322 + report_list_227 + report_others
for i in report_list:
    Sql_name = i
    cc.generate_report(Sql_name)
