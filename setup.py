import os

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel("apistar_request_id.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


setup(
    name="apistar_request_id",
    version=version,
    description='Request id generation and propagation for API Star.',
    long_description="Visit https://github.com/Bogdanp/apistar_request_id for more information.",
    packages=[],
    py_modules=["apistar_request_id"],
    install_requires=["apistar>=0.4"],
    python_requires=">=3.5",
    include_package_data=True,
)
