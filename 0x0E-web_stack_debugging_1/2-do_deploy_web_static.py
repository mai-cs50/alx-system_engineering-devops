#!/usr/bin/python3
from fabric.api import env, put, run
import os

env.user = "ubuntu"
env.hosts = ['18.204.7.186', '3.83.245.14']


def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False

    filename = os.path.basename(archive_path)
    foldername = filename.split(".")[0]

    try:
        put(archive_path, "/tmp/{}".format(filename))
        run("mkdir -p /data/web_static/releases/{}/".format(foldername))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(filename, foldername))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".
            format(foldername, foldername))
        run("rm -rf /data/web_static/releases/{}/web_static".
            format(foldername))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(foldername))
        print("New version deployed!")
        return True
    except Exception as e:
        print("Deployment failed:", str(e))
        return False

