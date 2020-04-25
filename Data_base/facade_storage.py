from Data_base.file_handler import FileHandler

import os


class FacadeStorage:
    def __init__(self, path_to_save_file):
        self.user_list = []
        self.inv_to_save = []
        self.name_of_csv_list = 'csv_user_list'
        self.path_to_save_file = path_to_save_file
        self.file_saver = FileHandler(path_to_save_file)

    def add_to_user_list(self, user_name):
        self.user_list.clear()
        self.user_list = self.get_list_of_users()
        user_name = user_name.upper()

        for i in self.user_list:
            if len(self.user_list) == 1:
                if user_name == i:
                    return False
            else:
                if user_name == i[0]:
                    return False

        self.user_list.append(user_name)
        self.file_saver.write_csv_file(self.name_of_csv_list, user_name, 'a+')
        self.create_dirs_for_user(user_name)
        return True

    def add_json_to_user_dir(self, user_name, name_of_file, json_to_save):
        user_name = user_name.upper()
        name_of_file = '\\users_dir\\' + user_name + '\\invitations\\' + name_of_file
        self.file_saver.write_json_file(name_of_file, json_to_save)

    def get_list_of_json_from_user_files(self, user_name, from_to_me=True):
        user_name = user_name.upper()
        if from_to_me:
            name_of_file = self.path_to_save_file + '\\users_dir\\' + user_name + '\\invitations\\to_me'
        else:
            name_of_file = self.path_to_save_file + '\\users_dir\\' + user_name + '\\invitations\\to_others'

        helper_list = []
        for js in os.listdir(name_of_file):
            if js.endswith('.json'):
                helper_list.append(js)

        return helper_list

    def read_json_from_user_dir(self, user_name, name_of_file, from_to_me=True):
        user_name = user_name.upper()
        if from_to_me:
            name_of_file = 'users_dir\\' + user_name + '\\invitations\\to_me\\' + name_of_file
        else:
            name_of_file = 'users_dir\\' + user_name + '\\invitations\\to_others\\' + name_of_file

        return self.file_saver.read_json_file(name_of_file)

    def delete_json_file(self, user_name, name_of_file, from_to_me=True):
        user_name = user_name.upper()
        if from_to_me:
            name_of_file = 'users_dir\\' + user_name + '\\invitations\\to_me\\' + name_of_file + ".json"
        else:
            name_of_file = 'users_dir\\' + user_name + '\\invitations\\to_others\\' + name_of_file + ".json"

        self.file_saver.delete_file(name_of_file)

    def create_dirs_for_user(self, user_name):
        helper = 'users_dir\\' + user_name + '\\'
        if not ['users_dir'] in os.listdir(self.path_to_save_file):
            self.file_saver.create_dir('users_dir')

        self.file_saver.create_dir(helper)
        self.file_saver.create_dir(helper + 'personal')
        self.file_saver.create_dir(helper + 'invitations')
        self.file_saver.create_dir(helper + 'invitations\\to_me')
        self.file_saver.create_dir(helper + 'invitations\\to_others')

    def del_user_from_list(self, user_name):
        self.user_list.clear()
        self.user_list = self.get_list_of_users()
        user_name = user_name.upper()
        helper = self.find_user(user_name)
        if helper is not False:
            del self.user_list[helper]
            self.file_saver.erase_and_write_csv_file(self.name_of_csv_list, self.user_list, 'w+')
            self.file_saver.delete_dir('users_dir\\'+user_name)
            return True
        else:
            return False

    def find_user(self, name_to_find):
        self.user_list.clear()
        self.user_list = self.get_list_of_users()
        try:
            return self.user_list.index([name_to_find])
        except ValueError:
            return False

    def get_list_of_users(self):
        file_name = 'csv_user_list'
        return self.file_saver.read_csv_file(file_name)

    def del_multyply_lines(self):
        self.user_list.clear()
        self.user_list = self.get_list_of_users()

        for i in range(len(self.user_list)):
            for j in range(i+1, len(self.user_list)):
                if self.user_list[i][0] == self.user_list[j][0]:
                    del self.user_list[j]

        return self.user_list
