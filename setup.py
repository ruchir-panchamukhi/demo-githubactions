from setuptools import setup, find_packages

setup(
    name='demo-package',  # Your package name
    version='0.1.0',  # Package version
    author='Ruchir',  # Your name
    author_email='ruchir.panchamukhi@Triconinfotech.com',  # Your email
    description='A simple example package',  # Short description
    long_description=open('README.md').read(),  # Long description
    long_description_content_type='text/markdown',
    url='https://github.com/ruchir-panchamukhi/demo-githubactions.git',  # Repo URL
    packages=find_packages(),  # Automatically find packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Supported Python versions
)
