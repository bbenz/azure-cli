Debian Packaging
================

Updating the Debian package
---------------------------

Firstly, in `debian_dir_creator.sh`, modify debian/changelog with the new release information.
Create a PR for this change so it is tracked in the repo for next time.

Next, on a build machine (e.g. new Ubuntu 14.04 VM), run the build script.

For example:

First copy the build scripts onto the build machine.
```
$ > debian_build.sh; editor debian_build.sh
$ > debian_dir_creator.sh; editor debian_dir_creator.sh
$ chmod +x debian_build.sh debian_dir_creator.sh
```

Then execute it with the appropriate environment variable values.
```
$ export CLI_VERSION=0.2.1 \
    && export CLI_DOWNLOAD_SHA256=0cc8223baad64296c78537b92da27062af1d4a1baaaef55a21f9bdf2d17420be \
    && ~/debian_build.sh ~/debian_dir_creator.sh
```

Now you have built the package, upload the package to the apt repository.


Verification
------------

```
$ sudo dpkg -i azure-cli_${CLI_VERSION}-1_all.deb
$ az
$ az --version
```
