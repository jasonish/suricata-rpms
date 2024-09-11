#! /usr/bin/env python

import sys
import os

from datetime import datetime

def main():
    try:
        version = sys.argv[1]
    except:
        print("usage: $0 <new-version>", file=sys.stderr)
        return 1
    print("Updating to Suricata {}".format(version))

    state = ""
    spec = []
    with open("suricata.spec") as spec_in:
        for line in spec_in:
            if line.startswith("Version:"):
                spec.append("Version: {}".format(version))
            elif line.startswith("Release:"):
                # Reset release to 1.
                spec.append("Release: 1%{?dist}")
            elif line.startswith("%changelog"):
                spec.append(line.strip("\n"))
                state = "%changelog"
            elif state == "%changelog":
                state = ""
                if line.find(version) < 0:
                    dt = datetime.now()
                    spec.append("* {} Jason Ish <jish@oisf.net> - 1:{}-1".format(
                        dt.strftime("%a %b %d %Y"), version))
                    spec.append("- Update to Suricata {}".format(version))
                    spec.append("")
                spec.append(line.strip("\n"))
            else:
                spec.append(line.strip("\n"))

    with open("suricata.spec", "w") as spec_out:
        spec_out.write("\n".join(spec))
        spec_out.write("\n")

    print("""
Now run:
    make update-sources

And then push a test build:
    make copr-testing
""")

if __name__ == "__main__":
    sys.exit(main())
