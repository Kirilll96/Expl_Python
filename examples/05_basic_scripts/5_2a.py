ip = input('network:')
mask = input('mask:')
print(f'Address your network: {ip}/{mask}')
ip_split = ip.split('.')
Nmask = f"{'1' * int(mask) + '0' * (32 - int(mask))}"
ip_ZeroOne = f"{int(ip_split[0]):08b}" + f"{int(ip_split[1]):08b}" + f"{int(ip_split[2]):08b}" + f"{int(ip_split[3]):08b}"
new_ip = f"{ip_ZeroOne[0:int(mask)] + '0' * (32 - int(mask))}"
print(f"""
        Network:
        {ip_split[0]:<8} {ip_split[1]:<8} {ip_split[2]:<8} {ip_split[3]:<8}
        {int(new_ip[0:8],2):<8} {int(new_ip[8:16],2):<8} {int(new_ip[16:24],2):<8} {int(new_ip[24:32],2):<8}
        {new_ip[0:8]:<08} {new_ip[8:16]:<08} {new_ip[16:24]:<08} {new_ip[24:32]:<08}
        
        Mask:
        /{mask}
        {int(Nmask[0:8],2):<8} {int(Nmask[8:16],2):<8} {int(Nmask[16:24],2):<8} {int(Nmask[24:32],2):<8}
        {Nmask[0:8]:<08} {Nmask[8:16]:<08} {Nmask[16:24]:<08} {Nmask[24:32]:<08}
        """)
        
