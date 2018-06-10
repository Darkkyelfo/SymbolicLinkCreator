import os, sys, socket

# python createLink local name remoteName
computerName = socket.gethostname()
# userAdmin = "raul1"
pathRemoteServer = r"\\192.168.56.123\html"
localCreateLink = r"C:\Users\raul1\projetosPHP"
localName = sys.argv[1]
fullLocalPath = localCreateLink + "\\" + localName + "_local"
# Caso só receba um argumento esse argumento deve ser de mesmo nome do arquivo remoto
try:
    remoteName = sys.argv[2]
except IndexError:
    remoteName = localName
os.system(r'''mkdir %s''' % fullLocalPath)
os.system(r'''mklink /d "%s\%s" "%s\%s"''' % (fullLocalPath, localName, pathRemoteServer, remoteName))
