from setuptools import setup, find_packages

setup(
    name="dl_kep",
    version="0.0.1",
    description="download keler data",
    url="http://github.com/jpdeleon/dl_kep",
    author="Jerome de Leon",
    author_email="jpdeleon.bsap@gmail.com",
    license="MIT",
    # packages=["dl_kep"],  # or find_packages(),
    # package_data={"chronos": "data"},
    include_package_data=True,
    scripts=[
        "scripts/dl_kep",
    ],
    zip_safe=False,
    install_requires=[
        "lightkurve",
    ],
)
