import shutil
from pathlib import Path

from setuptools import setup, find_packages

if Path.is_dir(Path('build')):
    print("Cleaning up previous build..")
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("dvtTestKit.egg-info", ignore_errors=True)

with open("docs/README.md", "r") as fh:
    long_description = fh.read()


def bump_version():
    """
    Reads the current version number from a file called `version.txt`, increments the patch version number by 1, and writes the new version back to the file. If the file doesn't exist, it is created with a default version of `v0.0.1`.

    Returns:
        str: The new version string.
    """
    try:
        with open('version.txt', 'r') as f:
            current_version = f.read().strip()
    except FileNotFoundError:
        # If the file doesn't exist, create it with a default version
        current_version = 'v0.0.1'
        with open('version.txt', 'w') as f:
            f.write(current_version)

    # Strip off any leading 'v' character before parsing the version
    current_version = current_version.lstrip('v')
    version_parts = current_version.split('.')
    major = int(version_parts[0])
    minor = int(version_parts[1])
    patch = int(version_parts[2])

    # Increment the version by 1
    patch += 1

    # Construct the new version string
    new_version = f'v{major}.{minor}.{patch}'

    # Write the new version back to the file
    with open('version.txt', 'w') as f:
        f.write(new_version)

    # Return the new version
    return str(new_version)


setup(
    name='dvtTestKit',
    version=bump_version(),
    description='Toolkit for Minim DVT department',
    long_description="long_description",
    long_description_content_type="text/markdown",
    author='Dan.Edens',
    author_email='Dane@minim.comm',
    url='https://github.com/DanEdens/dvt_tk.git',
    packages=find_packages(exclude=("docs","dist", "data", "build", ".run")),
    scripts=['bin/dvtTestKit.cmd', 'bin/post.cmd'],
    script_args=["bdist_wheel"],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'dvttestkit=dvtTestKit.testKitUtils:main'
        ],
    },
    install_requires=[
        "paho-mqtt",
        "slack_sdk",
        "jira",
        "pyshorteners",
        "pexpect",
        "netmiko",
        "requests",
        "bs4",
        # "shpinx", add to build requires TODO
        # "sphinxcontrib.confluencebuilder",
    ],
    python_requires='>=3.10'
)
