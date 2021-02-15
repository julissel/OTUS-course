import os
from setuptools import setup, find_packages
with open(os.path.join(os.path.dirname(__file__), "README.md")) as read_me_file:
    read_me_description = read_me_file.read()

setup(
    name="consolesearcher",
    version="0.1",
    license='GNU General Public License v3.0',
    author="julissel",
    author_email="julissel@yandex.ru",
    description="This is a simple search engine program",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/julissel/consolesearcher",
    packages=find_packages(),
    include_package_data=True,
    keywords=["console", "search"],
    classifiers=[],
    entry_points={
        "console_scripts": [
            "consolesearcher = consolesearcher.__main__:main",
        ]
    },
    python_requires=">=3.8",
    install_requires=["dicttoxml", "requests", "bs4", "selenium"],
)
