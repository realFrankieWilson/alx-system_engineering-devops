# An automated way of fixing a 500 error code returned by apache server.
file { 'fixedType':
  command  => 'sudo mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-local.php',
  provider => shell,
}
