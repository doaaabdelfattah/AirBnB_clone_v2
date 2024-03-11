#!/usr/bin/python3
''' Fabric script that generates a .tgz archive
from the contents of the
web_static folder of your
AirBnB Clone repo
'''
from datetime import datetime
from fabric.api import env, put, run
import os

env.hosts = ['34.207.211.205', '54.162.98.18']


def do_deploy(archive_path):
    '''distributes an archive to your web servers
    '''
    if os.path.isfile(archive_path) is False:
        return False
    filename = os.path.basename(archive_path)

    # Upload the archive to the /tmp/ directory of the web server
    if put(archive_path, "/tmp/{}".format(filename)).failed is True:
        return False

    # Uncompress the archive
    # tar -xzf archive.tgz -C /path/to/target_directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format((filename), filename)).failed is True:
        return False

    # Delete the archive from the web server
    if run("rm /tmp/{}".format(filename)).failed is True:
        return False

    # Delete the symbolic link /data/web_static/current
    if run("rm -rf /data/web_static/current".format(filename)).failed is True:
        return False

    # Create a new the symbolic link on the web server
    if run("ln -s /data/web_static/releases/{} /data/web_static/current".format(filename)).failed is True:
        return False
    
    return True
