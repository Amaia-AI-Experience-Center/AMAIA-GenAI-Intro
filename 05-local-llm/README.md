# 🚀 Ejecutar un LLM Local con Ollama y TinyLlama

Esta guía te permitirá ejecutar un modelo de lenguaje local usando Ollama y TinyLlama en tu entorno de desarrollo.

## 📋 ¿Qué es Ollama?

**Ollama** es una plataforma de código abierto que permite ejecutar modelos de lenguaje de gran tamaño localmente en tu máquina. Ofrece:

- 🔒 **Privacidad total**: Tus datos nunca salen de tu máquina
- ⚡ **Rendimiento**: Ejecución local sin latencia de red
- 🛠️ **Fácil instalación**: Un solo comando para instalar
- 🎯 **Múltiples modelos**: Soporte para diversos modelos de lenguaje

## 🧠 ¿Qué es TinyLlama?

**TinyLlama** es un modelo de lenguaje compacto con **1.1 mil millones de parámetros**, diseñado para ser:

- 📦 **Ligero**: Solo ~1GB de tamaño
- ⚡ **Rápido**: Optimizado para entornos con recursos limitados
- 🎯 **Eficiente**: Ideal para desarrollo y pruebas
- 🔧 **Perfecto para Codespaces**: Funciona bien con 4GB de RAM

## 🚀 Instalación y Configuración

### 1️⃣ Instalar Ollama

En tu terminal (Codespace):

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**¿Qué hace este comando?**
- Descarga el script de instalación oficial de Ollama
- Instala Ollama en tu sistema
- Configura las dependencias necesarias

### 2️⃣ Iniciar el Servicio

```bash
ollama serve &
```

**¿Qué hace este comando?**
- Inicia el servicio de Ollama en segundo plano
- El `&` permite que el servicio corra en background
- Habilita la comunicación con los modelos

### 3️⃣ Descargar TinyLlama

```bash
ollama pull tinyllama
```

**¿Qué hace este comando?**
- Descarga el modelo TinyLlama-1.1B (~1GB)
- Lo almacena localmente en tu sistema
- Lo prepara para su uso

### 4️⃣ Ejecutar el Modelo

```bash
ollama run tinyllama
```

**¿Qué hace este comando?**
- Inicia una sesión interactiva con TinyLlama
- Te permite escribir prompts directamente
- El modelo responde en tiempo real

## 💬 Ejemplo de Uso

Una vez ejecutado `ollama run tinyllama`, puedes interactuar así:

```
>>> ¿Qué es un modelo de lenguaje pequeño?

...
```

## 🔧 Comandos Útiles

```bash
# Ver modelos instalados
ollama list

# Detener un modelo
ollama stop tinyllama

# Ver información del modelo
ollama show tinyllama

# Eliminar un modelo
ollama rm tinyllama
```

## 🎯 Ventajas de Usar LLMs Locales

- **🔒 Privacidad**: Tus datos nunca salen de tu máquina
- **⚡ Velocidad**: Sin latencia de red
- **💰 Costo**: Sin costos por API
- **🛠️ Control**: Configuración completa del entorno
- **📚 Aprendizaje**: Entender cómo funcionan los LLMs

## 🚨 Consideraciones

- **Memoria**: TinyLlama requiere ~2GB de RAM
- **Almacenamiento**: El modelo ocupa ~1GB de espacio
- **Rendimiento**: Más lento que modelos en la nube, pero más privado

## 🔗 Recursos Adicionales

- [Ollama Official Website](https://ollama.com)
- [TinyLlama Paper](https://arxiv.org/abs/2401.02385)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)

---

**¡Listo!** 🎉 Ahora tienes tu propio modelo de lenguaje ejecutándose localmente.
