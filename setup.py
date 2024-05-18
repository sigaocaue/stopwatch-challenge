from setuptools import setup, find_packages

# Lê o conteúdo do README.md para a descrição longa
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="stopwatch-cli",
    version="0.0.1",
    author="Cauê Prado",
    description="Um cronômetro simples para rodar no terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sigaocaue/stopwatch-challenge",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
    ],
    entry_points={
        'console_scripts': [
            'stopwatch=stopwatch.stopwatch:cli',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
