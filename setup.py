import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("buscas.py", base = base, icon = "icon.ico")
]

buildOptions = dict(
    packages = ['PIL'],
    includes = [],
    include_files = [
        'favicon.png',
        ('Cats', 'Cats'),
        ('GifMaker', 'GifMaker'),
        ('Gifs', 'Gifs'),
        ('Logs', 'Logs')
    ],
    excludes = []
)

setup(
    name = "Buscas",
    version = "1.0",
    description = "Buscas cegas e heurísticas. By Alfredo Albélis, Pedro Bernini",
    options = dict(build_exe = buildOptions),
    executables = executables
)
