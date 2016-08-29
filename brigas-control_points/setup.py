
import shutil

from distutils.core import setup


long_description = """
Control Point for the BRisa Game Server. Allows users to play games over UPnP
with almost zero-configuration.
"""
version = '0.1'


def main():
    setup(
        name='python-brigas-control-point',
        version=version,
        description='BRiGaS Control Point',
        long_description=long_description,
        author='BRiGaS team',
        author_email='brisas-team@launchpad.net',
        url='http://launchpad.net/brigas',
        download_url='http://launchpad.net/brigas',
        license='none',
        maintainer='Diogo Dutra Albuquerque',
        maintainer_email='diogo.comp@gmail.com',
        platforms='any',
        scripts=['bin/brigas-cp_test'],
        keywords=['UPnP', 'Game Server', 'Gaming', 'Game'],
        package_dir = {'brisa_game_server/control_points': 'src',
                       'brisa_game_server/control_points/game_manager':
		       'src/game_manager'},
        packages=['brisa_game_server/control_points',
                  'brisa_game_server/control_points/game_manager'],
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
