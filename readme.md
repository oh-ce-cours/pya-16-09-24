# Télécharger des paquets pour les installer hors ligne 

https://stackoverflow.com/questions/11091623/how-to-install-packages-offline


##On the system that has access to internet

The pip download command lets you download packages without installing them:

`pip download -r requirements.txt`

(In previous versions of pip, this was spelled pip install --download -r requirements.txt.)

##On the system that has no access to internet

Copy over the downloaded packages to this system and then you can use

`pip install --no-index --find-links /path/to/download/dir/ -r requirements.txt`

to install those downloaded modules, without accessing the network.


# Manipulation des fstrings 

https://fstring.help/cheat/
