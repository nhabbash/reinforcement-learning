from setuptools import setup, find_packages

setup(name='gym_bandits',
      description='K-armed Bandit Environment',
      packages=find_packages(),
      version='0.0.1',
      install_requires=['gym']
)