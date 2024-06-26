#
# Copyright (c) 2024 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_google_business_information import SourceGoogleBusinessInformation

if __name__ == "__main__":
    source = SourceGoogleBusinessInformation()
    launch(source, sys.argv[1:])
