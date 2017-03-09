import sys, os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\LOCAL_TO_PYTHON\\Python35-32\\tcl\\tk8.6"

setup(
    name = "Bookstore",
    version = "1.0",
    description = "Bookstore App.",
    executables = [Executable("frontend.py", base = "Win32GUI")],
    options = {"build_exe": {'include_files': [r"H:\Anaconda3\DLLs\tcl86t.dll", r"H:\Anaconda3\DLLs\tk86t.dll", os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll')]}})


# mport sys, os
#
# os.environ['TCL_LIBRARY'] = "C:\\Users\\(YOUR USERNAME)\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
# os.environ['TK_LIBRARY'] = "C:\\Users\\(YOUR USERNAME)\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"
# from cx_Freeze import setup, Executable
#
# # Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"]}
#
# # GUI applications require a different base on Windows (the default is for a
# # console application).
# base = None
# if sys.platform == "win32":
#     base = "Win32GUI"
# setup(  name = "BookStore",
#         version = "0.1",
#         description = "My BookStore Application",
#         options = {"build_exe": {'include_files': [r"C:\Users\(YOUR USERNAME)\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll", \
#                          r"C:\Users\(YOUR USERNAME)\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll", os.path.join(sys.base_prefix, 'DLLs', 'sqlite3.dll')]}},
