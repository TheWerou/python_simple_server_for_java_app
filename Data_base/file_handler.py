import csv
import json
import os
import shutil


class FileHandler:
    def __init__(self, adress):
        self.file_path = adress

    def create_dir(self, dir_name):
        try:
            file_adr_name = self.file_path + '\\' + dir_name
            os.mkdir(file_adr_name)
            return True
        except FileExistsError:
            return False

    def delete_dir(self, dir_name):
        try:
            file_adr_name = self.file_path + '\\' + dir_name
            shutil.rmtree(file_adr_name)
            return True
        except FileExistsError:
            return False

    def write_csv_file(self, file_name, list_to_save, type_of_in='w+'):
        file_name = self.file_path + '\\' + file_name + '.csv'

        multy_list = False
        for i in list_to_save:
            if type(i) is list:
                multy_list = True

        with open(file_name, type_of_in, newline='') as file:
            writer = csv.writer(file)

            if multy_list is True:
                writer.writerows(list_to_save)
            else:
                save_prep = [list_to_save]
                writer.writerow(save_prep)

    def erase_and_write_csv_file(self, file_name, list_to_save, type_of_in='w'):
        file_name = self.file_path + '\\' + file_name + '.csv'

        with open(file_name, type_of_in, newline='') as file:
            writer = csv.writer(file)
            writer.writerows(list_to_save)

    def read_csv_file(self, file_name):
        file_name = self.file_path + '\\' + file_name + '.csv'
        output = None
        output_list = []
        try:
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                iter = 0
                for row in reader:
                    if iter == 1:
                        output_list.append(output)
                        output_list.append(row)
                    elif iter > 1:
                        output_list.append(row)
                    else:
                        output = row

                    iter += 1

                if iter == 1:
                    return output
                else:
                    return output_list
        except FileNotFoundError:
            return []

    def write_json_file(self, file_name, text_to_save, type_of_in='w+'):
        file_name = self.file_path + '\\' + file_name + ".json"

        with open(file_name, type_of_in, newline='') as file:
            json.dump(text_to_save, file)

    def read_json_file(self, file_name):
        file_name = self.file_path + '\\' + file_name

        with open(file_name, 'r', newline='') as file:
            output = json.load(file)

        return output

    def delete_file(self, file_name):
        try:
            file_adr_name = self.file_path + '\\' + file_name
            os.remove(file_adr_name)
            return True
        except FileExistsError:
            return False

