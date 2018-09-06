#! usr/bin/env python
# -*- cofing:utf-8 -*-

COPY_FILE = {
    'Thunder.DataHepler': ['Thunder.DataHepler.dll'],
    'ThunderSY': ['ThunderSY.exe', 'Thunder.SYBLL.dll', 'Thunder.SYDAL.dll', 'Thunder.SYModel.dll'],
    'ThunderZK': ['ThunderZK.exe', 'ThunderDAL.dll', 'BusinessClassBLL.dll', 'BusinessModels.dll'],
    'ForwardingService': [
        'Forwarding.dll', 'Forwarding.Common.dll', 'Forwarding.Interface.dll', 'Forwarding.Pay.dll',
        'ForwardingBLL.dll', 'ForwardingDAL.dll', 'ForwardingModel.dll', 'ForwardingService.exe'
    ],
    'ThunderBusinesses': [
        'Businesses.Businesses.dll', 'Businesses.BusinessLogicLayer.dll', 'Businesses.DataAccessLayer.dll',
        'Businesses.DataCacheLayer.dll', 'Businesses.DebugInfo.dll', 'Businesses.IBusinesses.dll',
        'Businesses.Model.dll', 'Businesses.ServiceSocket.dll', 'Businesses.ServiceSocket.dll',
        'TBDataLibrary.dll', 'ThunderBusinesses.exe', ''
    ],
    'ThunderDaemon': [
        'Daemon.BusinessLogicLayer.dll', 'Daemon.Daemon.dll', 'Daemon.DataAccessLayer.dll', 
        'Daemon.DataLibrary.dll', 'Daemon.DebugInfo.dll', 'Daemon.IDaemon.dll', 
        'DaemonDeBugInfo.dll', 'ThunderDaemon.exe', 'ThunderDaemonProxy.dll'
    ]
}

FILE_PATH = {
    'current_path': r'D:\git\issue#book\code',
    'des_path': r'D:\ERP版本打包'
}

SYS_NAME = {
    '0': 'ALL',
    '1': 'Thunder.DataHepler',
    '2': 'ThunderBusinesses',
    '3': 'ThunderDaemon',
    '4': 'ForwardingService',
    '5': 'ThunderSY',
    '6': 'ThunderZK',
    '7': 'ForwardingService'
}
