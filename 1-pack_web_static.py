#!/usr/bin/python3
''' Fabric script that generates a .tgz archive
from the contents of the 
web_static folder of your 
AirBnB Clone repo
'''
from datetime import datetime
from fabric.api import local

def do_pack():
    ''' Create a tgz file of directory.'''
    # the current date now
    dt = datetime.utcnow()
    file = "versions/web_static_{}.tgz".fromat(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    
    
    # Create a source distribution tar archive (for a Python App.)
    # command for archive tar [-options] <name of the tar archive> [files or directories which to add into archive]
    local("tar -cvzf {} web_static".format(file))