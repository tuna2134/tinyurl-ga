import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()

packages = [
    "tinyurl_ga"
]

setuptools.setup(
    entry_points={
        "console_scripts": [
            "tinyurl-ga = tinyurl_ga:main"
        ]
    },
    packages=packages,
    name="tinyurl-ga",
    version="0.0.2",
    author="DMS",
    author_email="masato190411@gmail.com",
    description="This is tinyurl.ga wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuna2134/tinyurl-ga",
    install_requires=_requires_from_file('rqs.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
