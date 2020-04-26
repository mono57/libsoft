from cx_Freeze import setup, Executable


base = None    

executables = [Executable("start_app.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}
# On appelle la fonction setup
setup(
    name = "Libsoft",
    version = "0.1",
    description = "Programme de gestion de la librairie",
    executables = executables,
)
#C:\python34\python.exe setup.py build  // commande pour executer le script
#python setup.py build