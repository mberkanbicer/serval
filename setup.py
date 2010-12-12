from setuptools import setup, find_packages

setup(
    name='serval',
    version='0.1',
    url='http://github.com/rspivak/serval',
    license='MIT',
    description='Simple Scheme interpreter in Python',
    author='Ruslan Spivak',
    author_email='ruslan.spivak@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    zip_safe=False,
    entry_points="""\
    [console_scripts]
    serval = serval.interpreter:main
    """
    )