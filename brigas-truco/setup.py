
import shutil

from distutils.core import setup


long_description = """
UPnP Game Server Truco extention. Allows users to play the Truco game over UPnP
with almost zero-configuration.
"""
version = '0.1'


def main():
    setup(
        name='python-brigas-truco',
        version=version,
        description='BRiGaS Truco',
        long_description=long_description,
        author='BRiGaS team',
        author_email='brisas-team@launchpad.net',
        url='http://launchpad.net/brigas',
        download_url='http://launchpad.net/brigas',
        license='none',
        maintainer='Diogo Dutra Albuquerque',
        maintainer_email='diogo.comp@gmail.com',
        platforms='any',
        keywords=['UPnP', 'Game Server', 'Gaming', 'Game', 'Truco'],
        package_dir = {'brisa_game_server/games/truco': 'src'},
        packages=['brisa_game_server/games/truco'],
        package_data={'brisa_game_server/games/truco': ['*.xml']},
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
