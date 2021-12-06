"""
WSGI config for A_Registro_Maquinas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# add python site packages, you can use virtualenvs also
site.addsitedir("C:/Users/karla.amezcua/AppData/Local/Programs/Python/Python39/lib/site-packages/")

# Add the app's directory to the PYTHONPATH 
sys.path.append('C:/Registro_Maquinas/A_Registro_Maquinas') 
sys.path.append('C:/Registro_Maquinas/A_Registro_Maquinas/A_Registro_Maquinas')  

os.environ['DJANGO_SETTINGS_MODULE'] = 'A_Registro_Maquinas.settings' 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A_Registro_Maquinas.settings')  
 
application = get_wsgi_application()