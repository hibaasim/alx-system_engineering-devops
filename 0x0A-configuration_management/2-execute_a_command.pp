# Manifest that kills a process named killmenow.

exec { 'killed':
  command => 'pkill killmenow',
  path    => '/usr/bin',
}
