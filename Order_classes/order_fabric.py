from Data_base.facade_storage import FacadeStorage
from Order_classes.basic_classes.tee_order import TeeOrder
from Order_classes.basic_classes.coffee_order import CoffeeOrder

import os
import json


class Comends:
    def __init__(self, place_to_save, user="None"):
        self.user = user
        self.place_to_save = place_to_save
        # self.out_comands = ["ASK", "NOO", "AKC", "LST", "WRG", "SND"]

    def check_input(self, recived_dictionary):
        try:
            if recived_dictionary['type'] and recived_dictionary['reciver'] and recived_dictionary['from_who']:
                return True

        except KeyError:
            return False

    def main(self, recived_string):
        recived_dictionary = json.loads(recived_string)
        if self.check_input(recived_dictionary) is True:
            if recived_dictionary['type'] == "ASK":
                return self.handle_ask(recived_dictionary)

            elif recived_dictionary['type'] == "CHK":
                return self.handle_chk(recived_dictionary)

            elif recived_dictionary['type'] == "CMY":
                return self.handle_cmy(recived_dictionary)

            elif recived_dictionary['type'] == "NOO":
                return self.handle_noo(recived_dictionary)

            elif recived_dictionary['type'] == "AKC":
                try:
                    if recived_dictionary['what'] == "coffee":
                        if recived_dictionary['with_sugar'] and recived_dictionary['with_milk']:
                            return self.handle_akc(recived_dictionary)
                    elif recived_dictionary['what'] == "tee":
                        if recived_dictionary['with_sugar'] and recived_dictionary['with_honey']:
                            return self.handle_akc(recived_dictionary)
                    else:
                        return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                                           "from_who": "SERWER", "reason": "no such drink"})
                except KeyError:
                    return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                                       "from_who": "SERWER", "reason": "wrong json send"})

            elif recived_dictionary['type'] == "LOG":
                return self.handle_log(recived_dictionary)

            else:
                pass
        else:
            pass
            # return wrg

    def handle_ask(self, recived_dictionary):
        file_saver = self.__object_files_facede()
        invitations = file_saver.get_list_of_json_from_user_files(recived_dictionary["from_who"])
        if not self.__check_if_inv_exist("ASK", recived_dictionary["from_who"], invitations):

            if file_saver.find_user(recived_dictionary["reciver"]) is not False and \
                    file_saver.find_user(recived_dictionary["from_who"]) is not False:

                json_to_save = {"type": "ASK", "reciver": recived_dictionary["reciver"],
                                "from_who": recived_dictionary["from_who"]}

                self.__save_file_both("ASK", recived_dictionary, json.dumps(json_to_save))

            else:
                return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                                   "from_who": "SERWER", "reason": "recipient not exist"})

        return json.dumps({"type": "END", "reciver": recived_dictionary["from_who"], "from_who": "SERWER"})

    def handle_chk(self, recived_dictionary):
        file_saver = self.__object_files_facede()

        if file_saver.find_user(recived_dictionary["from_who"]) is not False:

            invitations = file_saver.get_list_of_json_from_user_files(recived_dictionary["from_who"])
            amount_of_in = len(invitations)
            invitations_list = []
            snd_json = json.dumps({"type": "SND", "reciver": recived_dictionary["from_who"], "from_who": "SERWER",
                                   "amount": amount_of_in})
            invitations_list.append(snd_json)

            for js in invitations:

                invitations_list.append(file_saver.read_json_from_user_dir(recived_dictionary["from_who"], js))
                helper = self.__check_type(js)
                if helper is not False:
                    file_saver.delete_json_file(helper[1], js)

            invitations_list.append(json.dumps({"type": "END", "reciver": recived_dictionary["from_who"],
                                                "from_who": "SERWER"}))
            return invitations_list
        else:
            return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                               "from_who": "SERWER", "reason": "somthing went wrong"})

    def handle_cmy(self, recived_dictionary):
        file_saver = self.__object_files_facede()
        if file_saver.find_user(recived_dictionary["from_who"]) is not False:

            invitations = file_saver.get_list_of_json_from_user_files(recived_dictionary["from_who"], False)
            amount_of_in = len(invitations)
            invitations_list = []
            snd_json = json.dumps({"type": "SND", "reciver": recived_dictionary["from_who"], "from_who": "SERWER",
                                   "amount": amount_of_in})
            invitations_list.append(snd_json)

            for js in invitations:
                invitations_list.append(file_saver.read_json_from_user_dir(recived_dictionary["from_who"], js, False))
                helper = self.__check_type(js)
                if helper is not False:
                    file_saver.delete_json_file(helper[1], js, False)

            invitations_list.append(json.dumps({"type": "END", "reciver": recived_dictionary["from_who"],
                                                "from_who": "SERWER"}))
            return invitations_list
        else:
            return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                               "from_who": "SERWER", "reason": "somthing went wrong"})

    def handle_noo(self, recived_dictionary):
        file_saver = self.__object_files_facede()
        invitations = file_saver.get_list_of_json_from_user_files(recived_dictionary["from_who"])

        if not self.__check_if_inv_exist("ASK", recived_dictionary["from_who"], invitations):
            file_to_del = "ASK_" + recived_dictionary["from_who"]
            file_saver.delete_json_file(recived_dictionary["from_who"], file_to_del)

            json_to_save = {"type": "NOO", "reciver": recived_dictionary["reciver"],
                            "from_who": recived_dictionary["from_who"]}

            self.__save_file_both("NOO", recived_dictionary, json.dumps(json_to_save))

            return json.dumps({"type": "END", "reciver": recived_dictionary["from_who"], "from_who": "SERWER"})

        else:
            return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                               "from_who": "SERWER", "reason": "somthing went wrong 2"})

    def handle_akc(self, recived_dictionary):
        file_saver = self.__object_files_facede()
        invitations = file_saver.get_list_of_json_from_user_files(recived_dictionary["from_who"])
        invitations2 = file_saver.get_list_of_json_from_user_files(recived_dictionary["reciver"], False)

        if self.__check_if_inv_exist("ASK", recived_dictionary["reciver"], invitations) and \
                self.__check_if_inv_exist("ASK", recived_dictionary["from_who"], invitations2):

            file_to_del = "ASK_" + recived_dictionary["reciver"]
            file_saver.delete_json_file(recived_dictionary["from_who"], file_to_del)

            file_to_del = "ASK_" + recived_dictionary["from_who"]
            file_saver.delete_json_file(recived_dictionary["reciver"], file_to_del, False)

            if recived_dictionary['what'] == "tee":
                order_class = TeeOrder(recived_dictionary)
            else:
                order_class = CoffeeOrder(recived_dictionary)

            order_class = json.dumps(order_class.__dict__)
            print("przeszlo")
            self.__save_file_both("AKC", recived_dictionary, order_class)
            return json.dumps({"type": "END", "reciver": recived_dictionary["from_who"], "from_who": "SERWER"})

        else:
            return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                               "from_who": "SERWER", "reason": "somthing went wrong 1"})

    def handle_log(self, recived_dictionary):
        saver = self.__object_files_facede()
        if saver.add_to_user_list(recived_dictionary['from_who']) is True:
            return json.dumps({"type": "END", "reciver": recived_dictionary["from_who"], "from_who": "SERWER"})
        else:
            return json.dumps({"type": "WRG", "reciver": recived_dictionary["from_who"],
                               "from_who": "SERWER", "reason": "User exist"})

    def __object_files_facede(self):
        return FacadeStorage(self.place_to_save)

    def __check_if_inv_exist(self, type, name_of_user, names_in_list):
        lenght_list = len(names_in_list)
        print("===============================================================")
        print(name_of_user)
        print("===============================================================")
        print(names_in_list)
        print("===============================================================")
        for i in range(lenght_list):
            helepr = names_in_list[i].split('_')
            print(helepr)
            print("===============================================================")
            if helepr[0] == type:
                if helepr[1] == name_of_user + '.json':
                    return True
                else:
                    return False

        return False

    def __check_type(self, names_in_list):
        helepr = names_in_list.split('_')
        if helepr[0] == "NOO" or helepr[0] == "AKC":
            return True, helepr[1]
        else:
            return False

    def __save_file_both(self, name_of_file, recived_dictionary, json_to_save):

        file_saver = self.__object_files_facede()

        name_of_file = "to_me\\" + name_of_file + "_" + recived_dictionary["from_who"]
        file_saver.add_json_to_user_dir(recived_dictionary["reciver"], name_of_file, json_to_save)

        name_file2 = "to_others\\" + name_of_file + "_" + recived_dictionary["reciver"]
        file_saver.add_json_to_user_dir(recived_dictionary["from_who"], name_file2, json_to_save)

    def __dell_both_file(self, recived_dictionary):
        file_saver = self.__object_files_facede()

        file_to_del = "ASK_" + recived_dictionary["from_who"]
        file_saver.delete_json_file(recived_dictionary["from_who"], file_to_del)
        file_saver.delete_json_file(recived_dictionary["reciver"], file_to_del, False)
