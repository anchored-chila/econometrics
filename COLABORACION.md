# Trabajar juntos en EconoMetrics

Repositorio compartido: https://github.com/anchored-chila/econometrics

## Preparar cada PC

1. Instalar Git o GitHub Desktop e iniciar sesión en GitHub.
2. El propietario debe dar acceso al amigo desde el repositorio, en Settings > Collaborators. El amigo debe aceptar la invitación.
3. En esta PC el proyecto ya está conectado al repositorio. En la PC del amigo, usar Clone repository en GitHub Desktop o:

```powershell
git clone https://github.com/anchored-chila/econometrics.git
cd econometrics
```

4. Configurar en cada PC su propio nombre y correo para los commits:

```powershell
git config user.name "Tu nombre"
git config user.email "Tu correo de GitHub o correo noreply"
git config pull.ff only
```

5. En Windows ejecutar `iniciar.bat`. En Linux ejecutar `bash run.sh` desde la carpeta del proyecto (Python 3.10+; en Debian/Ubuntu instalar `python3-venv`). Abrir http://127.0.0.1:8000. Cada PC tendrá su propio entorno Python y su propia clave de Gemini.

### Flujo del compañero en Linux usando Git

```bash
git clone https://github.com/anchored-chila/econometrics.git
cd econometrics
git config user.name "mixiotes12"
git config user.email "SU_CORREO_VERIFICADO_O_NOREPLY"
git config pull.ff only
bash run.sh
```

Para editar, usar otra terminal en la misma carpeta. Antes de comenzar: `git pull --ff-only`. Después de editar: `git status`, `git add` con los archivos modificados, `git commit -m "Descripcion"` y `git push`. GitHub puede solicitar autenticación al publicar; el nombre y correo de autor no inician sesión.

El usuario de Windows puede usar GitHub Desktop y el de Linux los comandos Git: ambos comparten las mismas ramas y commits. Para trabajo simultáneo, usar una rama por tarea como se explica abajo.

## Compartir cambios

Un commit se guarda localmente. Para compartirlo hay que hacer Push; la otra persona debe hacer Fetch y Pull. Los cambios no aparecen al escribir ni por hacer únicamente Commit.

En GitHub Desktop:

1. Antes de editar, pulsar Fetch origin y luego Pull origin si hay cambios.
2. Editar y probar el programa.
3. Revisar Changed files, escribir un resumen y pulsar Commit to main.
4. Pulsar Push origin.
5. El compañero pulsa Fetch origin y Pull origin, y recarga el navegador.

Equivalente en terminal, revisando los archivos antes de añadirlos:

```powershell
git pull --ff-only
git status
git add app README.md COLABORACION.md .gitignore .gitattributes
git diff --cached
git commit -m "Describe el cambio realizado"
git push origin main
```

## Cuando ambos trabajan al mismo tiempo

Para cambios independientes conviene crear una rama por tarea desde main actualizado:

```powershell
git switch main
git pull --ff-only
git switch -c mejora-maquinaria
# Editar, revisar, añadir archivos y hacer commit
git push -u origin mejora-maquinaria
```

Crear un Pull Request en GitHub para integrar la rama en main. Después de integrarlo, ambos vuelven a main y descargan los cambios. Para revisar una rama del compañero antes de integrarla, hacer Fetch origin y seleccionarla en GitHub Desktop.

Si los dos publican en main y Git rechaza el Push, guardar primero los cambios locales en un commit y ejecutar:

```powershell
git fetch origin
git merge origin/main
```

Si aparecen conflictos, revisar los archivos indicados y conservar las modificaciones necesarias de ambos. Después añadir los archivos resueltos, hacer commit y push. Para cancelar la integración usar `git merge --abort`. No usar force push para sobrescribir el trabajo del otro.

## Qué se comparte

Se comparte el código y su historial. Los proyectos guardados en localStorage, las claves de API y las modificaciones aún no publicadas no se sincronizan entre PCs. Los archivos .env y los entornos virtuales quedan excluidos. Nunca añadir claves al código.
