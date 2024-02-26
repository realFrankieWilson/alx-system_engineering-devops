# Fixed the task 0 error by increasing the ulimit in the nginx default file.

exec { 'fix-default-file':
  command => 'sed -i "s/40906/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin',
}

# Restart Nginx
-> exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}