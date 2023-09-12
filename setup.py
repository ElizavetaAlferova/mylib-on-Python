from setuptools import setup, find_packages
setup(name='shapes',
      version='0.1',
      url='https://github.com/ElizavetaAlferova/mylib-on-Python',
      license='MIT',
      author='Elizaveta Ilicheva',
      author_email='alferovaem.work@gmail.com',
      description='Manage configuration files',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)