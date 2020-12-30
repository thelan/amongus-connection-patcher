import os
import sys

data_dir = os.path.join(os.path.expandvars('%userprofile%'), 'AppData', 'LocalLow', 'Innersloth', 'Among Us')
print(data_dir)

if not os.path.isdir(data_dir):
  print('failed to find data dir')
  sys.exit(1)

data_file = os.path.join(data_dir, 'regionInfo.dat')

servername = 'mysrv'
ping = '127.0.0.1'
servers = [
        {
                'name': servername,
                'ip': ping,
                'port': 22023,
        }
]

with open(data_file, 'wb') as handle:
  handle.write(bytes([0x00, 0x00, 0x00, 0x00]))

  handle.write(bytes([len(servername)]))
  handle.write(bytes(servername, 'UTF-8'))

  handle.write(bytes([len(ping)]))
  handle.write(bytes(ping, 'UTF-8'))

  # Server length
  handle.write(bytes([len(servers)]))
  for server in servers:
    handle.write(bytes([0x00, 0x00, 0x00]))

    # ServerName
    handle.write(bytes([len(server['name'])]))
    handle.write(bytes(server['name'], 'UTF-8'))

    # Encode IP
    handle.write(bytes(map(int, server['ip'].split('.'))))

    # encode port
    handle.write(server['port'].to_bytes(6, 'little'))

os.system('start steam://rungameid/945360')
