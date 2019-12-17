import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("buscas.py", base=base)
]

buildOptions = dict(
        packages = ['PIL'],
        includes = [],
        include_files = ['favicon.png', 'GifMaker/font.ttf', 'GifMaker/ImagemTabuleiro.png'],
        excludes = []
)

setup(
    name = "Buscas",
    version = "1.0",
    description = "Buscas cegas e heurísticas. By Alfredo Albélis, Pedro Bernini",
    options = dict(build_exe = buildOptions),
    executables = executables
 )