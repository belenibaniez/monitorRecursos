import psutil
from datetime import datetime

def generarInforme():
    cpuCount = psutil.cpu_count () #cpu logicos
    print(cpuCount)
    


def run():
    while True:
        print(psutil.cpu_percent(interval=1, percpu=True))

        



#cpulogical = psutil.cpu_count (lógico = "Falso") # núcleo físico de la CPUç
#print ('núcleo físico de la CPU:', cpulogical)


cpuTimes = psutil.cpu_times()
#print ('usuario de CPU / sistema / tiempo de inactividad:', cpuTimes)

#print(psutil.cpu_percent())
#print(psutil.virtual_memory())


#print(dict(psutil.virtual_memory()._asdict()))


if __name__=="__main__":
    run()