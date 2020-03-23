from os import path

from setuptools import setup

REQUIREMENTS = ['pytest']

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'rb') as f:
    long_description = f.read().decode('utf8')

setup(
    name='pytest-tstcls',
    version='2020.1.1',
    py_modules=['tstcls'],
    provides=['tstcls'],
    description='Test Class Base',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Singular Labs, Inc",
    author_email='devs@singular.net',
    url='https://github.com/singular-labs/tstcls',
    keywords="pytest, test, class, base",
    install_requires=REQUIREMENTS,
    license="MIT License",
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
