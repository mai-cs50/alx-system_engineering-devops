# practice using Puppet
file {'/etc/ssh/ssh_config':
	ensure  => 'present',
}

file_line {'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
  replace => 'true',
}

file_line {'ssh_identity_file':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^IdentityFile',
}
