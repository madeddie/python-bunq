from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('VERSION') as f:
    version = f.read().strip()

setup(
    name='bunq',
    version=version,
    description='Simple wrapper around the bunq API',
    long_description=readme,
    author='Edwin Hermans',
    author_email='edwin@madtech.cx',
    url='https://github.com/madeddie/python-bunq',
    license='MIT',
    install_requires=['requests', 'cryptography'],
    py_modules=['bunq']
)
