
## 📌 ¿Qué es GitHub?
GitHub es una plataforma de desarrollo colaborativo que permite alojar proyectos utilizando el sistema de control de versiones Git. Facilita la colaboración entre desarrolladores mediante funciones como forks, pull requests y revisiones de código.

---

## 🗃️ ¿Cómo crear un repositorio en GitHub?
1. Inicia sesión en GitHub.
2. Haz clic en el botón `New` o `+` y selecciona `New repository`.
3. Asigna un nombre al repositorio, agrega una descripción opcional.
4. Elige si será público o privado.
5. Haz clic en `Create repository`.

---

## 🌿 ¿Cómo crear una rama en Git?
```bash
git branch nombre-de-la-rama
```

---

## 🔄 ¿Cómo cambiar a una rama en Git?
```bash
git checkout nombre-de-la-rama
```

---

## 🔀 ¿Cómo fusionar ramas en Git?
```bash
git checkout rama-principal
git merge nombre-de-la-rama
```

---

## 💾 ¿Cómo crear un commit en Git?
```bash
git add .
git commit -m "Mensaje del commit"
```

---

## 🚀 ¿Cómo enviar un commit a GitHub?
```bash
git push origin nombre-de-la-rama
```

---

## 🌍 ¿Qué es un repositorio remoto?
Es una versión alojada en línea (por ejemplo en GitHub) de tu repositorio local. Permite compartir y colaborar con otros.

---

## 🔗 ¿Cómo agregar un repositorio remoto a Git?
```bash
git remote add origin URL-del-repositorio
```

---

## ⬆️ ¿Cómo empujar cambios a un repositorio remoto?
```bash
git push origin nombre-de-la-rama
```

---

## ⬇️ ¿Cómo tirar de cambios de un repositorio remoto?
```bash
git pull origin nombre-de-la-rama
```

---

## 🍴 ¿Qué es un fork de repositorio?
Es una copia de un repositorio en tu propia cuenta de GitHub, que puedes modificar libremente sin afectar al original.

---

## 🧪 ¿Cómo crear un fork de un repositorio?
1. Ve al repositorio original en GitHub.
2. Haz clic en el botón `Fork` en la esquina superior derecha.
3. GitHub creará una copia del repositorio en tu cuenta.

---

## 📤 ¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?
1. Haz cambios en tu fork.
2. Haz clic en `Contribute` > `Open pull request`.
3. Escribe una descripción y envía la solicitud.

---

## ✅ ¿Cómo aceptar una solicitud de extracción?
1. En el repositorio original, ve a la pestaña `Pull requests`.
2. Selecciona la solicitud.
3. Revisa los cambios y haz clic en `Merge pull request`.

---

## 🏷️ ¿Qué es una etiqueta en Git?
Es una referencia que apunta a un commit específico, generalmente usada para marcar versiones (`v1.0.0`, etc.).

---

## 🏷️ ¿Cómo crear una etiqueta en Git?
```bash
git tag nombre-etiqueta
```

---

## 🏷️ ¿Cómo enviar una etiqueta a GitHub?
```bash
git push origin nombre-etiqueta
```

---

## 📜 ¿Qué es un historial de Git?
Es el registro completo de todos los commits hechos en el repositorio.

---

## 🔍 ¿Cómo ver el historial de Git?
```bash
git log
```

---

## 🔎 ¿Cómo buscar en el historial de Git?
```bash
git log --grep="palabra-clave"
```

---

## ❌ ¿Cómo borrar el historial de Git?
No se recomienda borrar el historial. Sin embargo, para reescribirlo:
```bash
git rebase -i HEAD~n
# o para eliminar completamente:
rm -rf .git
git init
```
⚠️ **Advertencia:** Esto puede causar pérdida de información y no se debe hacer en repositorios compartidos.

---

## 🔐 ¿Qué es un repositorio privado en GitHub?
Un repositorio que solo es accesible por ti y las personas que invites.

---

## 🛡️ ¿Cómo crear un repositorio privado en GitHub?
1. En la creación del repositorio, selecciona la opción `Private`.
2. Luego haz clic en `Create repository`.

---

## 👥 ¿Cómo invitar a alguien a un repositorio privado en GitHub?
1. Ve a la pestaña `Settings` > `Collaborators`.
2. Agrega el nombre de usuario de la persona.
3. Haz clic en `Invite`.

---

## 🌐 ¿Qué es un repositorio público en GitHub?
Es un repositorio visible y accesible para cualquier persona en internet.

---

## 🌐 ¿Cómo crear un repositorio público en GitHub?
1. En la creación del repositorio, selecciona la opción `Public`.
2. Haz clic en `Create repository`.

---

## 🔗 ¿Cómo compartir un repositorio público en GitHub?
Copia y comparte la URL del repositorio. Por ejemplo:
```
https://github.com/tu-usuario/nombre-del-repositorio
```

---

**📚 Tecnicatura Universitaria en Programación - A Distancia**  
_Materia: Programación I_
