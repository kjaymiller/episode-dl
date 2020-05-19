from setuptools import setup, find_packages

with open("README.md") as filename:
    long_description = filename.read()


setup(
        name='EpisodeDL',
        version='2020.5.1',
        description='EpisodeD(own)L(oader). Download Podcast Episodes with Ease'
        long_description=long_description,
        long_description_content_type='text/markdown',
        url='https://github.com/kjaymiller/episode_dl',
        author='Jay Miller',
        author_email='kjaymiller@gmail.com',
        license='MIT',
        packages=find_packages(),
        zip_safe=False,
        )
