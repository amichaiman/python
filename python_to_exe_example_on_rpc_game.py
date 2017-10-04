#!/usr/bin/python3
from cx_Freeze import setup, Executable

setup(name = 'rpc',
      version = '0.1',
      description = 'rpc game',
      executables = [Executable("new.py")]
    )
