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

#python setup.py build  // commande pour executer le script