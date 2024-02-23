# install flask from pip3
exec { 'puppt-lint':
  command => '/usr/bin/apt-get -y install puppt-lint -v 2.5.0',
}
