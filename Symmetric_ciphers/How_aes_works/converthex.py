
hex_modulus = "00:b9:88:f4:ea:6e:6a:e0:cf:12:b0:44:30:29:7f:b9:34:fb:36:97:20:76:93:b8:1e:67:0e:2b:3f:af:1e:51:99:aa:38:37:aa:c4:38:ef:e6:69:4b:63:69:f3:fd:12:6c:3d:d9:2c:e0:9f:b2:e6:df:7a:28:0c:a8:dd:2e:60:98:3a:84:38:c1:bb:26:0a:09:f4:a5:3e:e0:73:d0:17:33:fd:0b:c1:b2:fa:18:ac:0a:17:68:f5:e1:7a:51:e5:86:4e:2a:1a:cc:50:c8:75:15:0a:fa:06:66:f3:57:35:88:f1:21:38:12:18:bb:70:9a:bb:7d:8b:46:db:fe:2f:db:f3:aa:b7:b4:3a:59:5f:ee:87:87:a9:c6:dc:30:12:0a:2f:a3:29:b0:93:06:fa:77:89:3e:72:02:23:7e:81:65:91:0c:bb:ab:fa:7f:cc:c8:2a:e0:7b:55:41:c0:6c:37:50:ea:db:01:cc:ba:57:cf:b5:cf:05:47:8a:3d:ad:45:93:c7:76:d8:42:3d:f6:97:87:c1:6b:74:46:e2:4f:d1:0b:09:9e:c6:b8:a2:3e:82:ea:51:3e:73:9f:af:54:76:ba:8d:5b:19:92:99:76:3e:e5:d9:d3:96:ba:f7:13:91:67:8a:2a:fa:7c:33:2b:c3:bf:4a:dd:61:6c:d0:57:b1"

hex_modulus = hex_modulus.replace(":", "")

print(hex_modulus)

modulus_decimal = int(hex_modulus, 16)
print( modulus_decimal)

## formatiing hex removing ":" and converting to integer