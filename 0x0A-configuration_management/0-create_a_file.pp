# create a file in /tmp

file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  groub   => 'www-data',
  require => File['/tmp'],
}

file { '/tmp':
  ensure  => directory,
}
