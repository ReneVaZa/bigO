def limpiar_feed(publicaciones: list) -> list:
    if len(publicaciones) <= 1:
        return publicaciones
    
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    if not depositos:
        return 0.0
    
    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    saldo_nuevo = (saldo_anterior + depositos[-1]) * (1 + tasa_interes)
    
    return saldo_nuevo

def maxima_profundidad(comentarios: list) -> int:
    if not comentarios:
        return 0
    
    profundidades = []
    
    for elem in comentarios:
        if isinstance(elem, list):
            profundidades.append(1 + maxima_profundidad(elem))
        else:
            profundidades.append(1)
            
    return max(profundidades)


if __name__ == "__main__":
    feed = ["Post A", "Post B", "Post B", "Post C", "Post B"]
    print("RESULTADO 1:", limpiar_feed(feed))

    depositos = [1000, 2000, 1500]
    tasa = 0.05
    resultado_saldo = calcular_saldo_final(depositos, tasa)
    print(f"RESULTADO 2: {resultado_saldo:.2f}")

    hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
    print("RESULTADO 3:", maxima_profundidad(hilo))
