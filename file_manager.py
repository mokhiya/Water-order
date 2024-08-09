import os
import json


class JsonManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def _file_exists_and_not_empty(self):
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read(self):
        if self._file_exists_and_not_empty():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def write(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)

    def add_data(self, data: dict):
        all_data = self.read()
        all_data.append(data)
        self.write(all_data)
        return "Data added successfully"

    def update_data(self, identifier, key, new_data):
        all_data = self.read()
        updated = False

        for item in all_data:
            if item[key] == identifier:
                item.update(new_data)
                updated = True
                break

        if updated:
            self.write(all_data)
            return True
        return False

    def delete_data(self, identifier, key):
        all_data = self.read()
        updated_data = []

        for item in all_data:
            if item[key] != identifier:
                updated_data.append(item)

        self.write(updated_data)
        return len(updated_data) < len(all_data)


user_manager = JsonManager("users.json")
