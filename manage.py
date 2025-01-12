#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Docker")

    from configurations import management

    # This allows easy placement of apps within the interior
    # stl_dsa directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "stl_dsa"))

    management.execute_from_command_line(sys.argv)
