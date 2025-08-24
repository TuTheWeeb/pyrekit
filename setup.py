from setuptools import setup, find_packages

setup(
    name='pyrekit',
    version='0.1.0',
    author='TuTheWeeb',
    author_email='eduardo.tuler@gmail.com',
    description='A toolkit to create react apps with python backend and includes pywebview to make desktop apps.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/TuTheWeeb/pyrekit',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'beautifulsoup4>=4.12.0',
        'Flask>=2.3.0',
        'Flask-Cors>=4.0.0',
        'watchdog>=3.0.0',
        'pywebview>=4.0.0',
        'requests',
    ],
    
    entry_points={
        'console_scripts': [
            'pyrekit = pyrekit.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)