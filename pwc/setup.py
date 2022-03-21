from setuptools import find_packages, setup

setup(
    name='Grocery',
    packages=find_packages(include=['Grocery']),
    version='0.1.0',
    description='grocery store manager',
    author='Neetash',
    license='PWC',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)