<div align="center">

![wasp](wasp.png)

wasp
======

[![Current Release](https://img.shields.io/github/release/devinmatte/wasp.svg)](https://github.com/devinmatte/wasp/releases)
[![Open Issues](https://img.shields.io/github/issues-raw/devinmatte/wasp.svg)](https://github.com/devinmatte/wasp/issues)
[![Contributors](https://img.shields.io/github/contributors/devinmatte/wasp.svg)](https://github.com/devinmatte/wasp/graphs/contributors)


[![Code Triagers Badge](https://www.codetriage.com/devinmatte/wasp/badges/users.svg)](https://www.codetriage.com/devinmatte/wasp)
[![first-timers-only](http://img.shields.io/badge/first--timers--only-friendly-blue.svg)](http://www.firsttimersonly.com/)

wasp generates and creates basic resources for a modern web app.
Initializes a project with a manifest, package, and helps you tag versions effectively.

Named wasp from the idea that wasps invented paper long before the first human thought to put his thoughts down on a sheet of papyrus.

</div>

Manifest
--------
Helps to generate a [web manifest](https://developer.mozilla.org/en-US/docs/Web/Manifest) for use in any modern web app. The goal being to make generating one easy, as a single command setup.
```bash
wasp init [-m --manifest]
```

Package
--------
Helps to generate a [package.json](https://docs.npmjs.com/files/package.json) for NPM or other tools that use this configuration. It creates a `package.json` to the NPM spec.
```bash
wasp init [-p --package]
```

Tagging
-------
Not currently implemented. Come back in a few versions
```bash
wasp tag v1.0.5
```

Build
-----
To build for Debian:

First, update the `changelog`:
```bash
dch -i
```

To Build, run:
```bash
debuild -us -uc
```

Design
------

Right now there's no format design pattern in use. The current goal is to get a functioning tool.
I would like to follow a formally defined design pattern, but until I determine one, this is the current design.
