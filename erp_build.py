#! usr/bin/env python
## -*- coding:utf-8 -*-

import os 
import stat
import shutil
import logging

from pprint import pprint
from settings import COPY_FILE, SYS_NAME, FILE_PATH

COMMAND = {
    'rebuild': r'MSBuild.exe {0}\{1}\{1}.sln /t:rebuild /property:Configuration=Release',
    'rebuild_long': r'MSBuild.exe {0}\{1}\{1}\{1}.sln /t:rebuild /property:Configuration=Release'
}
COPY_FILE_PATH = {
    'filename_path': r'{0}\{1}\{1}\bin\Release\{2}',
    'filename_path_long': r'{0}\{1}\{1}\{1}\bin\Release\{2}',
}

LONG_PATH = ['ThunderBusinesses', 'ThunderDaemon']

class RebuildClass(object):

    def __init__(self):
        self.current_path = FILE_PATH['current_path']
        self.des_path = FILE_PATH['des_path']

        if not os.path.exists(self.des_path):
            os.makedirs(self.des_path) 
        
        list_rebuild_paths = os.listdir(self.current_path)
        list_rebuild_paths = [list_rebuild_path for list_rebuild_path in list_rebuild_paths \
        if os.path.isdir(self.current_path + '\\' + list_rebuild_path)]
        self.list_path = list_rebuild_paths

    def copy_file(self, fun_name):

        list_file = COPY_FILE[fun_name]
        path = 'filename_path' if fun_name not in LONG_PATH else 'filename_path_long'
        for i in list_file:
            file_path = COPY_FILE_PATH[path].format(self.current_path, fun_name, i)
            ocx_path_file = self.current_path + '\\OCX\\' + i
            des_path_file = self.des_path + '\\' + i 

            if not os.path.isfile(file_path):
                return

            self.move_file(file_path, ocx_path_file)
            self.move_file(file_path, des_path_file)

    def move_file(self, file_path, des_path):
        '''文件移动'''
        try:
            #  去掉目标文件只读属性
            os.chmod(file_path, stat.S_IWRITE)
            shutil.copy(file_path, des_path)
            logging.info('copy: %s TO %s' %(file_path, des_path))
        except Exception as e:
            logging.error(e)

    def rebuild(self, sys_name):
        path = 'rebuild' if sys_name not in LONG_PATH else 'rebuild_long'

        cmd_rebuild_command = COMMAND[path].format(self.current_path,sys_name)
        print(cmd_rebuild_command)
        os.system(cmd_rebuild_command)
        self.copy_file(sys_name)


def print_info():
    for key, value in SYS_NAME.items():
        print('index: %s, SysName: %s'%(key, value))
    input_key = input('put you index:')
    return input_key

if __name__ == '__main__':
    
    print('press q to quit')
    input_key = print_info()
    while True:
        if input_key == 'q':
            break
        if input_key in SYS_NAME.keys():
            print(input_key)
            rc = RebuildClass()
            if input_key == '0':
                for key, value in SYS_NAME.items():
                    if key != '0':
                        rc.rebuild(value)
            else:
                rc.rebuild(SYS_NAME[input_key])
        input_key = print_info()