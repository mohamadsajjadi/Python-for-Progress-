import os
import shutil


class FileManager:
    deleted_files = []

    def find(self, name, address):
        result = []
        var = list(os.walk(address))
        for item in var:
            for file in item[2]:
                if name == file:
                    result.append(os.path.join(item[0], name))
        return result

    def create_file(self, name, address):
        try:
            if os.path.isfile(os.path.join(address, name)):
                pass
            else:
                with open(os.path.join(address, name), 'w') as f:
                    pass
        except:
            pass

    def create_dir(self, name, address):
        try:
            if os.path.isdir(os.path.join(address, name)):
                pass
            else:
                os.mkdir(os.path.join(address, name))
        except:
            pass

    def delete(self, name, address):
        try:
            if os.path.isfile(os.path.join(address, name)):
                t = (name, address)
                FileManager.deleted_files.append(t)
                backup = 'backup_' + name
                self.create_file(backup, address)
                shutil.copyfile(os.path.join(address, name), os.path.join(address, backup))
                os.remove(os.path.join(address, name))
        except:
            pass

    def restore(self, name):
        try:
            for item in FileManager.deleted_files[::-1]:
                if item[0] == name:
                    backup = 'backup_' + name
                    self.create_file(item[0], item[1])
                    shutil.copyfile(os.path.join(item[1], backup), os.path.join(item[1], item[0]))
                    os.remove(os.path.join(item[1], backup))
                    FileManager.deleted_files.remove(item)
                    break
        except:
            pass


# fm = FileManager()
# fm.create_dir('test', '.')
# fm.create_dir('test1', 'test')
# fm.create_dir('test2', 'test/test1/')
# fm.create_file('test.txt', 'test')
# fm.create_file('test.txt', 'test/test1')
# fm.create_file('test.txt', 'test/test1/test2')
# print(fm.find('test.txt', 'test'))
# fm.delete('test.txt', 'test')
# fm.delete('test.txt', 'test/test1/')
# fm.delete('test.txt', 'test/test1/test2')
# fm.restore('test.txt')
# fm.restore('test.txt')