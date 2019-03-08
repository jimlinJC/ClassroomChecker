from django.shortcuts import render
from django.http import HttpResponse
import datetime
import requests
from bs4 import BeautifulSoup
today = datetime.date.today()
now = datetime.datetime.now()
nextClass = now+datetime.timedelta(0,hours=1)
src = "http://stuinfo.ntust.edu.tw/classroom_user/classroom_usecondition.aspx"
period = []
period.append([])
period.append([])
period[0].append('0')
period[0].append('0800')
period[0].append('0901')
period[0].append('1001')
period[0].append('1111')
period[0].append('1211')
period[0].append('1311')
period[0].append('1411')
period[0].append('1511')
period[0].append('1621')
period[0].append('1721')
period[0].append('1821')
period[0].append('1916')
period[0].append('2011')
period[0].append('2106')
# -----------------------------------
period[1].append('0')
period[1].append('0900')
period[1].append('1000')		
period[1].append('1110')
period[1].append('1210')
period[1].append('1310')
period[1].append('1410')
period[1].append('1510')
period[1].append('1620')
period[1].append('1720')
period[1].append('1820')
period[1].append('1915')
period[1].append('2010')
period[1].append('2105')
period[1].append('2200')
# ------------------------------------



def home_view(request, *args, **kwargs):
    context = {'noneUsedClassroomNow' : checkTRclassroomNow(), 'noneUsedClassroomNext' : checkTRclassroomNext()}
    return render(request, 'showclassroom.html', context)

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})
    
def checkTRclassroomNow():
    theNoneUsed = []
    theClassTime = ''
    tabledata = getClassroom()
    for classroom in tabledata:
        for i in range(1,15):
            # print(int(period[0][i]),'--',int(now.strftime('%H%M')),'--',int(period[1][i]),'--',int(now.strftime('%H%M')))
            if(int(period[0][i]) <= int(now.strftime('%H%M')) and int(period[1][i]) >= int(now.strftime('%H%M'))): 
                if(tabledata[classroom][i] == ''):
                    print(classroom)
                    theNoneUsed.append(classroom)
                    theClassTime = str(i)
                    
                
    if theNoneUsed:
        return { theClassTime : theNoneUsed }
    else :
        return('its breaktime now')


def checkTRclassroomNext():
    theNoneUsed = []
    theClassTime = ''
    tabledata = getClassroom()
    for classroom in tabledata:
        for i in range(1,15):
            if(int(period[0][i]) <= int(nextClass.strftime('%H%M')) and int(period[1][i]) >= int(nextClass.strftime('%H%M'))): 
                if(tabledata[classroom][i] == ''):
                    print(classroom)
                    theNoneUsed.append(classroom)
                    theClassTime = str(i)

    if theNoneUsed:
        return { theClassTime : theNoneUsed }
    else :
        return('its break time next class')

def getClassroom():
    theday = datetime.date(2019,2,26)
    toPost = {
            "__EVENTTARGET": "date_cal",
            "__EVENTARGUMENT": 6996+(today-theday).days,
            "classlist_ddl": "TR",
            "__VIEWSTATE": "dDw1NTk0MzU4NjE7dDw7bDxpPDE+Oz47bDx0PDtsPGk8Mz47aTw0Pjs+O2w8dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PDtsPGk8NT47PjtsPHQ8QDA8cDxwPGw8U0Q7PjtsPGw8U3lzdGVtLkRhdGVUaW1lLCBtc2NvcmxpYiwgVmVyc2lvbj0xLjAuNTAwMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODk8MjAxNy0xMi0wNT47Pjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47Pj47Pj47Pj47Pu5S1476NkYk5hmd81mL76xisA4B",
            "__VIEWSTATEGENERATOR": "D2C5BC33"
    }
    req = requests.post(src, data=toPost)
    html_data = BeautifulSoup(req.text, "html5lib")
    table_data = { row("td", nowrap="nowrap")[0].text.strip() :[cell.text.strip() for cell in row("td", nowrap="nowrap")]
                for row in html_data.table("tr", nowrap="nowrap")}
    return table_data


    # -------------------------------------------------------------------------------------------------------------



    # 
    # print('\n-------------------------------------------------')
    # print(now)
    # print(nextClass)
    # print('-------------------------------------------------\n')




    # # ----------------------------------------------------------------------------------------------------------------------




    
    #             
    #         elif(int(period[0][i]) > int(nextClass.strftime('%H%M')) and int(period[1][i-1]) < int(nextClass.strftime('%H%M'))):
    #             nowIsBreakTime = True


    # if nowIsBreakTime == True:
    #     print('its break time now')
    #     nowIsBreakTime = False
    # else:
    #     print(f'\nthe not used classroom between {theNextClassTime}')

    


