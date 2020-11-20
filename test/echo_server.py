from src.beHacked import network

n = network(("127.0.0.1",59487))
n.send(b"hi"*2050)
#n.close()
