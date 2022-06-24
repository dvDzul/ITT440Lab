from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.107',  #Your Server IP
    'username': 'dzul', #your Server Username
    'password': 'comel12345', #your server password
    'port' : 9898,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
