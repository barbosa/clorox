<img src="https://cloud.githubusercontent.com/assets/235208/14230584/449b1f4e-f92c-11e5-8075-9c7fe628eb28.png"/>

[![Build Status](https://travis-ci.org/barbosa/clorox.svg?branch=master)](https://travis-ci.org/barbosa/clorox)
[![PyPI Version](https://img.shields.io/pypi/v/clorox.svg)](https://pypi.python.org/pypi/clorox)
[![Dependency Status](https://gemnasium.com/barbosa/clorox.svg)](https://gemnasium.com/barbosa/clorox)

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

I've never liked these 8 lines above (7 comment lines + 1 blank one). It does nothing but puts a lot of unuseful information in the beginning of your Objective-C/Swift files. If it is an open source project or if it is gonna be distributed, then ok, it makes sense to have it. Otherwise, it's just a waste of LOC. I'll tell you why, line by line:

Line      |    Explanation
----------|----------------
:one:     | Blank comment
:two:     | File name: static. Xcode **does not change it** if you rename the file
:three:   | Project name: static. Xcode **does not change it** if you rename the project
:four:    | Blank comment
:five:    | File's creator and date: It just says **who** created the file (even if that person never touches it again) and **when**. Both infos are easily fetched with a simple `git log` or a `git blame` (which would be much more valuable)
:six:     | Copyright, year and company: static. Xcode **does not update** the copyright with its current year. And also, it **does not update** the company name if changed (ok, maybe this is an uncommon case)
:seven:   | Blank comment
:eight:   | Blank line


## Installation

`clorox` was written in python :snake: and distributed via [pypi](pypi.python.org). As your MacOS already comes with python installed, you can easily install it using the command below:

```
sudo pip install clorox
```

## Usage

:warning: WARNING: Make sure that your project is backed up through source control before doing anything.

In its basic usage, the command takes only one argument, which is the root path you want to run the cleaning:

```
clorox --path MyProject
```

The following screenshots show the execution output and the `diff` of some modified files:

<p align="center">
<img width="432" alt="clorox in action" src="https://cloud.githubusercontent.com/assets/235208/14130792/80017618-f603-11e5-8957-9897495c08b1.png">
<img width="432" alt="screen shot 2016-03-29 at 11 10 12 pm" src="https://cloud.githubusercontent.com/assets/235208/14130793/84385bd4-f603-11e5-83aa-ee335e5222e6.png">

</p>

If you are not comfortable running the command and want to see which files would be affected by its execution, simply add the option `--inspection` or `-i`, like this:

```
clorox --path MyProject --inspection
```

## Note

`clorox` only removes already existent file comment headers from existent source files. So it is useful when you have a project with a bunch of files and then decide to get rid of them all. For new files, Xcode will still add the cruft. To change that, you need to modify the file templates you want.

First, check which templates you have installed under your Xcode directory:

```
ls -al /Applications/Xcode.app/Contents/Developer/Library/Xcode/Templates/File\ Templates/Source/
```

It should print something like:

```
drwxr-xr-x  15 root  wheel  510 Mar 15 18:56 .
drwxr-xr-x   7 root  wheel  238 Mar 15 20:19 ..
drwxr-xr-x   7 root  wheel  238 Mar 15 18:56 C File.xctemplate
drwxr-xr-x   7 root  wheel  238 Mar 15 18:56 C++ File.xctemplate
drwxr-xr-x  21 root  wheel  714 Mar 15 18:56 Cocoa Class.xctemplate
drwxr-xr-x   6 root  wheel  204 Mar 15 18:56 Header File.xctemplate
drwxr-xr-x   9 root  wheel  306 Mar 15 18:56 Objective-C File.xctemplate
drwxr-xr-x   5 root  wheel  170 Mar 15 18:56 Objective-C new superclass.xctemplate
drwxr-xr-x   4 root  wheel  136 Mar 15 18:56 Playground Page.xctemplate
drwxr-xr-x   8 root  wheel  272 Mar 15 20:40 Playground with Platform Choice.xctemplate
drwxr-xr-x   6 root  wheel  204 Mar 15 20:40 Playground.xctemplate
drwxr-xr-x   4 root  wheel  136 Mar 15 18:56 Sources Folder Swift File.xctemplate
drwxr-xr-x   6 root  wheel  204 Mar 15 18:56 Swift File.xctemplate
drwxr-xr-x   7 root  wheel  238 Mar 15 18:56 UI Test Case Class.xctemplate
drwxr-xr-x   7 root  wheel  238 Mar 15 18:56 Unit Test Case Class.xctemplate
```

Then look for files named `___FILEBASENAME___.*` inside the folder you want and clean its content.

## Acknowlegdements

- [@jonreid](https://github.com/jonreid) for sharing the same thoughts and [blogging](http://qualitycoding.org/template-code-clutter/) about it
- [@gabrielfalcao](https://github.com/gabrielfalcao) for creating [couleur](https://github.com/gabrielfalcao/couleur) and making my life easier using these fancy colored outputs
- [@marcelofabri](https://github.com/marcelofabri) for writing a [motivating article](http://equinocios.com/open-source/2016/03/01/o-mundo-e-mais-que-seu-umbigo/) on how to contribute to the open source initiative [pt-BR]

## Author

Gustavo Barbosa. :octocat: [GitHub](https://github.com/barbosa) :bird: [Twitter](https://twitter.com/gustavocsb)

## License

This project is distributed under the [MIT License](https://raw.githubusercontent.com/barbosa/clorox/master/LICENSE.txt).
