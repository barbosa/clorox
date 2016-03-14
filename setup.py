from distutils.core import setup

VERSION = '0.1'

setup(
  name = 'clorox',
  packages = ['clorox'],
  version = VERSION,
  description = "Removes Xcode's file comment blocks cruft",
  author = 'Gustavo Barbosa',
  author_email = 'gustavocsb@gmail.com',
  url = 'https://github.com/barbosa/clorox',
  download_url = 'https://github.com/barbosa/clorox/tarball/%s' % VERSION,
  keywords = ['xcode', 'objective-c', 'swift', 'ios', 'macos'],
  classifiers = [],
)
