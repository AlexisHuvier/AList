from setuptools import setup, find_packages

import alist

setup(
    name="AList",
    version=alist.__version_num__,
    description="Anime/manga manager with other features",
    url="http://github.com/AlexisHuvier/AList",
    author="LavaPower",
    author_email="lavapower84@gmail.com",
    packages=find_packages(),
    install_requires=[
        "jikanpy",
        "Pillow",
        "googletrans~=3.1.0a0"
    ],
    entry_points={
        "console_scripts": [
            "alist = alist.AList:launch"
        ]
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: French',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ]
)