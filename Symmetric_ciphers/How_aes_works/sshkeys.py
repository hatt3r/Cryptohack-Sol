hex_modulus = "00:ad:3c:ba:9b:6b:e1:85:bc:31:dd:15:5b:35:56:f7:64:e7:a7:0a:aa:ac:39:71:da:26:96:ed:37:e3:ae:ba:52:ca:05:22:a9:22:83:c1:f9:90:db:0d:79:f4:a9:69:1f:e2:53:b1:b4:64:a0:a2:59:14:6e:01:b4:ec:b8:73:7e:0b:3e:76:e9:78:50:bf:38:0a:4c:19:13:19:85:dd:17:f5:9d:1b:fe:bf:ba:6a:2e:dd:9d:3e:c0:9b:d3:66:0b:c4:99:e1:1c:96:f8:ad:06:b3:d9:93:38:40:2b:53:39:ca:98:0d:47:8a:7c:b1:c2:69:95:38:12:49:bf:38:0a:4a:ae:97:f0:e3:fd:28:7e:7f:0a:3a:b1:4d:d2:de:3f:76:a9:cd:bb:05:51:82:86:94:22:1b:08:e3:ba:de:02:90:76:ae:cd:00:3f:80:a0:81:22:22:f2:ce:81:5c:2c:41:e1:8c:e0:4e:10:4a:e7:be:b4:4f:58:22:00:26:10:0b:93:05:76:ad:46:c3:e2:0d:48:59:ae:d0:23:6a:b7:9c:1d:27:96:78:cf:9e:38:f0:69:1e:d3:a4:7e:20:cb:63:52:21:83:43:74:2d:4f:67:ca:de:05:a1:67:19:35:e0:ce:14:36:b7:44:4e:04:d6:fe:64:38:07:f0:5c:be:29:31:be:80:46:a4:a6:ed:b4:6d:1a:81:f3:a3:4d:e9:fa:c3:2c:e9:19:f7:1d:f0:df:6b:49:b6:aa:ab:25:30:0b:cb:83:a2:dc:c5:b4:5c:f3:ba:d5:40:53:d7:7d:d5:36:a0:1b:35:81:84:da:0c:7e:99:70:55:39:ec:db:b1:8e:3a:0b:f5:76:7e:6c:41:24:92:98:fd:21:4d:b3:cc:0e:54:e1:ca:c2:a4:47:d0:62:39:56:c1:b5:61:90:a5:5f:77:ea:93:c1:83:25:84:44:6a:8c:a8:2f:71:ca:42:dd:54:7b:f6:56:ed:39:4f:45:8c:c0:a0:80:7a:d8:2d"

hex_modulus = hex_modulus.replace(":", "")

modulus_decimal = int(hex_modulus, 16)
print(modulus_decimal)

## convert hex to decimal that is ssh keys