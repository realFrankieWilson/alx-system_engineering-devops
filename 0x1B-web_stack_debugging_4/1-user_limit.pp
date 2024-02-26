# This script changes/increases the hardfile for the user "holberton"

exec { 'increases-hard-file-for-a-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:bin/'
}

# This script changes/increases the softfile for the user "holberton"

exec { 'increases-hard-file-for-a-user':
  command => 'sed -i "/holberton soft/s/4/40000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:bin/'
}
