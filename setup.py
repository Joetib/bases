
import io
import re
from setuptools import setup


with io.open('bases/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='bases',
    version=version,
    description='A Python Implementation to convert from one base to another',
    long_description=long_description,
    author='Oti Boateng Joseph',
    author_email='otiboatenjoe@gmail.com',
    url='https://github.com/Joetib/bases',
    packages= ['bases'],
    license='MIT',
    classifiers=[
        'Development Status :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Mathematics',
        'Topic :: Software Development :: Number bases',
    ],
    
)