Microsoft Windows [Version 10.0.22000.348]
(c) Microsoft Corporation. All rights reserved.

---------------------------------

## C:\Users\Vicky\Desktop\Repository\Basics-of-Python\Day 5 - pypi>python setup.py sdist

    running sdist
    running egg_info
    creating vanks.egg-info
    writing vanks.egg-info\PKG-INFO
    writing dependency_links to vanks.egg-info\dependency_links.txt
    writing top-level names to vanks.egg-info\top_level.txt
    writing manifest file 'vanks.egg-info\SOURCES.txt'
    reading manifest file 'vanks.egg-info\SOURCES.txt'
    reading manifest template 'MANIFEST.in'
    writing manifest file 'vanks.egg-info\SOURCES.txt'
    running check
    warning: check: missing meta-data: if 'author' supplied, 'author_email' should be supplied too

    creating vanks-0.0.1
    creating vanks-0.0.1\vanks.egg-info
    creating vanks-0.0.1\vicks
    copying files to vanks-0.0.1...
    copying MANIFEST.in -> vanks-0.0.1
    copying Readme.txt -> vanks-0.0.1
    copying setup.py -> vanks-0.0.1
    copying vanks.egg-info\PKG-INFO -> vanks-0.0.1\vanks.egg-info
    copying vanks.egg-info\SOURCES.txt -> vanks-0.0.1\vanks.egg-info
    copying vanks.egg-info\dependency_links.txt -> vanks-0.0.1\vanks.egg-info
    copying vanks.egg-info\top_level.txt -> vanks-0.0.1\vanks.egg-info
    copying vicks\__init__.py -> vanks-0.0.1\vicks
    copying vicks\account.py -> vanks-0.0.1\vicks
    Writing vanks-0.0.1\setup.cfg
    creating dist
    Creating tar archive
    removing 'vanks-0.0.1' (and everything under it)

---------------------------------------

## C:\Users\Vicky\Desktop\Repository\Basics-of-Python\Day 5 - pypi>twine upload dist/*

    Uploading distributions to https://upload.pypi.org/legacy/
    Enter your username: imvickykumar999
    Enter your password:
    Uploading vanks-0.0.1.tar.gz
    100%|█████████████████████████████████████████████████████████████| 4.12k/4.12k [00:02<00:00, 1.44kB/s]

    View at:
    https://pypi.org/project/vanks/0.0.1/

C:\Users\Vicky\Desktop\Repository\Basics-of-Python\Day 5 - pypi>
