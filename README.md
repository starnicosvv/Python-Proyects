# 📚 Menú de Proyectos en Python

Sistema desarrollado en Python que integra múltiples aplicaciones de consola dentro de un único menú principal.

## 🚀 Descripción

Este proyecto funciona como un **contenedor de aplicaciones**, permitiendo acceder desde un menú principal a diferentes herramientas desarrolladas en Python:

* 🧮 Calculadora
* 📇 Agenda de Contactos
* ✅ TO-DO List
* 💰 Gestor de Gastos Personales

Cada módulo posee su propio menú y funcionalidades independientes.

---

# 📂 Estructura del Proyecto

```text
Proyecto/
│
├── Main.py
├── Calculadora.py
├── Agenda.py
├── TODO_list.py
├── GestorDeGastosPersonales.py
│
├── funciones_gastos.py
├── Utils.py
│
├── movimientos.json
├── log_movimientos.txt
│
└── README.md
```

---

# ⚙️ Requisitos

* Python 3.10 o superior
* Módulos estándar de Python

Verificar instalación:

```bash
python --version
```

---

# ▶️ Ejecución

Ejecutar el archivo principal:

```bash
python Main.py
```

Se mostrará el siguiente menú:

```text
--- Menú de Proyectos ---

1. Calculadora
2. Agenda de contactos
3. TO-DO list
4. Gestor de gastos personales
5. Salir
```

---

# 🧮 Módulo Calculadora

Permite realizar operaciones matemáticas básicas.

### Funcionalidades

* Suma
* Resta
* Multiplicación
* División
* Menú interactivo

---

# 📇 Módulo Agenda de Contactos

Permite administrar una lista de contactos.

### Funcionalidades

* Agregar contacto
* Buscar contacto
* Modificar contacto
* Eliminar contacto
* Listar contactos

---

# ✅ Módulo TO-DO List

Permite gestionar tareas pendientes.

### Funcionalidades

* Crear tareas
* Marcar tareas como completadas
* Eliminar tareas
* Visualizar tareas

---

# 💰 Módulo Gestor de Gastos Personales

Permite registrar y administrar ingresos y gastos personales.

## Funcionalidades

### 1. Agregar movimiento

Registrar:

* Tipo (Ingreso/Gasto)
* Descripción
* Categoría
* Monto
* Fecha

### 2. Buscar movimiento

Búsqueda por:

* Descripción
* Tipo (opcional)

### 3. Eliminar movimiento

Eliminar movimientos registrados.

### 4. Mostrar movimientos

Visualización completa de todos los movimientos almacenados.

### 5. Importar movimientos

Importación desde archivos JSON.

### 6. Exportar movimientos

Exportación de datos a archivos JSON.

### 7. Visualizar log

Consulta del historial de movimientos registrados.

### 8. Persistencia de datos

Los movimientos se almacenan en:

```text
movimientos.json
```

El historial de acciones se registra en:

```text
log_movimientos.txt
```

---

# 💾 Almacenamiento

## movimientos.json

Contiene todos los movimientos financieros registrados.

Ejemplo:

```json
[
    {
        "tipo": "gasto",
        "descripcion": "Supermercado",
        "categoria": "Alimentación",
        "monto": 150000,
        "fecha": "2026-03-28"
    }
]
```

---

# 📝 Registro de Actividades

Cada movimiento agregado queda registrado en:

```text
log_movimientos.txt
```

Esto permite mantener un historial de operaciones realizadas.

---

# 🛠 Tecnologías Utilizadas

* Python 3
* JSON para persistencia de datos
* Programación modular
* Manejo de archivos
* Menús interactivos por consola

---

# 🎯 Objetivos del Proyecto

* Practicar programación modular.
* Aplicar separación de responsabilidades.
* Implementar persistencia de datos mediante JSON.
* Desarrollar aplicaciones CRUD en consola.
* Integrar múltiples proyectos en una sola aplicación.

---

# 👨‍💻 Autor

Desarrollado como proyecto académico y de práctica para fortalecer conocimientos en:

* Python
* Estructuras de datos
* Manejo de archivos
* Programación modular
* Desarrollo de aplicaciones de consola

---

# 📄 Licencia

Proyecto de uso educativo y académico.
