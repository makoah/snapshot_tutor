from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author="Marco K",
    author_email="marco.karmidi@gmail.com",
    summary="Making and monitoring snapshots AWS",
    packages=['shotty'],
    url="www.karmma.nl",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
