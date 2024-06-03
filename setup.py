import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="khmerpronounce",
    version="0.0.1",
    description="Khmer Pronounciation Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seanghay/khmerpronounce",
    author="Seanghay Yath",
    author_email="seanghay.dev@gmail.com",
    license="Apache License 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">3.5",
    packages=setuptools.find_packages(),
    package_dir={"khmerpronounce": "khmerpronounce"},
    package_data={
        "khmerpronounce": [
          "model.fst",
        ]
    },
    include_package_data=True,
    install_requires=[
        "sosap"
    ],
)