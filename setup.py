from cx_Freeze import setup, Executable

includes = ["pythonping", "net_util","cx_Freeze","platform", "subprocess"]
excludes = ["tkinter", "test","unittest", "pydoc","http"]
packages = ["os", "platform", "net_util","concurrent","subprocess","platform"]

# Dependencies are automatically detected, but it might need fine tuning.
# build_exe_options = {"packages": ["os"], "includes": ["pythonping", "net_util"], "excludes": ["tkinter", "test","unittest"],"optimize": 2}

# build_exe_options = {"packages": packages, "includes": includes, "excludes": excludes,"optimize": 2}
# build_exe_options = dict(packages = [], excludes = [])
# build_exe_options = dict(packages = [], excludes = [])

build_exe_options = {"excludes": excludes,"optimize": 2}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
# if sys.platform == "win32":
#     base = "Win32GUI"

exe = Executable(script='test.py', base = base, icon='icons/ping.ico')

setup(name = "myconsole",
        version = "0.1",
        description = "My Console application!",
        options = {"build_exe": build_exe_options},
        executables = [exe])

# setup(name = "myconsole",
#         version = "0.1",
#         description = "My Console application!",
#         options = {"build_exe": build_exe_options},
#         executables = [Executable("test.py", base=base, icon='icons/ping.ico')])