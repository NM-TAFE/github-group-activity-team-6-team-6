from setuptools import setup, find_packages

setup(
    name='tic_tac_toe',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.3.3',
    ],
    entry_points={
        'console_scripts': [
            'tic-tac-toe=app:app.run',
        ],
    },
)
