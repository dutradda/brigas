
import shutil

from distutils.core import setup


long_description = """
UPnP Game Server 0.1 implementation. Allows users to play games over UPnP
with almost zero-configuration.
"""
version = '0.1'


def main():
    setup(
        name='python-brisa-game-server',
        version=version,
        description='BRisa Game Server',
        long_description=long_description,
        author='BRiGaS team',
        author_email='brisas-team@launchpad.net',
        url='http://launchpad.net/brigas',
        download_url='http://launchpad.net/brigas',
        license='none',
        maintainer='Diogo Dutra Albuquerque',
        maintainer_email='diogo.comp@gmail.com',
        platforms='any',
        scripts=['bin/brisa-game-server'],
        keywords=['UPnP', 'Game Server', 'Gaming', 'Game'],
        package_dir = {'brisa_game_server': 'src',
                       'brisa_game_server/services': 'src/services',
                       'brisa_game_server/services/game_manager':
                       'src/services/game_manager',
                       'brisa_game_server/games': 'src/games',
                       'brisa_game_server/services/xmls':
                       'src/services/xmls'},
        packages=['brisa_game_server',
                  'brisa_game_server/services',
                  'brisa_game_server/services/game_manager',
                  'brisa_game_server/games',
                  'brisa_game_server/services/xmls'],
        package_data={'brisa_game_server/services/xmls': ['*.xml']},
        classifiers=['Development Status :: 3 - Alpha',
                     'Environment :: Other Environment',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Servers',
                     'Natural Language :: English',
                     'Operating System :: Linux',
                     'Programming Language :: Python',
                     'Topic :: Games'])

if __name__ == "__main__":
    main()
