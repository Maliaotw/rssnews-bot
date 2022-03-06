from conf import settings
import json
import time
import os


class JsonFile:

    path = settings.ACCESSKEY_FILE

    def __init__(self):
        self.data = self.get_or_create_json()

    def get_or_create_json(self):
        if os.path.exists(self.path):
            data = json.load(open(self.path, 'r'))
        else:
            data = {}
            # json.dump(data, open(self.path, 'w'))

        return data


    def set_data(self,data: dict):
        self.data = data
        self.save()


    def save(self):
        json.dump(self.data, open(self.path, 'w'))


    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)


class AccessKeyFile(JsonFile):

    @property
    def API_SECRET(self):
        return self.data['secret']

    @property
    def API_ID(self):
        return self.data['id']




if __name__ == '__main__':
    jrecord = JsonFile()
    print(jrecord.data)

