# Cajones es una aplicacion que calcula el listado de partes
# de una cajonera
# unidad de medida en mm

# constantes
hol_lado = 13


# variables
h = 900
a = 600
prof_c = 400

h_c = 120
a_c = 200

hol_sup = 20
hol_inf = 10
hol_int = 40
hol_lateral = 2

esp_lado = 18
esp_sup = 18
esp_inf = 18
esp_c = 15

cubre_der_total = True
cubre_iz_total = True


def calcular_lado_cajon(prof_c, esp_c):
    lado_cajon = prof_c - 2 * esp_c
    return lado_cajon


def calcular_a_c(cubre_iz_total, cubre_der_total, esp_lado, hol_lado, hol_lateral, a):
    if cubre_der_total:
        espesor_derecho = esp_lado
    else:
        espesor_derecho = esp_lado / 2 - hol_lateral

    if cubre_iz_total:
        espesor_izquierdo = esp_lado
    else:
        espesor_izquierdo = esp_lado / 2 - hol_lateral

    ancho_cajon = a - espesor_izquierdo - espesor_derecho - 2 * hol_lateral
    return ancho_cajon


def calcular_h_c(h, esp_sup, esp_inf, hol_sup, hol_int, hol_inf):
    suma_holhura = hol_sup + hol_int + hol_inf
    suma_espesor = esp_sup + esp_inf
    espacio_cajones = h - suma_espesor - suma_holhura
    altura_cajon = espacio_cajones / 3
    return altura_cajon


h_c = calcular_h_c(h, esp_sup, esp_inf, hol_sup, hol_int, hol_inf)
a_c = calcular_a_c(cubre_iz_total, cubre_der_total, esp_lado, hol_lado, hol_lateral, a)
l_c = calcular_lado_cajon(prof_c, esp_c)

print("frente cajon: ", a_c, " X ", round(h_c))
print("lado cajon: ", l_c, " X ", round(h_c))

