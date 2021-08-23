from calculo_ipv4 import CalcIPv4


calc = CalcIPv4(ip='192.168.0.2', mascara='255.255.255.0')
print(f'IP: {calc.ip}')
print(f'Máscara: {calc.mascara}')
print(f'Rede: {calc.rede}')
print(f'Broadcast: {calc.broadcast}')
print(f'Prefixo: {calc.prefixo}')
print(f'Número de IPs da rede: {calc.numer_ips}')