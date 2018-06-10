import os,sys,socket

# python createLink local name remoteName
computerName = socket.gethostname()
# userAdmin = "raul1"
pathRemoteServer = r"\\192.168.56.123\html"
localCreateLink =r"C:\Users\raul1\projetosPHP"
localName = sys.argv[1]
remoteName = sys.argv[2]
os.system(r'''mklink /d "%s\%s" "%s\%s"'''%(localCreateLink,localName,pathRemoteServer,remoteName))
