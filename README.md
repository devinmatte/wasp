wasp
======

[![Code Triagers Badge](https://www.codetriage.com/devinmatte/wasp/badges/users.svg)](https://www.codetriage.com/devinmatte/wasp)
[![first-timers-only](http://img.shields.io/badge/first--timers--only-friendly-blue.svg)](http://www.firsttimersonly.com/)

Wasp Generates and creates basic resources for a modern web app.
Initializes a project with a manifest, package, and helps you tag versions effectively.

Named wasp from the idea that wasps invented paper long before the first human thought to put his thoughts down on a sheet of papyrus.

Manifest
--------
Helps to generate a [web manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) for use in any modern web app. The goal being to make generating one easy, as a single command setup.
```
wasp init [-m --manifest]
```

Tagging
-------
Not currently implemented. Come back soon
```
wasp tag v1.0.5
```

Build
-----
To build the debian package, update the `changelog` and then run:
```
debuild -us -uc
```
