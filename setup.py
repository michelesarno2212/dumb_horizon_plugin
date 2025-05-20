from setuptools import setup

setup(
    name='flat_plugin',
    version='0.0.1',
    packages=['.'],
    include_package_data=True,
    entry_points={
        'horizon.dashboard_panels': [
            'flat_plugin = panel'
        ],
    },
)
