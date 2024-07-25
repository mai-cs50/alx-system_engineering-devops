# practice using Puppet
file-line { 'ssh_password_authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => true,
  line    => 'PasswordAuthentication no',
  match   => '^PasswordAuthentication',

file-line {'ssh_identity_file':
  ensure => 'present',
  path   => '~/.ssh/config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^TdentityFile',
}
