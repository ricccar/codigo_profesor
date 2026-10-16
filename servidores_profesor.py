
# Monitor de servidores
servidores = {
    # health es encendido o apagado
    "web-1": {"cpu": 40, "ram": 800, "health": True},
    "web-2": {"cpu": 85, "ram": 2000, "health": False},
    "db-1": {"cpu": 99, "ram": 80, "health": True},
    "db-2": {"cpu": 20, "ram": 10000, "health": False},
    "web-3": {"cpu": 5, "ram": 512, "health": False},
    "front-1": {"cpu": 97, "ram": 2048, "health": True},
}
# Detectar:
#   CPU superior a 80%  |  RAM menos de 512  |  Criticos estan encendidos y cumplen ambas
servidores_criticos = []
for servidor, valores_servidor in servidores.items():
    cpu_alta = 80
    memoria_baja = 512
    estado_servidor = 0  # 1 esta mal, 2 esta critico
    if valores_servidor["cpu"] >= cpu_alta:
        estado_servidor += 1
    if valores_servidor["ram"] <= memoria_baja:
        estado_servidor += 1
    if valores_servidor["health"]:
        if estado_servidor <= 0:
            print(f"El servidor {servidor} esta estable")
        elif estado_servidor == 1:
            print(f"El servidor {servidor} esta en mal estado")
        elif estado_servidor == 2:
            servidores_criticos.append(servidor)
            print(f"El servidor {servidor} esta en estado critico!")
    else:
        print(f"El servidor {servidor} esta apagado")
print("-" * 20)  # separador en el menu
print(
    f"Tenemos {len(servidores_criticos)} servidores criticos, que son {servidores_criticos}")
