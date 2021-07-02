"""Fabric自动化部署"""
from fabric.api import local


def hello(name=''):
    print(f'hello {name}')


def prepare_deploy():
    local("python manage.py test demo")
    # 前提已在当前目录git init
    # local("git add -p && git commit")
    # local("git push")
