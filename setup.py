import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="algofi-amm-py-sdk",
    description="Algofi AMM Python SDK",
    author="Algofi",
    author_email="founders@algofi.org",
    version="1.1.1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    project_urls={
        "Source": "https://github.com/Algofiorg/algofi-amm-py-sdk",
    },
    install_requires=["py-algorand-sdk >= 1.6.0"],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    include_package_data=True
)