#!/usr/bin/env python3
#
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import distutils.util
import io

import setuptools

with open("VERSION") as f:
    version = f.read().strip()
with open("README.md") as f:
    # Force UTF-8 file encoding to support non-ascii characters in the readme.
    with io.open("README.md", encoding="utf-8") as f:
        long_description = f.read()
with open("noptimizer/requirements.txt") as f:
    requirements = [ln.split("#")[0].rstrip() for ln in f.readlines()]

# When building a bdist_wheel we need to set the appropriate tags: this package
# includes compiled binaries, and does not include compiled python extensions.
try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

    class bdist_wheel(_bdist_wheel):
        def finalize_options(self):
            _bdist_wheel.finalize_options(self)
            self.root_is_pure = False

        def get_tag(self):
            python, abi, plat = _bdist_wheel.get_tag(self)
            python, abi = "py3", "none"
            return python, abi, plat


except ImportError:
    bdist_wheel = None

setuptools.setup(
    name="noptimizer",
    version=version,
    description="NOPtimizer",
    author="KKimJ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KKimj/NOPtimizer",
    license="MIT",
    packages=[
        "noptimizer",
    ],
    
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.6",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Compilers",
    ],
    cmdclass={"bdist_wheel": bdist_wheel},
    platforms=[distutils.util.get_platform()],
    zip_safe=False,
)