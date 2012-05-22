from setuptools import setup, find_packages
setup(
    name = "langid",
    version = "0.1",
    py_modules = ['langid'],
    scripts = ['langid.py'],
    install_requires = ['numpy']
)
