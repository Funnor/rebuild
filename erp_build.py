#! usr/bin/env python
## -*- coding:utf-8 -*-

import os 
import stat
import shutil
import logging

from pprint import pprint
from settings import COPY_FILE, SYS_NAME, FILE_PATH, COMMAND, COPY_FILE_PATH, LONG_PATH, SHOT_PATH, SP_SYS_NAME


class RebuildClass(object):

    def __init__(self):
        self.current_path = FILE_PATH['current_path']
        self.des_path = FILE_PATH['des_path']
        
        list_rebuild_paths = os.listdir(self.current_path)
        list_rebuild_paths = [list_rebuild_path for list_rebuild_path in list_rebuild_paths \
        if os.path.isdir(self.current_path + '\\' + list_rebuild_path)]
        self.list_path = list_rebuild_paths

    def get_path(self, fun_name):
        copy_path = 'file_name_path' if fun_name not in LONG_PATH else 'file_name_path_long'
        rebuid_path = 'rebuild' if fun_name not in LONG_PATH else 'rebuild_long'
        return rebuid_path, copy_path

    def copy_file(self, fun_name):

        # 判断路径是否存在
        if not os.path.exists(self.des_path):
            os.makedirs(self.des_path)
        if fun_name == 'ThunderSupermarket' and not os.path.exists(self.des_path):
            os.makedirs(self.des_path + r'\zh-CN')

        list_file = COPY_FILE[fun_name]
        _, path = self.get_path(fun_name)
 
        for i in list_file:
            if fun_name in SP_SYS_NAME:
                file_path = COPY_FILE_PATH[path].format(self.current_path, fun_name, SP_SYS_NAME[fun_name], i)
            else:
                file_path = COPY_FILE_PATH[path].format(self.current_path, fun_name, fun_name, i)
            ocx_path_file = self.current_path + '\\OCX\\' + i
            des_path_file = self.des_path + '\\' + i 

            if not os.path.isfile(file_path):
                continue

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

        path,_ = self.get_path(sys_name)
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