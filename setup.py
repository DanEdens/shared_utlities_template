import shutil
from pathlib import Path

from setuptools import setup, find_packages

# Delete previous build files to prevent removed files from remaining
if Path.is_dir(Path('build')):
    print("Cleaning up previous build..")
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("MinimTestKit.egg-info", ignore_errors=True)


with open("MinimTestKit/docs/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='MinimTestKit',
    version='0.0.0.1',
    description='Minim Device Automator and Testing toolKit',
    long_description="long_description",
    long_description_content_type="markdown",
    author='Dan.Edens',
    author_email='dane@minim.com',
    url='ssh://git-codecommit.us-east-2.amazonaws.com/v1/repos/_MinimTestKit',
    packages=find_packages(),
    scripts=['MinimTestKit/bin/testkit.cmd'],
    script_args=["bdist_wheel"],
    license='',
    keywords=["Minim"],
    include_package_data=True,
    package_data={
        "": ["*.cmd", "*.md", "*.ini", "*.png",
             "*.jpg", "*.json", "*.url", "*.zip"]
        },
    setup_requires=[
        ],
    install_requires=[
        ],
    python_requires='>=3.10'
    )
