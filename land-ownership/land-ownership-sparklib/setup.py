from setuptools import setup

setup(name='landownership-sparklib',
      version='0.0.1',
      description='pyspark app to process hierarchical landownershipdata',
      url='https://github.com/VarunBhandary/technical-challenge',
      author='Varun Bhandary',
      author_email='varun.bhandary@gmail.com,
      packages=['pipelines', 'pipelines.utils', 'pipelines.jobs'],
      zip_safe=False)
