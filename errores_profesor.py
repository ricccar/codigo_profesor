logs = ["ERROR", "INFO", "CRITICAL", "WARNING", "ERROR", "ERROR", "INFO"]

# elimino duplicados y hago mi lista de claves  Set no admite duplicados
claves_logs = list(set(logs))
resultado = {}  # hago el diccionario
for clave in claves_logs:
    resultado[clave] = logs.count(clave)  # relleno el diccionario

print(resultado)
