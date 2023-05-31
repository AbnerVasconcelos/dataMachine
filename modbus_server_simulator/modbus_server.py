import openpyxl
from pyModbusTCP.server import DataBank, ModbusServer
import random
import time

class serversimu():
    def __init__(self, host_ip, port, xlsx_file):
        self._server = ModbusServer(host=host_ip, port=port, no_block=True)
        self._db = DataBank
        self._xlsx_file = xlsx_file

    def read_variables_from_excel(self):
        wb = openpyxl.load_workbook(self._xlsx_file)
        sheet = wb.active
        first_row = True
        for row in sheet.iter_rows(min_row=2, values_only=True):
            address = int(row[0])
            if first_row:
                # Mantenha o valor original da primeira leitura
                value = int(row[1])
                first_row = False
            else:
                # Atribua um valor aleatório entre 50 e 200 para as leituras subsequentes
                if address >= 48008:
                    value = random.choice([True, False])
                else:
                    value = random.randint(50, 200)
            self._db.set_words(address, [value])
        wb.close()

    def run(self):
        try:
            self._server.start()
            print("Servidor modbus em execução")
            while True:
                self.read_variables_from_excel()
                print("===========================")
                print("Tabela modbus")
                print('Temperature: {} {} {} {} {} {}'.format(
                    self._db.get_words(28001),
                    self._db.get_words(28002),
                    self._db.get_words(28003),
                    self._db.get_words(28004),
                    self._db.get_words(28005),
                    self._db.get_words(28006)
                ))

                time.sleep(5)
        except Exception as e:
            print("Erro: ", e.args)
