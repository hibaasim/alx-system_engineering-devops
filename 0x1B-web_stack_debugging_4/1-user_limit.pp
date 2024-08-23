# Configure soft and hard limis to 5000

exec { 'increase-hard':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

exec { 'increase-soft':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
