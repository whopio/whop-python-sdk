from setuptools import setup, find_packages

setup(
    name='whop',
    version='3.0',
    license='MIT',
    author="Whop",
    author_email='support@whop.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/whopio/whop-python-sdk',
    keywords='whop',
    install_requires=[
          'python_dateutil >= 2.5.3',
          'setuptools >= 21.0.0',
          'urllib3 >= 1.25.3',
      ]
)
