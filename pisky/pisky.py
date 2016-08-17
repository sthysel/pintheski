import bobo
import socket
import psutil
import pprint

@bobo.query('/')
def isgood():
    hostname = socket.gethostname()
    return "{} is online".format(hostname)

@bobo.query('/ps')
def processes():
    procs = [str(proc) for proc in psutil.process_iter()]
    proc_str = " ".join(procs)
    return proc_str

