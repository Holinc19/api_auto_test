import os
import pytest

if __name__ == '__main__':
    if os.path.exists("allure-results"):
        for i in os.listdir("allure-results"):
            if os.path.isfile("allure-results/" + i):
                os.remove("allure-results/" + i)
    pytest.main(['--capture=no', '-v', '--alluredir=allure-results/'])

    # 生成allure报告
    # allure generate allure-results/ -c -o allure-report/
