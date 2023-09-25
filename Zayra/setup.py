from cx_Freeze import setup, Executable

executables = [Executable("Zayra.py")]

setup(
    name="Zayra",
    version="1.0",
    description="Assistente virtual",
    executables=executables
)
