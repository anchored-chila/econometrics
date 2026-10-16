"""Start the development server on Windows, Linux and macOS."""
import os
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent


def main():
    if sys.version_info < (3, 10):
        print("Se necesita Python 3.10 o posterior.", file=sys.stderr)
        return 1

    environment = ROOT / ".venv"
    python = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not python.exists():
        if environment.exists():
            print("La carpeta .venv esta incompleta o pertenece a otro sistema. "
                  "Renombrala y vuelve a iniciar; cada PC necesita su propio entorno.", file=sys.stderr)
            return 1
        print("Creando el entorno de Python de esta PC...", flush=True)
        try:
            venv.EnvBuilder(with_pip=True).create(environment)
        except Exception as exc:
            print(f"No se pudo crear el entorno: {exc}", file=sys.stderr)
            print("En Debian/Ubuntu instala python3-venv. "
                  "Renombra .venv si quedo incompleta y vuelve a intentar.", file=sys.stderr)
            return 1

    try:
        # Run on every start so dependencies added by a collaborator are installed.
        subprocess.run([str(python), "-m", "pip", "install", "-r",
                        str(ROOT / "requirements.txt")], cwd=ROOT, check=True)
        print("Abre http://127.0.0.1:8000 — Ctrl+C para detener.", flush=True)
        return subprocess.call([str(python), "-m", "uvicorn", "app.main:app",
                                "--host", "127.0.0.1", "--port", "8000", "--reload",
                                "--reload-dir", str(ROOT / "app")], cwd=ROOT)
    except subprocess.CalledProcessError as exc:
        print("No se pudieron instalar las dependencias. Revisa la conexion "
              "y el error anterior; puedes volver a ejecutar el inicio.", file=sys.stderr)
        return exc.returncode
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
