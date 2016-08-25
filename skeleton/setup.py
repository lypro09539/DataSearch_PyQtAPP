try:
    from setuptools import setup
except Importerror:
    from distutils.core import setup

config = {
        'description':'My Project',
        'author':'Lypro09539',
        'url':'www.baidu.com',
        'download_url':'www.baidu.com',
        'author_email': '772907490@qq.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex46','bin'],
        'scripts': [],
        'name': 'ex46'

}

setup(**config)
