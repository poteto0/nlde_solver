from setuptools import setup, find_packages

setup(
    name='nlde_solver',  # パッケージ名（pip listで表示される）
    version="1.0.0",  # バージョン
    description="solve nonlinear differential equations approximately",  # 説明
    author='poteto0',  # 作者名
    packages=find_packages(),  # 使うモジュール一覧を指定する
    license='MIT'  # ライセンス
)
