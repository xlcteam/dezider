#!/usr/bin/env python
import os

from brutal.core.management import exec_overlord

if __name__ == "__main__":
    os.environ.setdefault("BRUTAL_CONFIG_MODULE", "dezider.config")
    exec_overlord("dezider.config")