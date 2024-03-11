#!/usr/bin/python3
''' Fabric script that generates a .tgz archive
from the contents of the 
web_static folder of your 
AirBnB Clone repo
'''
from datetime import datetime
from fabric.api import local
import os

def do_pack():
    ''' Create a tgz file of directory.'''
    # the current date now
    dt = datetime.utcnow()
    file = "versions/web_static_{}.tgz".format(dt.strftime("%Y%m%d%H%M%S"))
    
    
    # Create a source distribution tar archive (for a Python App.)
    if not os.path.exists("versions"):
       local("mkdir -p versions")
    # command for archive tar [-options] <name of archive> [files or directories which to add into archive]
    if local("tar -cvzf {} web_static".format(file)).return_code != 0:
        return None    
    return file