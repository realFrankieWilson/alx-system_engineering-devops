# An automated way of fixing a 500 error code returned by apache server.
file { '/var/www/html/index.html':
  ensure  => file,
  content => '<p> Hello World!!! </p>',
}
