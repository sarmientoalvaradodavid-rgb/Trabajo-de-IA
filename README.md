# Trabajo-de-IA
# 🚌 Lógica Difusa para Satisfacción del Transporte en Cuba

**Autores:** David Sarmiento & Abdiel Anaya  
**Materia:** Inteligencia Artificial II  
**Universidad de Oriente**

## Descripción del Problema
En Cuba, la percepción de la calidad del transporte público (ómnibus) es subjetiva. Un tiempo de espera de 30 minutos puede ser "poco" para unos y "mucho" para otros.

Este sistema usa **Lógica Difusa** para estimar la Satisfacción del Ciudadano (0 a 10) basado en:
- ⏱️ Tiempo de espera (0-120 min)
- 🪑 Comodidad (0-10)
- 🚏 Disponibilidad (0-10)

## Tecnologías Usadas
- Python 3.x
- scikit-fuzzy
- numpy
- matplotlib

## Cómo ejecutar
1. Clona el repositorio
2. Instala dependencias: `pip install -r requirements.txt`
3. Corre el programa: `python src/main.py`

## Estructura del Proyecto
/fuzzy-logic-transporte
│
├── src/               # Código fuente (lógica difusa)
├── data/              # Datos de ejemplo (CSV)
├── docs/              # Pre-artículo (PDF)
├── presentacion/      # Diapositivas (PPTX)
└── video/             # Demo funcional (MP4)

## Declaración de Uso de IA
Se utilizó ChatGPT como herramienta de apoyo para la estructuración del código y el pre-artículo. Todo el contenido fue validado y adaptado al contexto cubano por los autores.
