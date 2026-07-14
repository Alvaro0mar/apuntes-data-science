# Guía de flujo de trabajo: VS Code + Conda + Git + GitHub

Esta es tu referencia rápida para cada vez que te sientes a trabajar en tus prácticas de Data Science.

---

## 🔵 Paso 1: Activar tu entorno de conda

Cada vez que abras una terminal nueva en VS Code:

```powershell
conda activate data_science
```

Esto cambia tu terminal de `(base)` a `(data_science)`, el entorno donde tienes instalados numpy y pandas.

**Cómo verificar que estás en el entorno correcto:** mira el inicio de la línea en tu terminal:

```
(data_science) PS C:\Users\ALVARO\Documents\GitHub\apuntes-data-science>
```

Si dice `(data_science)` al inicio, vas bien.

---

## 🟢 Paso 2 (opcional): Verificar que Git está instalado

Solo necesitas hacerlo si algo falla o tienes dudas:

```powershell
git --version
```

Debería mostrarte algo como:

```
git version 2.55.0.windows.2
```

---

## 🟡 Paso 3: Traer los cambios más recientes de GitHub (`git pull`)

**Siempre hazlo primero**, antes de empezar a trabajar, por si editaste algo en la web de GitHub o en otra computadora:

```powershell
cd apuntes-data-science
git pull
```

| Comando | Qué hace |
|---|---|
| `cd apuntes-data-science` | Entra a la carpeta de tu repositorio (sáltalo si ya estás adentro) |
| `git pull` | Trae los cambios nuevos de GitHub a tu computadora |

Si no hay cambios nuevos, verás: `Already up to date.`

---

## 🟠 Paso 4: Trabajar y editar tu código

Edita tus archivos `.py` normalmente en VS Code. No olvides guardar con `Ctrl+S`.

---

## 🔴 Paso 5: Subir tus cambios a GitHub (`add`, `commit`, `push`)

Cuando termines de trabajar, son 3 comandos:

### 1. `git add` — Prepara los cambios
```powershell
git add .
```
El punto `.` significa "todos los archivos que cambié". Es como meter tus cosas en una caja antes de enviarla.

### 2. `git commit` — Guarda una "foto" de esos cambios
```powershell
git commit -m "Agregué ejercicio de operaciones básicas"
```
El mensaje entre comillas describe qué hiciste. Sé breve y claro.

### 3. `git push` — Sube los cambios a GitHub
```powershell
git push
```
Ahora tus cambios aparecerán en la página web de GitHub.

---

## 📋 Resumen del flujo diario completo

```powershell
conda activate data_science      # 1. Activa tu entorno
cd apuntes-data-science          # 2. Entra a tu carpeta de proyecto
git pull                         # 3. Trae cambios recientes

# ... trabajas y editas tu código ...

git add .                        # 4. Prepara tus cambios
git commit -m "mensaje breve"    # 5. Guarda la foto de esos cambios
git push                         # 6. Sube todo a GitHub
```

---

## 🖼️ Analogía para recordarlo

GitHub es como una carpeta compartida en la nube, y Git es el "mensajero" que va y viene.

| Comando | Analogía |
|---|---|
| `git pull` | Trae lo nuevo de la nube a tu compu |
| `git add` | Prepara tu paquete para enviar |
| `git commit` | Le pones una etiqueta/nota al paquete |
| `git push` | Envías el paquete a la nube |

---

## 💡 Alternativa visual (sin escribir comandos)

VS Code tiene todo esto en botones, si prefieres no usar la terminal:

1. Clic en el ícono de rama 🔀 en la barra lateral izquierda
2. Ahí ves los archivos modificados
3. Escribes el mensaje del commit en la cajita de texto
4. Clic en el ✓ (commit) y luego en "Sync Changes" (hace pull y push juntos)

---

## ⚠️ Solución de problemas comunes

### Error: `fatal: not a git repository (or any of the parent directories): .git`

Te sale si ejecutas `git pull` (o `git add`, `git commit`, `git push`) estando **fuera** de la carpeta de tu repositorio. Por ejemplo, si tu terminal muestra:

```
(data_science) PS C:\Users\ALVARO\Documents\GitHub>
```

Fíjate que falta `\apuntes-data-science` al final de la ruta — estás un nivel arriba, en la carpeta contenedora, no dentro del repositorio en sí.

**Solución:** entra a la carpeta del repositorio antes de usar cualquier comando de git:

```powershell
cd apuntes-data-science
```

**Cómo confirmar que ya estás en el lugar correcto:** la ruta en tu terminal debe terminar con el nombre de tu repositorio:

```
(data_science) PS C:\Users\ALVARO\Documents\GitHub\apuntes-data-science>
```

Si ves eso, ya puedes usar `git pull`, `git add`, `git commit` y `git push` sin problema.

---

## 🧪 Ejemplo completo de principio a fin

Supongamos que hoy quieres agregar un ejercicio nuevo llamado `ejercicio_listas.py`.

```powershell
# 1. Activas tu entorno
conda activate data_science

# 2. Entras a tu carpeta de proyecto
cd C:\Users\ALVARO\Documents\GitHub\apuntes-data-science

# 3. Traes cualquier cambio reciente de GitHub
git pull
# Salida esperada: Already up to date.

# 4. Creas y trabajas tu archivo en VS Code
# (escribes tu código en ejercicio_listas.py y guardas con Ctrl+S)
```

Contenido de `ejercicio_listas.py`:
```python
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)
```

Lo corres en la terminal para probar que funciona:
```powershell
python ejercicio_listas.py
```

Salida:
```
manzana
pera
uva
```

Ahora que funciona, lo subes a GitHub:

```powershell
# 5. Preparas el archivo nuevo
git add .

# 6. Guardas la "foto" con un mensaje descriptivo
git commit -m "Agrego ejercicio de listas con bucle for"

# 7. Subes el cambio a GitHub
git push
```

Salida esperada de `git push`:
```
Enumerating objects: 4, done.
...
To https://github.com/tu_usuario/apuntes-data-science.git
   abc1234..def5678  main -> main
```

Con eso, si entras a la página web de tu repositorio en GitHub, ya deberías ver `ejercicio_listas.py` ahí. ✅

---

## ✅ Checklist mental antes de cerrar VS Code

- [ ] ¿Guardé todos mis archivos? (`Ctrl+S`)
- [ ] ¿Hice `git add .`?
- [ ] ¿Hice `git commit -m "..."`?
- [ ] ¿Hice `git push`?

Si los 4 están hechos, tu trabajo de hoy ya quedó respaldado en GitHub.
