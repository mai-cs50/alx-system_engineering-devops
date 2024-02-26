# practice using Puppet
file-line { 'replace passwordAuthentication':
  ensure  => 'present',
  path    => '/etc/ssh/sshd_config',
  replace => true,
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
}
file-line {'add the private key ~/.ssh/school':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
