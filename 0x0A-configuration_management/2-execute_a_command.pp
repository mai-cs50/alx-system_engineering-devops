# reate a manifest that kills a process named killmenow.

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => '/usr/bin:/bin',
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
  subscribe   => File['/tmp/killmenow_signal'],
}
file { '/tmp/killmenow_signal':
  ensure => file,
}
