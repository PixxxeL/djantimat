from distutils.core import setup
import djantimat

setup(
    name = "djantimat",
    version = djantimat.__version__,
    packages = ["djantimat"],
    url = 'https://github.com/PixxxeL/djantimat',
    author = 'pixel',
    author_email = 'ivan.n.sergeev@gmail.com',
    maintainer = 'pixel',
    maintainer_email = 'ivan.n.sergeev@gmail.com',
    license = 'MIT',
    description = 'Detect dirty slang in russian texts and process it',
    download_url = 'https://github.com/PixxxeL/djantimat/archive/master.zip',
    classifiers = [
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    include_package_data = True,
    install_requires = [
        'pymorphy2==0.8'
    ],
)
