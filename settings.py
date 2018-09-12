#! usr/bin/env python
# -*- cofing:utf-8 -*-

COMMAND = {
    'rebuild_shot': r'MSBuild.exe {0}\{1}.sln /t:rebuild /property:Configuration=Release',
    'rebuild': r'MSBuild.exe {0}\{1}\{1}.sln /t:rebuild /property:Configuration=Release',
    'rebuild_long': r'MSBuild.exe {0}\{1}\{1}\{1}.sln /t:rebuild /property:Configuration=Release'
}

COPY_FILE_PATH = {
    'file_name_path_shot': r'{0}\{1}\bin\Release\{2}',
    'file_name_path': r'{0}\{1}\{2}\bin\Release\{3}',
    'file_name_path_long': r'{0}\{1}\{1}\{2}\bin\Release\{3}',
}

LONG_PATH = ['ThunderBusinesses', 'ThunderDaemon', 'ThunderDeposit']
SHOT_PATH = ['']
SP_SYS_NAME = {
    'ThunderSetCenter': 'Thunder.SetCenter',
    'Thunder.Common': 'Thunder.Common.View'
}


COPY_FILE = {
    # 1
    'Thunder.DataHepler': ['Thunder.DataHepler.dll'],
    # 2
    'Thunder.Common': [
        'Thunder.Common.BLL.dll', 'Thunder.Common.DAL.dll', 'Thunder.Common.Model.dll', 'Thunder.Common.View.exe'
    ],
    # 3
    'ThunderBusinesses': [
        'Businesses.Businesses.dll', 'Businesses.BusinessLogicLayer.dll', 'Businesses.DataAccessLayer.dll',
        'Businesses.DataCacheLayer.dll', 'Businesses.DebugInfo.dll', 'Businesses.IBusinesses.dll',
        'Businesses.Model.dll', 'Businesses.ServiceSocket.dll', 'Businesses.ServiceSocket.dll',
        'TBDataLibrary.dll', 'ThunderBusinesses.exe', 'ThunderBusinessesProxy.dll'
    ],
    # 4
    'ThunderDaemon': [
        'Daemon.BusinessLogicLayer.dll', 'Daemon.Daemon.dll', 'Daemon.DataAccessLayer.dll', 
        'Daemon.DataLibrary.dll', 'Daemon.DebugInfo.dll', 'Daemon.IDaemon.dll', 
        'DaemonDeBugInfo.dll', 'ThunderDaemon.exe', 'ThunderDaemonProxy.dll'
    ],
    # 5
    'ThunderSY': ['ThunderSY.exe', 'Thunder.SYBLL.dll', 'Thunder.SYDAL.dll', 'Thunder.SYModel.dll'],
    # 6
    'ThunderZK': ['ThunderZK.exe', 'ThunderDAL.dll', 'BusinessClassBLL.dll', 'BusinessModels.dll'],
    # 7
    'ForwardingService': [
        'Forwarding.dll', 'Forwarding.Common.dll', 'Forwarding.Interface.dll', 'Forwarding.Pay.dll',
        'ForwardingBLL.dll', 'ForwardingDAL.dll', 'ForwardingModel.dll', 'ForwardingService.exe'
    ],
    # 8
    'ThunderSetCenter': [
        'Thunder.SetCenter.exe', 'ThunderSetCenterBLL.dll', 'ThunderSetCenterDAL.dll', 'ThunderSetCenterModel.dll'
    ],
    # 9
    'ThunderFM': [
        'ThunderFM.exe', 'ThunderFMBLL.dll', 'ThunderFMDAL.dll', 'ThunderFMModel.dll'
    ],
    # 10
    'ThunderMember': [
        'ThunderMember.exe', 'ThunderMember.BusinessLogicLayer.dll', 'ThunderMember.DataAccess.dll', 
        'ThunderMember.Foundation.dll', 'ThunderMember.Model.dll', 'ThunderMember.ViewModel.dll'
    ],
    'ThunderDeposit': [
        'ThunderDeposit.exe', 'ThunderDeposit.DataAccess.dll', 'ThunderDeposit.Foundation.dll',
        'ThunderDeposit.Model.dll', 'ThunderDeposit.ViewModel.dll'
    ],
    'ThunderSupermarket': [
        'ThunderSupermarket.exe', 'ThunderSupermarketBLL.dll', 'ThunderSupermarketDAL.dll', 'ThunderSupermarketModel.dll',
        'ThunderSupermarketRibbonLib.dll', r'zh-CN\ThunderSupermarket.resources.dll'
    ]
}

FILE_PATH = {
    'current_path': r'D:\git\issue#book\code',
    'des_path': r'D:\ERP版本打包'
}

SYS_NAME = {
    '0': 'ALL',
    '1': 'Thunder.DataHepler',
    '2': 'Thunder.Common',
    '3': 'ThunderBusinesses',
    '4': 'ThunderDaemon',
    '5': 'ForwardingService',
    '6': 'ThunderSY',
    '7': 'ThunderZK',
    '8': 'ThunderSetCenter',
    '9': 'ThunderFM',
    '10': 'ThunderMember',
    '11': 'ThunderDeposit',
    '12': 'ThunderSupermarket'
}
