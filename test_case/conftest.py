# encoding: utf-8
import os
import pytest
import yaml

'''
@author: lingshu
@file: conftest.py
@time: 2019/6/6 11:10
@desc:
'''

def pytest_sessionfinish(session):
    print("\n")
    print(">>>>>>=====================================<<<<<<")
    print(session)
    print(session.config)
    print(session.config.getoption('allure_report_dir'))

@pytest.fixture(scope="session", autouse=True)
def env_config(request):
    """
    读取yml配置文件
    """
    project_name = 'api_auto_test'
    rootPath = get_root_path(project_name)
    config_path = os.path.abspath(rootPath + 'config' + os.sep + 'env_config.yml')  # 获取tran.csv文件的路径
    with open(config_path) as f:
        env_config = yaml.load(f)  # 读取配置文件
    return env_config


def get_root_path(project_name):
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find(project_name + os.sep) + len(project_name + os.sep)]  # 获取myProject，也就是项目的根路径
    return rootPath
