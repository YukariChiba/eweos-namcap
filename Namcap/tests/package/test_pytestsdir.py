# Copyright (C) 2003-2025 Namcap contributors, see AUTHORS for details.
# SPDX-License-Identifier: GPL-2.0-or-later
"""
Tests for the python-tests-directory rule.
"""

import os

import Namcap.rules.pytestsdir
from Namcap.tests.makepkg import MakepkgTest


class PyTestsDirTest(MakepkgTest):
    pkgbuild = """
pkgname=__namcap_test_pytestsdir
pkgver=1.0
pkgrel=1
pkgdesc="A package"
arch=('any')
url="http://www.example.com/"
license=('GPL-2.0-or-later')
depends=('python')
source=()
build() {
  touch "${srcdir}/init.py"
}
package() {
  install -D -m 644 "${srcdir}/init.py" "${pkgdir}/usr/lib/pythonX.Y/site-packages/tests/__init__.py"
}
"""

    def test_pytestsdir(self):
        """Package with tests directory in Python site-packages."""
        pkgfile = "__namcap_test_pytestsdir-1.0-1-any.pkg.tar"
        with open(os.path.join(self.tmpdir, "PKGBUILD"), "w") as f:
            f.write(self.pkgbuild)
        self.run_makepkg()
        pkg, r = self.run_rule_on_tarball(os.path.join(self.tmpdir, pkgfile), Namcap.rules.pytestsdir.PyTestsDirRule)
        self.assertEqual(
            r.errors,
            [
                (
                    "python-tests-directory",
                    (),
                ),
            ],
        )
        self.assertEqual(r.warnings, [])
        self.assertEqual(r.infos, [])
