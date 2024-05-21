from setuptools import setup, find_packages

setup(
      name='snipeit',
      version='1.2',
      description="Python library to access the SnipeIT API",
      install_requires=['requests','simplejson'],
      packages=find_packages(),
	include_package_data=True,
      zip_safe=False,
)
