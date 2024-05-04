# practice using Puppet
file-line { 'ssh_password_authentication':
  ensure  => 'present',
  path    => '/etc/ssh/sshd_config',
  replace => true,
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
}
file-line {'ssh_identity_file':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
}
