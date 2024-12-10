def es_contraseña_segura(contraseña):
    # Comprobar que la contraseña empieza y termina por una letra mayúscula
    empieza_termina_mayuscula = contraseña[0].isupper() and contraseña[-1].isupper()

    # Comprobar que la contraseña contiene al menos un valor numérico
    contiene_numero = any(char.isdigit() for char in contraseña)

    # Comprobar que la contraseña contiene alguno de los símbolos (punto, guión bajo, hashtag)
    contiene_simbolo = any(char in '._#' for char in contraseña)

    # Devolver True si cumple todas las condiciones, False en caso contrario
    return empieza_termina_mayuscula and contiene_numero and contiene_simbolo


# Ejemplo de uso
contraseña = "AsecurePassword1#P"
es_segura = es_contraseña_segura(contraseña)
print(f"La contraseña '{contraseña}' es segura: {es_segura}")
