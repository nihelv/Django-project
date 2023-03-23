from django.shortcuts import render
import random
import time


def day_of_the_week(week_day, lang_type='en'):
    """
    Check Day Of The Week
    0:Mon(월), 1:Tue(화), 2:Wed(수), 3:Thu(목), 4:Fri(금), 5:Sat(토), 6:Sun(일)
    :param week_day: Week Day
    :param lang_type: Return Lang(Default:En)
    :return:
    """
    tm = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    if lang_type == 'ko':
        tm = ['월', '화', '수', '목', '금', '토', '일']
    return tm[week_day]


if __name__ == '__main__':
    # 오늘 날짜의 요일
    wday = time.localtime().tm_wday




def today_dinner(request):
        
    menu=['햄버거', '치킨', '피자', '초밥']
    wday = time.localtime().tm_wday
    contents = {
        'menu' : random.choice(menu), 'day' : day_of_the_week(wday, lang_type='ko')
    }
    
    
    # contents2 = {
    #     'day' : day_of_the_week(wday, lang_type='ko')
    # }

    return render(request, 'today_dinner.html', contents)