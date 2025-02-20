from datetime import datetime, timedelta

# Hora atual
hora_atual = datetime.now()

# Subtrai 17 horas da hora atual
hora_17_atras = hora_atual - timedelta(hours=15)

# Exibe o horário de 17 horas atrás
print(f"A hora de 17 horas atrás foi: {hora_17_atras.strftime('%H:%M:%S')}")
