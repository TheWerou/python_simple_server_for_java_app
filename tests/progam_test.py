from Order_classes.order_fabric import Comends
from Data_base.file_handler import FileHandler
from Data_base.facade_storage import FacadeStorage

import os

# hih = FacadeStorage('C:\\Users\\wojte\\OneDrive\\Pulpit\\java\\herbata_piwo_py\\Storage')

cos = Comends('C:\\Users\\wojte\\OneDrive\\Pulpit\\java\\herbata_piwo_py\\Storage')

scheme_odp = '{"type": "LOG", "reciver": "SERWER", "from_who": "MACIEK", "what": "cofee", "with_sugar": "True"}'
coffee_odp = '{"type": "AKC", "reciver": "MACIEK", "from_who": "MICHAL","what": "coffee", "when": [16, 20], ' \
             '"with_sugar": "True", "with_milk": "True"} '

tee_odp = {"type": "AKC", "reciver": "SERWER", "from_who": "MACIEK",
           "what": "tee", "when": [16, 20], "with_sugar": "True", "with_honey": "True"}

log = '{"type": "LOG", "reciver": "SERWER", "from_who": "MACIEK"}'
log2 = '{"type": "LOG", "reciver": "SERWER", "from_who": "MICHAL"}'

ask3 = '{"type": "ASK", "reciver": "MICHAL", "from_who": "MACIEK"}'


chk = '{"type": "CHK", "reciver": "SERWER", "from_who": "MICHAL"}'
cmy = '{"type": "CMY", "reciver": "SERWER", "from_who": "MACIEK"}'

print(cos.main(log))
print(cos.main(log2))
print(cos.main(ask3))
print("---------------------------------------------------------------")
print(cos.main(chk))
print("---------------------------------------------------------------")
print(cos.main(cmy))
print("---------------------------------------------------------------")
print(cos.main(coffee_odp))

#hih.add_to_user_list("michal")
#hih.add_json_to_user_dir("michal", 'ASK', dykta)
#hih.add_json_to_user_dir("michal", 'JKK', dykta)
#print(hih.read_json_from_user_dir("michal", 'JKK'))
#hih.delete_json_file("michal", 'JKK')
