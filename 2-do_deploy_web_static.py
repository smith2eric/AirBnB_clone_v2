#!/usr/bin/python3
<<<<<<< HEAD
"""This script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy"""


from fabric.api import env, put, run
from os.path import exists
import shlex
env.hosts = ['35.185.108.180', '34.229.169.234']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """All remote commands must be executed on your both web servers
    (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in your script)"""
    if not exists(archive_path):
        return False
    try:
        pname = archive_path.replace('/', ' ')
        pname = shlex.split(pname)
        pname = pname[-1]

        wname = pname.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(pname)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except BaseException:
        return False
=======
"""
Distributes archived pack to both web servers
Usage:
    fab -f 2-do_deploy_web_static.py do_deploy:
    archive_path=versions/<file_name> -i my_ssh_private_key

Example:
    fab -f 2-do_deploy_web_static.py do_deploy:
    archive_path=versions/web_static_20170315003959.tgz -i my_ssh_private_key
"""

import os.path
from fabric.api import env, put, run

env.user = "ubuntu"
env.hosts = ["34.75.10.160", "35.231.86.187"]


def do_deploy(archive_path):
    """Distributes an archive to a web server.
       Returns True if successful and false if not
    """
    if os.path.isfile(archive_path) is False:
        return False
    fullFile = archive_path.split("/")[-1]
    folder = fullFile.split(".")[0]

    # Uploads archive to /tmp/ directory
    if put(archive_path, "/tmp/{}".format(fullFile)).failed is True:
        print("Uploading archive to /tmp/ failed")
        return False

    # Delete the archive folder on the server
    if run("rm -rf /data/web_static/releases/{}/".
           format(folder)).failed is True:
        print("Deleting folder with archive(if already exists) failed")
        return False

    # Create a new archive folder
    if run("mkdir -p /data/web_static/releases/{}/".
           format(folder)).failed is True:
        print("Creating new archive folder failed")
        return False

    # Uncompress archive to /data/web_static/current/ directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(fullFile, folder)).failed is True:
        print("Uncompressing archive to failed")
        return False

    # Deletes latest archive from the server
    if run("rm /tmp/{}".format(fullFile)).failed is True:
        print("Deleting archive from /tmp/ directory dailed")
        return False

    # Move folder from web_static to its parent folder,to expose the index
    # files outsite the /we_static path
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".
           format(folder, folder)).failed is True:
        print("Moving content to archive folder before deletion failed")
        return False

    # Delete the empty web_static file, as its content have been moved to
    # its parent directory
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(folder)).failed is True:
        print("Deleting web_static folder failed")
        return False

    # Delete current folder being served (the symbolic link)
    if run("rm -rf /data/web_static/current").failed is True:
        print("Deleting 'current' folder failed")
        return False

    # Create new symbolic link on web server linked to new code version
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(folder)).failed is True:
        print("Creating new symbolic link to new code version failed")
        return False

    print("New version deployed!")
    return True
>>>>>>> e3cc30ab45a610fcb3b4e6a7cc759ef6443e7fa5
