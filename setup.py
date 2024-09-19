from setuptools import setup, find_packages

setup(
    name='py-timeular',
    version='0.0.1',
    author="Conall O'Brien",
    author_email='conall@conall.net',
    description='A client library to the https://www.timeular.com API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/conallob/py-timeular',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests',  # Add other dependencies here
    ],
)
