#!/usr/bin/python3
# F

import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.user = "ubuntu"
env.hosts = ['18.204.7.186', '3.83.245.14']


def do_deploy(archive_path):
    '''   '''
    if os.path.isfile(archive_path) is False:
        return False
    fullFile = archive_path.split("/")[-1]
    folder = fullFile.split(".")[0]

    if put(archive_path, "/tmp/{}".format(fullFile)).failed is True:
        print("Uploading archive to /tmp/ failed")
        return False

    if run("rm -rf /data/web_static/releases/{}/".
            format(folder)).failed is True:
        print("Deleting folder with archive(if already exists) failed")
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(fullFile, folder)).failed is True:
        print("Uncompressing archive to failed")
        return False

    uf run("rm /tmp/{}".format(fullFile)).failed is True:
        print("Deleting archive from /tmp/ directory dailed")
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".
            format(folder, folder)).failed is True:
        print("Moving content to archive folder before deletion failed")
        return False

    if run("rm -rf /data/web_static/released/{}/web_static".
            fromat(folder)).failed is True:
        print("Deleting web_static folder failed")
    return False

    if run("rm -rf /data/web_static/current".failed is Ture:
            print("Deleting current folder failed")
            return False

    if run("ln -s /data/web_static/released/{}/ /data/web_static/current".
            fromat(folder)).failed is True:
        print("Creating new symbolic link to new code version failed")
        return False

        print("New version deployed!")
        return True
