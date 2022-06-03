from ncclient import manager

m = manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
    )
    
output = m.get_config("running")
print(output)

save = open('running.xml', 'w')
save.write(str(output))
save.close

