import pandas as pd
from pyModbusTCP.client import ModbusClient

# Configurações do cliente Modbus
server_ip = "127.0.0.1"  # Endereço IP do servidor Modbus
server_port = 502  # Porta do servidor Modbus

# Conecta ao servidor Modbus
client = ModbusClient(host=server_ip, port=server_port)

# Verifica se a conexão foi estabelecida
if not client.open():
    print("Erro ao conectar ao servidor Modbus")
    exit()

# Carrega os dados do arquivo .xlsx
df = pd.read_excel('test_variables.xlsx')

# Itera sobre as linhas do arquivo .xlsx
for index, row in df.iterrows():
    address = int(row['Address'])
    value = float(row['Value'])

    # Lê o valor do servidor Modbus
    read_value = client.read_holding_registers(address, 1)

    # Verifica se a leitura foi bem-sucedida
    if read_value:
        # Obtém o valor lido
        read_value = read_value[0]

        # Imprime o valor lido
        print(f"Variável {address}: {read_value}")
    else:
        print(f"Falha ao ler a variável {address}")

# Fecha a conexão com o servidor Modbus
client.close()
