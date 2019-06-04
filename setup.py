from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

setup(
    name="py3-bencode",
    version="0.0.3",
    description="Python 3 bencoding implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=["Programming Language :: Python"],
    keywords="bencode rawbytes torrent bittorrent",
    author="D.Bashkirtsevich",
    author_email="bashkirtsevich@gmail.com",
    url="https://github.com/bashkirtsevich-llc/py3bencode",
    license="GPL3 License",
    include_package_data=True,
    zip_safe=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires=">=3.6.*"
)
