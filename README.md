# 🏥 Bot de Autoevaluación Médica Básica

## 📌 Descripción

Este es un chatbot de consola desarrollado en Python que realiza una autoevaluación médica básica. A través de preguntas guiadas sobre síntomas, el bot ofrece recomendaciones generales de salud según la categoría elegida: respiratoria, digestiva o general.

> ⚠️ **Este bot NO sustituye el consejo médico profesional.** La información proporcionada es únicamente orientativa y educativa.

---

## 🧠 Características

- ✅ Interfaz en consola amigable  
- ✅ Preguntas tipo sí/no e intensidad (leve, moderado, severo)  
- ✅ Evaluación según categorías de síntomas:
  - Respiratorios: fiebre, tos, dificultad para respirar, etc.
  - Digestivos: diarrea, náuseas, vómito, dolor abdominal
  - Generales: fatiga, dolor muscular, mareo, dolor de cabeza  
- ✅ Recomendaciones personalizadas  
- ✅ Detección de posibles urgencias médicas  
- ✅ Consejos generales para el bienestar  

---

## 💻 Requisitos

- Python 3.6 o superior  
- No requiere librerías externas

---

## ▶️ Cómo usar

1. Ejecuta el programa:

   ```bash
   python bot_medico.py
   ```

2. Sigue las instrucciones en pantalla:
   - Elige la categoría de síntomas.
   - Responde las preguntas con “sí”, “no”, o selecciona la intensidad cuando se indique.
   - Recibe recomendaciones finales basadas en tus respuestas.

3. Puedes repetir la autoevaluación tantas veces como desees.

---

## ⚙️ Estructura del código

- `mostrar_bienvenida()`: Mensaje inicial y advertencias  
- `obtener_respuesta_si_no()`: Entrada sí/no  
- `obtener_intensidad_sintoma()`: Escala de gravedad  
- `evaluar_sintomas_*()`: Evaluación específica (respiratorios, digestivos, generales)  
- `seleccionar_categoria_sintomas()`: Permite elegir qué síntomas tienes  
- `main()`: Función principal  

---

## 🩺 Ejemplos de uso

### 🔹 Respiratorios
- Detección de posibles infecciones respiratorias
- Alertas ante dificultad respiratoria

### 🔹 Digestivos
- Sospecha de gastroenteritis o malestar estomacal
- Advertencias sobre dolor abdominal severo

### 🔹 Generales
- Fatiga, dolor muscular, estrés
- Posible relación con infecciones virales leves

---

## 🚫 Limitaciones

- No proporciona diagnósticos médicos  
- No reemplaza una consulta médica profesional  
- No detecta todas las condiciones clínicas posibles  

---

## 💙 Nota final

Este proyecto fue creado con fines educativos. Ante cualquier duda de salud, consulta con un profesional médico.

---

## ✍️ Autor

**Emiliano Martínez**  
[GitHub](https://github.com/EmilianoMAl)  
[LinkedIn](https://www.linkedin.com/in/emiliano-martinez-40a6882b7/)
