import os
from xref_lambda_packages import lambda_packages
from nose.tools import assert_true

def test_packages():
    for name, package in lambda_packages.items():
        for runtime, details in package.items():
            package_file_name = os.path.split(details['path'])[1]

            assert_true(package_file_name.startswith(runtime + "-"))
            assert_true(os.path.exists(details['path']))