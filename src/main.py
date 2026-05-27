import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl

print("=== SISTEMA DIFUSO - SATISFACCIÓN TRANSPORTE CUBA ===")
print("Autores: David Sarmiento & Abdiel Anaya")

# Variables de entrada
tiempo_espera = ctrl.Antecedent(np.arange(0, 121, 1), 'tiempo_espera')
comodidad = ctrl.Antecedent(np.arange(0, 11, 1), 'comodidad')
disponibilidad = ctrl.Antecedent(np.arange(0, 11, 1), 'disponibilidad')

# Variable de salida
satisfaccion = ctrl.Consequent(np.arange(0, 11, 0.1), 'satisfaccion')

# Funciones de pertenencia
tiempo_espera['corto'] = fuzz.trimf(tiempo_espera.universe, [0, 0, 40])
tiempo_espera['moderado'] = fuzz.trimf(tiempo_espera.universe, [20, 50, 80])
tiempo_espera['largo'] = fuzz.trimf(tiempo_espera.universe, [60, 120, 120])

comodidad['baja'] = fuzz.trimf(comodidad.universe, [0, 0, 5])
comodidad['media'] = fuzz.trimf(comodidad.universe, [2, 5, 8])
comodidad['alta'] = fuzz.trimf(comodidad.universe, [6, 10, 10])

disponibilidad['insuficiente'] = fuzz.trimf(disponibilidad.universe, [0, 0, 4])
disponibilidad['regular'] = fuzz.trimf(disponibilidad.universe, [2, 5, 8])
disponibilidad['alta'] = fuzz.trimf(disponibilidad.universe, [6, 10, 10])

satisfaccion['baja'] = fuzz.trimf(satisfaccion.universe, [0, 0, 4])
satisfaccion['media'] = fuzz.trimf(satisfaccion.universe, [3, 5, 7])
satisfaccion['alta'] = fuzz.trimf(satisfaccion.universe, [6, 10, 10])

# Reglas
r1 = ctrl.Rule(tiempo_espera['largo'] & comodidad['baja'], satisfaccion['baja'])
r2 = ctrl.Rule(tiempo_espera['corto'] & disponibilidad['alta'], satisfaccion['alta'])
r3 = ctrl.Rule(tiempo_espera['moderado'] & comodidad['media'], satisfaccion['media'])
r4 = ctrl.Rule(disponibilidad['insuficiente'] & comodidad['baja'], satisfaccion['baja'])
r5 = ctrl.Rule(tiempo_espera['corto'] & comodidad['alta'], satisfaccion['alta'])
r6 = ctrl.Rule(tiempo_espera['moderado'] & disponibilidad['regular'], satisfaccion['media'])

# Sistema
sistema = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6])
simulador = ctrl.ControlSystemSimulation(sistema)

# Entrada manual
e = float(input("Tiempo de espera (minutos 0-120): "))
c = float(input("Comodidad (0-10): "))
d = float(input("Disponibilidad (0-10): "))

simulador.input['tiempo_espera'] = e
simulador.input['comodidad'] = c
simulador.input['disponibilidad'] = d
simulador.compute()

print(f"\n SATISFACCIÓN: {simulador.output['satisfaccion']:.2f} / 10")
