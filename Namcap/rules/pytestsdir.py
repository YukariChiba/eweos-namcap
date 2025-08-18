# Copyright (C) 2025 Namcap contributors, see AUTHORS for details.
# SPDX-License-Identifier: GPL-2.0-or-later
"""
Test for whether a package installs a "tests" directory directly under Python's site-packages.

See https://gitlab.archlinux.org/pacman/namcap/-/issues/22
"""

from tarfile import TarFile

from Namcap.package import PacmanPackage
from Namcap.ruleclass import TarballRule


class PyTestsDirRule(TarballRule):
    name = "pytestsdir"
    description = "Verifies that the package doesn't install `python*/site-packages/tests`."

    def analyze(self, pkginfo: PacmanPackage, tar: TarFile) -> None:
        """Analyze package."""
        for entry in tar.getnames():
            if entry.startswith("usr/lib/python") and entry.endswith("site-packages/tests"):
                self.errors.append(
                    (
                        "python-tests-directory",
                        (),
                    )
                )
                break
