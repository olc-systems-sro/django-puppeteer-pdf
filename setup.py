from setuptools import setup, find_packages


setup(
    name='django-puppeteer-pdf',
    packages=find_packages(),
    include_package_data=True,
    version='0.1.4',
    description='Converts HTML to PDF using puppeteer.',
    long_description=open('README.rst').read(),
    license='BSD-2-Clause',
    author='Namespace',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-puppeteer-pdf',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    keywords='django puppeteer pdf',
)
