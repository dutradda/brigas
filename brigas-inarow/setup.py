
import shutil

from distutils.core import setup


long_description = """
A UPnP 4 in a row game using BRiGaS.
"""
version = '0.1'


def main():
    setup(
        name='python-brigas-4inarow',
        version=version,
        description='UPnP 4 in a row game',
        long_description=long_description,
        author='Diogo Dutra',
        author_email='diogo.comp@gmail.com',
        url='http://launchpad.net/brigas',
        download_url='http://launchpad.net/brigas',
        license='none',
        maintainer='Diogo Dutra Albuquerque',
        maintainer_email='diogo.comp@gmail.com',
        platforms='Linux',
        keywords=['UPnP', 'Game Server', 'Gaming', 'Game', '4 in a row'],
        package_dir = {'brisa_game_server/games/inarow': 'src'},
        packages=['brisa_game_server/games/inarow'],
        package_data={'brisa_game_server/games/inarow': ['*.xml']},
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
