# Sistema de autenticacion de usuarios

usuarios = {
    "joaquin": {
        "rol": "admin",
        "permisos": ["lectura", "escritura", "devops", "admin"],
        "activo": True
    },
    "maria": {
        "rol": "devops",
        "permisos": ["lectura", "devops"],
        "activo": True
    },
    "juan": {
        "rol": "developer",
        "permisos": ["lectura", "escritura"],
        "activo": True
    },
    "silvia": {
        "rol": "sales",
        "permisos": ["lectura"],
        "activo": False
    },
}

usuarios["silvia"]["activo"] = True
usuarios.update({"pedro": {"rol": "developer", "permisos": [
                "lectura", "escritura"], "activo": True}})
usuarios["juan"]["activo"] = False

permiso_a_consultar = input("Que permiso quieres consultar?\n")

usuarios_con_permisos = []
for usuario, info in usuarios.items():
    permisos = info["permisos"]
    activo = info["activo"]
    if permiso_a_consultar in permisos and activo:
        usuarios_con_permisos.append(usuario)

print(
    f"Los usuarios con permisos de {permiso_a_consultar} son {len(usuarios_con_permisos)}\n{usuarios_con_permisos}")
