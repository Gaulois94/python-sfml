#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pySFML2 - Cython SFML Wrapper for Python
# Copyright 2012, Jonathan De Wachter <dewachter.jonathan@gmail.com>
#
# This software is released under the GPLv3 license.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
from distutils.core import setup, Command
from distutils.extension import Extension

class Test(Command):
    user_options = []
    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        import sys, subprocess
        errno = subprocess.call([sys.executable, '-m',
                                 'unittest', 'discover', '-s', 'tests'])


if os.environ.get('USE_CYTHON'):
    import Cython.Distutils

    x11_source = 'src/sfml/x11.pyx'
    system_source = 'src/sfml/system.pyx'
    window_source = 'src/sfml/window.pyx'
    graphics_source = 'src/sfml/graphics.pyx'
    audio_source = 'src/sfml/audio.pyx'
    network_source = 'src/sfml/network.pyx'

else:
    x11_source = 'src/sfml/x11.cpp'
    system_source = 'src/sfml/system.cpp'
    window_source = 'src/sfml/window.cpp'
    graphics_source = 'src/sfml/graphics.cpp'
    audio_source = 'src/sfml/audio.cpp'
    network_source = 'src/sfml/network.cpp'

x11 = Extension('sfml.x11',
                [x11_source],
                ['include', 'src/sfml'],
                language='c++',
                libraries=['X11'])

system = Extension('sfml.system',
                    [system_source, 'src/sfml/error.cpp'],
                    ['include', 'src/sfml'],
                    language='c++',
                    libraries=['sfml-system', 'sfml-graphics'])

window = Extension('sfml.window',
                    [window_source, 'src/sfml/derivablewindow.cpp'],
                    ['include', 'src/sfml'],
                    language='c++',
                    libraries=['sfml-system', 'sfml-window'])

graphics = Extension('sfml.graphics',
                    [graphics_source, 'src/sfml/derivablerenderwindow.cpp', 'src/sfml/derivabledrawable.cpp'],
                    ['include', 'src/sfml'],
                    language='c++',
                    libraries=['sfml-system', 'sfml-window', 'sfml-graphics'])

audio = Extension('sfml.audio',
                    [audio_source, 'src/sfml/derivablesoundrecorder.cpp', 'src/sfml/derivablesoundstream.cpp'],
                    ['include', 'src/sfml'],
                    language='c++',
                    libraries=['sfml-system', 'sfml-audio'])

network = Extension('sfml.network',
                    [network_source],
                    ['include', 'src/sfml'],
                    language='c++',
                    libraries=['sfml-system', 'sfml-network'])

with open('README', 'r') as f:
    long_description = f.read()

kwargs = dict(
            name='pySFML2',
            ext_modules=[x11, system, window, graphics, audio, network],
            package_dir={'': 'src'},
            packages=['sfml'],
            version='1.2.0',
            description='The non-official Python binding for SFML2',
            long_description=long_description,
            author='Jonathan de Wachter, Edwin O Marshall'.decode('UTF-8'),
            author_email='dewachter.jonathan@gmail.com, emarshall85@gmail.com',
            url='http://openhelbreath.be/python-sfml2',
            license='LGPLv3',
            classifiers=['Development Status :: 5 - Production/Stable',
                        'Intended Audience :: Developers',
                        'License :: OSI Approved :: GNU General Public License v3 (LGPLv3)',
                        'Operating System :: OS Independent',
                        'Programming Language :: Cython',
                        'Topic :: Games/Entertainment',
                        'Topic :: Multimedia',
                        'Topic :: Software Development :: Libraries :: Python Modules'],
            cmdclass = {'test': Test})

if os.environ.get('USE_CYTHON')
    kwargs.update(cmdclass={'build_ext': Cython.Distutils.build_ext})

setup(**kwargs)
