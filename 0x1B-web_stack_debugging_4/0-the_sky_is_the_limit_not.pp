# Fixed the task 0 error by increasing the ulimit in the nginx default file.

exec { 'fix-default-file':
  command  => 'sudo sed -i "s/15/4096/g" /etc/default/nginx; sudo service nginx restart',
  provider => shell,
}
