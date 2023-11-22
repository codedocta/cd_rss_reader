from setuptools import setup, find_packages
from cd_rss_feed_reader.version import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cd_rss_reader",
    version=__version__,
    author="Code Docta",
    author_email="codedocta@gmail.com",
    description="The RSSReader is a Python utility for effortlessly fetching and parsing RSS and Atom feeds.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://codedocta.com',
    packages=find_packages(),
    install_requires=[
        'feedparser==6.0.10',
        'lxml==4.9.3',
        'sgmllib3k==1.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/codedocta/cd_rss_reader/issues',  # Replace with your issues URL
        'Source': 'https://github.com/codedocta/cd_rss_reader/',  # Replace with your repository URL
    },
)


