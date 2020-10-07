import hashlib

do_work = True

res_list = []
res_list_ni = []

while do_work:
    i = 0
    inputstr = input("Zu verhaeschende Zeichenkette eingeben: ")
    inp = inputstr.encode('utf-8')
    h = hashlib.sha256(inp)
    res_list.append([i,inputstr,h.hexdigest()])
    res_list_ni.append(h.hexdigest())
    inputstr = input("Weitere Zeichenkette verhaeschen? (Y/N)")
    if inputstr=="Y" or inputstr=="y":
        do_work = True
    else:
        do_work = False


print("Verhaeschte Liste mit Identifier")
for elem in res_list:
    print(elem)

print("Verhaeschte Liste ohne Identifier")
for elem in res_list_ni:
    print(elem)