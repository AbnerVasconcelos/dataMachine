import os
import time
from modbus_server import serversimu

print(os.listdir())

host_ip = "127.0.0.1"  # IP do host
port = 502  # Porta do servidor
variable_table = 'test_variables.xlsx'

servidor_modbus = serversimu(host_ip, port, variable_table)
servidor_modbus.run()

time.sleep(2)  # Aguarda 2 segundos
input("Pressione Enter para sair...")



