#!/usr/bin/python3
from cx_Freeze import setup, Executable

setup(name = 'rpc',
      version = '0.1',
      description = 'rpc game',
      executables = [Executable("new.py")]
    )



#then, in command line type "python3 python_to_exe_example_on_rpc_game.py build"
