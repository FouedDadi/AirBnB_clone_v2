#!/usr/bin/python3
"""
fab script that generates a .tgz archive from the contents of the web_static
"""
from datetime import datetime
from os.path import isdir
from fabric.api import local


def do_pack():
    """
    function do_pack
    """
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".format(dt))
        return ("versions/web_static_{:s}.tgz".format(dt))
    except:
        return None
