from services.price_tracker_service import track_bitcoin_price
import asyncio
import datetime
import math
from zoneinfo import ZoneInfo

#HORARIOS = ["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"]
HORARIOS = ["16:59", "17:05", "17:10", "17:15", "17:25", "17:32"]
FUSO_BRASIL = ZoneInfo("America/Sao_Paulo")


async def price_check_loop():
    print("[SCHEDULER] Serviço iniciado...")

    while True:
        proximo = proximo_horario()
        agora = datetime.datetime.now(FUSO_BRASIL)

        segundos_espera = (proximo - agora).total_seconds()
        minutos_espera = math.ceil(segundos_espera / 60)

        print(f"[SCHEDULER] Próxima execução agendada para: {proximo.strftime('%d/%m/%Y %H:%M')}")
        print(f"[SCHEDULER] Aguardando {minutos_espera} minutos...\n")

        await asyncio.sleep(segundos_espera)

        try:
            print("[SCHEDULER] Iniciando verificação do preço do Bitcoin...")
            await track_bitcoin_price(proximo.strftime("%d/%m/%Y %H:%M"))
            print("[SCHEDULER] Verificação finalizada com sucesso.\n")
        except Exception as e:
            print(f"[SCHEDULER][ERRO] Falha durante a verificação: {e}\n")



def proximo_horario() -> datetime.datetime:
    agora = datetime.datetime.now(FUSO_BRASIL)
    hoje = agora.date()

    horarios_datetime = []

    for h in HORARIOS:
        horario_dt = datetime.datetime.strptime(h, "%H:%M").replace(year=hoje.year, month=hoje.month, day=hoje.day, tzinfo=FUSO_BRASIL)
        horarios_datetime.append(horario_dt)

    for h in horarios_datetime:
        if h > agora:
            return h

    proximo = horarios_datetime[0] + datetime.timedelta(days=1)
    print(f"[SCHEDULER] Próximo horário será amanhã às {proximo.strftime('%H:%M')}")
    return proximo
