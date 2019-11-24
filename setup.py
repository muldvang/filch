import setuptools

setuptools.setup(
    name="filch",
    version="0.0.1",
    author="Torben Muldvang Andersen",
    author_email="muldvang@gmail.com",
    description="An i3bar status generator",
    url="https://github.com/muldvang/filch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license='MIT',
    install_requires=[
        'netifaces',
        'pulsectl',
        'pyroute2',
        'pyudev',
        'six',
        'yappi'
    ],
    scripts=['bin/filch'],
)
