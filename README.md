<img src="https://cloud.githubusercontent.com/assets/235208/14230584/449b1f4e-f92c-11e5-8075-9c7fe628eb28.png"/>

# Clorox
[![Build Status](https://travis-ci.org/barbosa/clorox.svg?branch=master)](https://travis-ci.org/barbosa/clorox)

Removes Xcode's file comment blocks cruft.

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

1. Blank comment;
2. File name: static. Xcode **doesn't change it** if you rename the file;
3. Project name: static. Xcode **doesn't change it** if you rename the project;
4. Blank comment;
5. File's creator and date: It just says **who** created the file (even if that person never touches it again) and **when**. Both infos are easily fetched with a simple `git log` or a `git blame` (which would be much more valuable);
6. Copyright, year and company: static. Xcode **doesn't update** the copyright with its current year. And also, it **does't update** the company name if changed (ok, maybe this is an uncommon case);
7. Blank comment;
8. Blank line.

*NOTE:* a few months ago I discovered that I was not the only one against it. [Jon Reid](http://qualitycoding.org/template-code-clutter/) wrote something about it.

## Installation

```
$ sudo pip install clorox
```

## Usage

### Basic
:warning: WARNING: Make sure that your project is backed up through source control before doing anything.

```
$ clorox MyProject
```

<p align="center">
<img width="432" alt="clorox in action" src="https://cloud.githubusercontent.com/assets/235208/14130792/80017618-f603-11e5-8957-9897495c08b1.png">
<img width="432" alt="screen shot 2016-03-29 at 11 10 12 pm" src="https://cloud.githubusercontent.com/assets/235208/14130793/84385bd4-f603-11e5-83aa-ee335e5222e6.png">

</p>


### Advanced

```
Usage:
    clorox [OPTIONS] [PATH]

Parameters:
    path                Path to run clorox

Options:
    --passive, -p       prints the output without running the script
    --help, -h          prints this help message
```

## Author

Gustavo Barbosa

## License

This project is under the [MIT License](https://raw.githubusercontent.com/barbosa/clorox/master/LICENSE.txt).
