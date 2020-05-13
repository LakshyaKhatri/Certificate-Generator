from setuptools import setup
setup(
    name='certify',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'certify=main:main'
        ]
    }
)
