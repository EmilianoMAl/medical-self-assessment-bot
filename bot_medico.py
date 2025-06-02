#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot de Autoevaluación Médica Básica
====================================
Este programa es un chatbot simple para realizar una autoevaluación médica básica.

IMPORTANTE: Este bot NO sustituye el consejo médico profesional.
Siempre consulte con un médico para diagnósticos y tratamientos apropiados.
"""


def mostrar_bienvenida():
    """
    Muestra el mensaje de bienvenida y advertencia médica
    """
    print("=" * 60)
    print("🏥 BOT DE AUTOEVALUACIÓN MÉDICA BÁSICA 🏥")
    print("=" * 60)
    print()
    print("⚠️  ADVERTENCIA IMPORTANTE ⚠️")
    print("Este bot NO sustituye el consejo médico profesional.")
    print("La información proporcionada es solo orientativa.")
    print("Siempre consulte con un médico para diagnósticos precisos.")
    print()
    print("¡Hola! Soy tu asistente de autoevaluación médica.")
    print("Te haré algunas preguntas sobre tus síntomas para darte")
    print("una orientación general sobre tu condición.")
    print()


def obtener_respuesta_si_no(pregunta):
    """
    Obtiene una respuesta sí/no del usuario

    Args:
        pregunta (str): La pregunta a realizar

    Returns:
        bool: True si la respuesta es sí, False si es no
    """
    while True:
        respuesta = input(f"{pregunta} (sí/no): ").lower().strip()
        if respuesta in ['sí', 'si', 's', 'yes', 'y']:
            return True
        elif respuesta in ['no', 'n']:
            return False
        else:
            print("Por favor, responde 'sí' o 'no'.")


def obtener_intensidad_sintoma(sintoma):
    """
    Obtiene la intensidad de un síntoma

    Args:
        sintoma (str): El síntoma a evaluar

    Returns:
        str: 'leve', 'moderado' o 'severo'
    """
    while True:
        print(f"\n¿Cómo calificarías la intensidad de tu {sintoma}?")
        print("1. Leve")
        print("2. Moderado")
        print("3. Severo")

        respuesta = input("Selecciona una opción (1-3): ").strip()

        if respuesta == '1':
            return 'leve'
        elif respuesta == '2':
            return 'moderado'
        elif respuesta == '3':
            return 'severo'
        else:
            print("Por favor, selecciona una opción válida (1-3).")


def evaluar_sintomas_respiratorios():
    """
    Evalúa síntomas respiratorios y proporciona recomendaciones

    Returns:
        str: Recomendación médica basada en los síntomas
    """
    print("\n--- EVALUACIÓN DE SÍNTOMAS RESPIRATORIOS ---")

    # Preguntas sobre síntomas respiratorios
    tiene_fiebre = obtener_respuesta_si_no("¿Tienes fiebre?")
    tiene_tos = obtener_respuesta_si_no("¿Tienes tos?")
    tiene_dolor_garganta = obtener_respuesta_si_no(
        "¿Tienes dolor de garganta?")
    tiene_congestion = obtener_respuesta_si_no("¿Tienes congestión nasal?")
    tiene_dificultad_respirar = obtener_respuesta_si_no(
        "¿Tienes dificultad para respirar?")

    # Evaluación de intensidad si hay síntomas severos
    intensidad_fiebre = None
    intensidad_tos = None
    intensidad_dificultad = None

    if tiene_fiebre:
        intensidad_fiebre = obtener_intensidad_sintoma("fiebre")

    if tiene_tos:
        intensidad_tos = obtener_intensidad_sintoma("tos")

    if tiene_dificultad_respirar:
        intensidad_dificultad = obtener_intensidad_sintoma(
            "dificultad respiratoria")

    # Análisis y recomendaciones
    sintomas_severos = 0
    sintomas_moderados = 0

    if intensidad_fiebre == 'severo' or intensidad_tos == 'severo' or intensidad_dificultad == 'severo':
        sintomas_severos += 1

    if tiene_dificultad_respirar:
        return ("🚨 ATENCIÓN URGENTE: La dificultad respiratoria puede ser un síntoma grave. "
                "Te recomiendo que busques atención médica INMEDIATA.")

    if intensidad_fiebre == 'severo':
        return ("⚠️ Fiebre alta detectada. Es recomendable que consultes con un médico "
                "lo antes posible, especialmente si la fiebre persiste por más de 2 días.")

    if tiene_fiebre and tiene_tos and tiene_dolor_garganta:
        return ("Podrías tener una infección respiratoria viral o bacteriana. "
                "Recomendaciones: descanso, hidratación abundante y consultar médico "
                "si los síntomas empeoran o no mejoran en 3-5 días.")

    if tiene_tos and tiene_congestion:
        return ("Posible resfriado común. Recomendaciones: descanso, líquidos calientes, "
                "y vaporizaciones. Consulta médico si persiste más de una semana.")

    if tiene_dolor_garganta:
        return ("Dolor de garganta leve. Puede ser viral. Recomendaciones: gárgaras "
                "con agua tibia y sal, hidratación. Consulta médico si empeora.")

    return ("Síntomas respiratorios leves. Mantén reposo e hidratación. "
            "Consulta médico si los síntomas persisten o empeoran.")


def evaluar_sintomas_digestivos():
    """
    Evalúa síntomas digestivos y proporciona recomendaciones

    Returns:
        str: Recomendación médica basada en los síntomas
    """
    print("\n--- EVALUACIÓN DE SÍNTOMAS DIGESTIVOS ---")

    tiene_nauseas = obtener_respuesta_si_no("¿Tienes náuseas?")
    tiene_vomito = obtener_respuesta_si_no("¿Has vomitado?")
    tiene_diarrea = obtener_respuesta_si_no("¿Tienes diarrea?")
    tiene_dolor_abdominal = obtener_respuesta_si_no("¿Tienes dolor abdominal?")
    tiene_fiebre = obtener_respuesta_si_no("¿Tienes fiebre?")

    intensidad_dolor = None
    if tiene_dolor_abdominal:
        intensidad_dolor = obtener_intensidad_sintoma("dolor abdominal")

    if intensidad_dolor == 'severo':
        return ("🚨 ATENCIÓN: Dolor abdominal severo puede indicar una condición grave. "
                "Busca atención médica INMEDIATA.")

    if tiene_vomito and tiene_diarrea and tiene_fiebre:
        return ("Posible gastroenteritis o intoxicación alimentaria. "
                "Recomendaciones: hidratación constante, dieta blanda, reposo. "
                "CONSULTA MÉDICO si hay signos de deshidratación.")

    if tiene_diarrea and tiene_nauseas:
        return ("Posible malestar gastrointestinal. Recomendaciones: hidratación, "
                "dieta blanda (arroz, pollo hervido, plátano). Consulta médico "
                "si persiste más de 2 días.")

    if tiene_dolor_abdominal and intensidad_dolor == 'moderado':
        return ("Dolor abdominal moderado. Evita alimentos irritantes. "
                "Si persiste o empeora, consulta médico.")

    return ("Síntomas digestivos leves. Mantén hidratación y dieta suave. "
            "Consulta médico si los síntomas persisten.")


def evaluar_sintomas_generales():
    """
    Evalúa síntomas generales como dolor de cabeza, fatiga, etc.

    Returns:
        str: Recomendación médica basada en los síntomas
    """
    print("\n--- EVALUACIÓN DE SÍNTOMAS GENERALES ---")

    tiene_dolor_cabeza = obtener_respuesta_si_no("¿Tienes dolor de cabeza?")
    tiene_fatiga = obtener_respuesta_si_no("¿Te sientes muy cansado/fatigado?")
    tiene_dolor_muscular = obtener_respuesta_si_no(
        "¿Tienes dolores musculares?")
    tiene_mareos = obtener_respuesta_si_no("¿Tienes mareos?")

    intensidad_dolor_cabeza = None
    if tiene_dolor_cabeza:
        intensidad_dolor_cabeza = obtener_intensidad_sintoma("dolor de cabeza")

    if intensidad_dolor_cabeza == 'severo':
        return ("⚠️ Dolor de cabeza severo puede requerir atención médica. "
                "Consulta médico, especialmente si es inusual para ti.")

    if tiene_dolor_cabeza and tiene_fatiga and tiene_dolor_muscular:
        return ("Síntomas compatibles con estrés, tensión o inicio de proceso viral. "
                "Recomendaciones: descanso, hidratación, relajación. "
                "Consulta médico si persiste más de 3 días.")

    if tiene_mareos:
        return ("Los mareos pueden tener múltiples causas. Evita movimientos bruscos, "
                "mantén hidratación. Consulta médico si persisten o empeoran.")

    if tiene_fatiga:
        return ("Fatiga puede deberse a estrés, falta de sueño o múltiples causas. "
                "Asegúrate de descansar bien. Consulta médico si persiste sin causa clara.")

    return ("Síntomas generales leves. Mantén buenos hábitos de descanso e hidratación. "
            "Consulta médico si los síntomas interfieren con tu vida diaria.")


def seleccionar_categoria_sintomas():
    """
    Permite al usuario seleccionar la categoría de síntomas que tiene

    Returns:
        str: La categoría seleccionada
    """
    print("\n¿Qué tipo de síntomas tienes principalmente?")
    print("1. Síntomas respiratorios (tos, fiebre, dolor de garganta, etc.)")
    print("2. Síntomas digestivos (náuseas, vómito, diarrea, dolor abdominal)")
    print("3. Síntomas generales (dolor de cabeza, fatiga, mareos, dolores musculares)")

    while True:
        opcion = input("\nSelecciona una opción (1-3): ").strip()

        if opcion == '1':
            return 'respiratorios'
        elif opcion == '2':
            return 'digestivos'
        elif opcion == '3':
            return 'generales'
        else:
            print("Por favor, selecciona una opción válida (1-3).")


def mostrar_recomendaciones_generales():
    """
    Muestra recomendaciones generales de salud
    """
    print("\n" + "=" * 50)
    print("📋 RECOMENDACIONES GENERALES DE SALUD")
    print("=" * 50)
    print("• Mantén una hidratación adecuada")
    print("• Descansa lo suficiente")
    print("• Mantén una alimentación balanceada")
    print("• Practica ejercicio regularmente")
    print("• Evita el estrés excesivo")
    print("• Consulta médico ante dudas o síntomas persistentes")


def main():
    """
    Función principal del bot de autoevaluación médica
    """
    # Mostrar bienvenida y advertencia
    mostrar_bienvenida()

    # Preguntar si el usuario quiere continuar
    if not obtener_respuesta_si_no("¿Deseas realizar una autoevaluación médica básica?"):
        print("\n¡Gracias por usar el bot! Cuídate y mantente saludable. 👋")
        return

    # Seleccionar categoría de síntomas
    categoria = seleccionar_categoria_sintomas()

    # Evaluar según la categoría seleccionada
    recomendacion = ""  # Inicializar la variable
    if categoria == 'respiratorios':
        recomendacion = evaluar_sintomas_respiratorios()
    elif categoria == 'digestivos':
        recomendacion = evaluar_sintomas_digestivos()
    elif categoria == 'generales':
        recomendacion = evaluar_sintomas_generales()
    else:
        recomendacion = "Error: Categoría no reconocida. Por favor, reinicia el programa."

    # Mostrar resultados
    print("\n" + "=" * 60)
    print("📋 RESULTADO DE LA EVALUACIÓN")
    print("=" * 60)
    print(f"\n{recomendacion}")
    print("\n⚠️  RECORDATORIO IMPORTANTE:")
    print("Esta evaluación es solo orientativa y NO sustituye")
    print("el consejo médico profesional. Ante cualquier duda,")
    print("consulta con un médico calificado.")

    # Mostrar recomendaciones generales
    mostrar_recomendaciones_generales()

    # Preguntar si quiere hacer otra evaluación
    print("\n" + "=" * 60)
    if obtener_respuesta_si_no("¿Deseas realizar otra evaluación?"):
        print("\n" + "="*60)
        main()  # Llamada recursiva para nueva evaluación
    else:
        print("\n¡Gracias por usar el bot de autoevaluación médica!")
        print("¡Que te mejores pronto! 🏥💙")
        print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n¡Gracias por usar el bot! ¡Cuídate! 👋")
    except Exception as e:
        print(f"\n❌ Ha ocurrido un error inesperado: {e}")
        print("Por favor, reinicia el programa.")
