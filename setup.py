from setuptools import setup

setup(
    name='too_many_repos',
    description='A pygments lexer for pytest output.',
    url='https://github.com/locknic/too-many-repos',
    version='0.0.1',
    author='Dominic Mortlock',
    author_email='dom.mortlock@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
    install_requires=['mypy', 'gitpython', 'pre-commit'],
)
