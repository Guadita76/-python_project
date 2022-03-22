from datetime import date, datetime, timedelta,timezone

def calculo_fecha_cumple (bd:str) -> datetime:

  bd = bd.split("/")
  fecha_actual = datetime.now()


  birth_day = datetime (year = int(bd[0]) ,month= int(bd[1]), day= int(bd[2]))


  rest_day = fecha_actual - birth_day

  print (rest_day.total_seconds())

