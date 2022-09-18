#!/usr/bin/python3
<<<<<<< HEAD
""" This Fabric script generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack."""
from fabric.operations import local
=======
"""
generates a .tgz archive from the contents of the web_static folder
Usage:
    fab -f 1-pack_web_static.py do_pack
"""
from fabric.api import local
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
from datetime import datetime


def do_pack():
<<<<<<< HEAD
    """ All archives must be stored in the folder versions
    (your function should create this folder if it doesn’t exist) """
    local("mkdir -p versions")
    status = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if status.failed:
        return None
    print(status)
    return status
=======
    """Generates .tgz archive from the contents of /web_static
       returns archive's path if successful and None if not
    """
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    filePath = 'versions/web_static_{}.tgz'.format(now)

    local('mkdir -p versions/')
    createArchive = local('tar -cvzf {} web_static/'.format(filePath))

    if createArchive.succeeded:
        return filePath
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
