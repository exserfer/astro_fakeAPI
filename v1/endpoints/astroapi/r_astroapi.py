import json
import string
import logging
import random

from datetime import timedelta, datetime, date

from fastapi import APIRouter, Depends, Request

from config import prnt



router_astroapi = APIRouter(
    prefix="/v1/horoscope_prediction",
    tags=["Horoscope"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


# Негератор случайной строки
async def randomword(length:int) -> str:
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))


# Генератор ебанного текст
# async def get_prediction(sign: str = 'aries', period: str = 'today'):
#     current_period = {
#         "yesterday": date.today() - timedelta(days=1),
#         'today': date.today(),
#         "tomorrow": date.today() + timedelta(days=1),
#         "weekly": f'{date.today()}-{date.today() + timedelta(days=7)}',
#         "monthly": 'April 2022',
#     }
#     rnd_length = random.randrange(5, 10)
#     random_word = await randomword(rnd_length)
#     rnd_str = f"{random.random()}:{random_word}"

#     key_select = 'daily' if period in ("yesterday", 'today', "tomorrow") else period

#     data_response = {
#         "daily" : {
#             "status": True,
#             "sun_sign": sign,
#             "prediction_date": current_period[period],
#             "prediction": {
#                 # "random_string": rnd_str,
#                 "health": "On the health front, there may be a minor digestive disorder, but rest assured it will be nothing serious.",
#                 "emotions": "You are feeling rather good and it seems that you can place the pulse of success easily. You will be profusely passionate about things today.",
#                 "personal_life": "Your rapport with relatives and associates will be good. Go out for a fun filled evening and you are likely to become the life and soul of the celebrations. Following your instincts today can lead to great things in your personal life and relationships.",
#                 "profession": "You shall become optimistic and invest more working hours, to get better results. A number of opportunities will open up and you are more than ready to take full advantage of them. Even for people in jobs, things are likely keep you extremely busy.",
#                 "travel": "Destiny smiles on you today. Make the most of the chances that comes your way.",
#                 "luck": "Today is your lucky day. Don't be shy about expressing your true feelings or you will lose a very good opportunity."
#             }
#         },
#         "weekly": {
#             "status": True,
#             "sun_sign": sign,
#             "prediction_start_date": "21 April 2022", 
#             "prediction_end_date": "28 April 2022", 
#             "prediction": "This is sample weekly report. A week filled with energy and activities makes you busy throughout. You enjoy love relationship, passion, beauty in everyway. Indulge yourself into some creativity as your creative vision can bring you great benefits. Visit an art exhibition or buy an antique art for your home, creative artwork or paintings can enhance you mood.Mid of the week might give you a feel of confused state it where decision making would be difficult, but things will get sorted as the weekend gets near. Love matters will blossom - a best time to go out on date, resolve conflicts, make up time for love, as this is week self expression comes easily. Your high energy levels shall keep you moving this week, it is your responsibility to maintain it thorough out. A good fitness plan along with the diet can help you achieve the goals, remember being consistent can make you reach there much faster!"
#         },
#         "monthly": {
#             "status": True,
#             "sun_sign": sign,
#             "prediction_month": "April",
#             "prediction": [
#                 "This is an ideal way to start the New Year as Aries have their planet Mars in the first house and so while Mars will encounter stiff opposition from the big heavies Pluto and Saturn by square, as it passes through your first house, you will have the energy to handle the questions these planets will ask of your commitment and strength.",
#                 "This is not a time for frivolous goals, these will quickly go by the wayside, this is a time when your most important goals must become your priority.",
#                 "You feel a great call to action and yet you sense that what you are setting up for will require commitment and will test your character. The powers that be in your life will resist what you intend, you should bear in mind that the very people you may respect or defer to could be the same people that now want to stand in your way and you now need to review your relationship with them.",
#                 "If you are happy with the course you are on, the effect of Jupiter will reinforce what you are doing adding energy and some luck at critical moments; if you have been struggling, this can be a time where you are more at peace with the unchangeable circumstances and have faith that you will prevail eventually.",
#                 "Aries are very open, this means that in relationships you are eager to share your deeper feelings and fears and that opens the gateway to some substantial sharing and progresses. Things get psychologically intimate quite quickly and in new love affairs you may find that similar family backgrounds or similar experience (good and bad) with parents draw you to a person and cement a bond.",
#                 "It is a time of positive experiences with others, not just in terms of having fun superficially but in terms of meaningful interaction and reaches the deeper parts of you. Much of what is good in love happens not so much in terms of external experience, but in terms of the affect a new person in your life has on you internally, they may just spark something or reawaken an energy you had not felt for some time."
#             ]
#         }
#     }
    
#     return data_response[key_select]


# Генератор ебанного текст
async def get_prediction(sign: str = 'aries', period: str = 'today'):
    current_period = {
        "yesterday": date.today() - timedelta(days=1),
        'today': date.today(),
        "tomorrow": date.today() + timedelta(days=1),
        "weekly": f'{date.today()}-{date.today() + timedelta(days=7)}',
        "monthly": 'May 2022',
    }

    key_select = 'daily' if period in ("yesterday", 'today', "tomorrow") else period

    data_response = {
        "daily" : {
            "status": True,
            "sun_sign": sign,
            "prediction_date": current_period[period],
            "prediction": {
                "health": "On the health",
                "emotions": "You are feeling",
                "personal_life": "Your rapport with.",
                "profession": "You shall become.",
                "travel": "Destiny smiles on you today.",
                "luck": "Today is your lucky day."
            }
        },
        "weekly": {
            "status": True,
            "sun_sign": sign,
            "prediction_start_date": "21 April 2022", 
            "prediction_end_date": "28 April 2022", 
            "prediction": "This is sample"
        },
        "monthly": {
            "status": True,
            "sun_sign": sign,
            "prediction_month": "April",
            "prediction": [
                "This is an ideal.",
                "This is not a time.",
                "You feel a great.",
                "If you are happy.",
                "Aries are very.",
                "It is a time."
            ]
        }
    }
    
    return data_response[key_select]


# Основной раздел
@router_astroapi.get("/")
async def astroapi():
    return {"error": False, "msg": 'AstroAPI'}


# Прогноз на сегодня
@router_astroapi.post("/daily/{zodiacName:str}")
async def horoscope_today(zodiacName: str = None):
    prediction = await get_prediction(sign=zodiacName, period='today')
    
    if prediction:
        prnt(prediction, '... Тип переменной prediction')
        return prediction

    logging.error('... There was a glitch when I received the prediction. The prediction is probably empty.')
    return {"error": False, "msg": f'today for _{zodiacName}_'}


# Прогно на завтра 
@router_astroapi.post("/daily/next/{zodiacName:str}")
async def horoscope_tomorrow(zodiacName: str = None):
    prediction = await get_prediction(sign=zodiacName, period='tomorrow')
    if prediction:
        prnt(prediction, '... Тип переменной prediction')
        return prediction

    return {"error": False, "msg": f'today for _{zodiacName}_'}


# Прогно на завтра 
@router_astroapi.post("/daily/previous/{zodiacName:str}")
async def horoscope_yesterday(zodiacName: str = None):
    prediction = await get_prediction(sign=zodiacName, period='yesterday')
    if prediction:
        prnt(prediction, '... Тип переменной prediction')
        return prediction

    return {"error": False, "msg": f'today for _{zodiacName}_'}


# Прогно на НЕДЕЛЮ
@router_astroapi.post("/weekly/{zodiacName:str}")
async def horoscope_yesterday(zodiacName: str = None):
    prediction = await get_prediction(sign=zodiacName, period='weekly')
    if prediction:
        prnt(prediction, '... Тип переменной prediction')
        return prediction

    return {"error": False, "msg": f'today for _{zodiacName}_'}


# Прогно на МЕСЯЦ
@router_astroapi.post("/monthly/{zodiacName:str}")
async def horoscope_yesterday(zodiacName: str = None):
    prediction = await get_prediction(sign=zodiacName, period='monthly')
    if prediction:
        prnt(prediction, '... Тип переменной prediction')
        return prediction

    return {"error": False, "msg": f'today for _{zodiacName}_'}
