<img src="https://cloud.githubusercontent.com/assets/235208/14230584/449b1f4e-f92c-11e5-8075-9c7fe628eb28.png"/>

[![Build Status](https://travis-ci.org/barbosa/clorox.svg?branch=master)](https://travis-ci.org/barbosa/clorox)

## Motivation

```objc
//
// TableViewController.m
// MyProject
//
// Created by My Name on 3/13/16.
// Copyright (c) 2016 My Company. All rights reserved.
//
```

I've never liked this 8 lines above (7 coment lines + 1 blank one). It does nothing but just puts a lot of unuseful information in the beginning of your Objective-C/Swift files. If it is an open source project or if it is gonna be distributed, then yes, it makes sense to have it. Otherwise, it is just a waste of LOC. I'll tell you why, line by line:

Line      |    Explanation
----------|----------------
:one:     | Blank comment
:two:     | File name: static. Xcode **doesn't change it** if you rename the file
:three:   | Project name: static. Xcode **doesn't change it** if you rename the project
:four:    | Blank comment
:five:    | File's creator and date: It just says **who** created the file (even if that person never touches it again) and **when**. Both infos are easily fetched with a simple `git log` or a `git blame` (which would be much more valuable)
:six:     | Copyright, year and company: static. Xcode **doesn't update** the copyright with its current year. And also, it **does't update** the company name if changed (ok, maybe this is an uncommon case)
:seven:   | Blank comment
:eight:   | Blank line

*NOTE:* a few months ago I discovered that I was not the only one against it. [Jon Reid](http://qualitycoding.org/template-code-clutter/) wrote something about it.

## Installation

`clorox` was written in python :snake: and distributed via [pypi](pypi.python.org). As your MacOS already comes with python installed, you can easily install it using the command below:

```
$ sudo pip install clorox
```

## Usage

### Basic
:warning: WARNING: Make sure that your project is backed up through source control before doing anything.

In its basic usage, the command takes only one argument, which is the root path you want to run the cleaning:

```
$ clorox MyProject
```

The following screenshots show the execution output and the `diff` of some modified files:

<p align="center">
<img width="432" alt="clorox in action" src="https://cloud.githubusercontent.com/assets/235208/14130792/80017618-f603-11e5-8957-9897495c08b1.png">
<img width="432" alt="screen shot 2016-03-29 at 11 10 12 pm" src="https://cloud.githubusercontent.com/assets/235208/14130793/84385bd4-f603-11e5-83aa-ee335e5222e6.png">

</p>

If you are not comfortable running the command and want to see which files would be affected by its execution, simply add the option `--passive` or `-p`, like this:

```
$ clorox -p MyProject
```

## Author

Gustavo Barbosa. :octocat: [GitHub](https://github.com/barbosa) :bird: [Twitter](https://twitter.com/gustavocsb)

## License

This project is distributed under the [MIT License](https://raw.githubusercontent.com/barbosa/clorox/master/LICENSE.txt).
