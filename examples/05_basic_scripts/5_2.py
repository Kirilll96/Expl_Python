#IpAddress = input('Enter network ip-address and network mask(for type xxx.xxx.xxx.xxx/xx):'+'/')
ip = input('network:')
mask = input('mask:')
print(f'Address your network: {ip}/{mask}')
ip = ip.split('.')
NetworkMask = {
'32' : [255, 255, 255, 255],
'31' : [255, 255, 255, 254],
'30' : [255, 255, 255, 252],
'29' : [255, 255, 255, 248],
'28' : [255, 255, 255, 240],
'27' : [255, 255, 255, 224],
'26' : [255, 255, 255, 192],
'25' : [255, 255, 255, 128],
'24' : [255, 255, 255, 0]
}
print(f"""
        Network:
        {ip[0]:<8} {ip[1]:<8} {ip[2]:<8} {ip[3]:<8}
        {int(ip[0]):08b} {int(ip[1]):08b} {int(ip[2]):08b} {int(ip[3]):08b}
        
        Mask:
        /{mask}
        {NetworkMask[f'{mask}'][0]:<8} {NetworkMask[f'{mask}'][1]:<8} {NetworkMask[f'{mask}'][2]:<8} {NetworkMask[f'{mask}'][3]:<8}
        {bin(NetworkMask[f'{mask}'][0]):<08} {bin(NetworkMask[f'{mask}'][1]):<08} {bin(NetworkMask[f'{mask}'][2]):<08} {bin(NetworkMask[f'{mask}'][3]):<08}""")
