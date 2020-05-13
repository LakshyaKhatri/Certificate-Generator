import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='certify',
    version='0.0.1',
    author='Lakshya Khatri',
    author_email='lakshyak67@gmail.com',
    description="A Certificate Generator",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LakshyaKhatri/Certify',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'certify=main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Development Status :: 1 - Planning',
        'Topic :: Education :: Testing'
    ],
    python_requires='>=3.0',
)
