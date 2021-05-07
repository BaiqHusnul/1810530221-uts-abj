f = open('vlan-database.txt', 'w')
while True:
    ch = input("input Data VLAN Baru (y/t)? ")
    if ch == 'y' or ch == 'Y':
        print("*" * 40)
        idvlan = input("Masukkan VLAN ID : ")
        nmvlan = input("Masukkan Nama VLAN : ")
        f.write(str("VLAN ID : "+idvlan+", Name : "+nmvlan)+ '\n')
        print("-" * 40)
        elif ch == 't' or ch == 'T':
            f.close()
            f = open('vlan-database.txt', "r")
            print(f.read())
            break
        else:
            print("Invalid Command")