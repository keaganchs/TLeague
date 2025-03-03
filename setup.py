from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup


setup(
    name='TLeague',
    version='1.4',
    description='Tencent Distributed League for Multiagent Reinforcement Learning',
    keywords='League, SC2',
    packages=[
      'tleague',
    ],
    install_requires=[
      'gymnasium==1.1',
      'joblib',
      'numpy',
      'scipy',
      'pyzmq',
      'paramiko',
      'libtmux',
      'absl-py',
      'xlrd',
      'pyyaml',
      'psutil',
      'namedlist',
      "dm-tree", # For TF2 migration: https://github.com/tensorflow/tensorflow/issues/33748
    ],
    scripts=['tleague/bin/tleague_horovodrun']
)
