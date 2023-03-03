import pyvisa

rm = pyvisa.ResourceManager()
inst = None

def list_ports():
    print(rm.list_resources())


def connect(port):
    global inst
    inst = rm.open_resource(port)
    inst.write_termination = '\r\n'
    inst.read_termination = '\n'

def get_id():
    print(inst.query("*IDN?"))

def set_voltage(channel, voltage):
    send_string = ("VSET{},{}".format(channel, voltage))
    print(send_string)
    inst.query(send_string)


def set_voltage_all(voltage):
    send_string = ""
    for i in range(1,5):
        send_string += "VSET{},{};".format(i, voltage)
    print(send_string)
    inst.query(send_string)


def set_current(channel, current):
    send_string = ("ISET{},{}".format(channel, current))
    print(send_string)
    inst.query(send_string)

def set_current_all(current):
    send_string = ""
    for i in range(1,5):
        send_string += "ISET{},{};".format(i, current)
    print(send_string)
    inst.query(send_string)

def set_status(channel, status ):
    send_string = "OUT{},{}".format(channel, int(status))
    print(send_string)
    inst.query(send_string)

def set_status_all(status):
    send_string = ""
    for i in range(1,5):
        send_string += "OUT{},{};".format(i, int(status))
    print(send_string)
    inst.query(send_string)





