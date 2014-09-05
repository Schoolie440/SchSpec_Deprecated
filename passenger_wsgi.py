import sys, os
virt_binary = "/home/schoolcr/pyenv/bin/python"
if sys.executable != virt_binary: os.execl(virt_binary, virt_binary, *sys.argv)
sys.path.append(os.getcwd())
from app import app as application
