# This script changes/increases the hardfile for the user "holberton"

exec { 'increases-hard-file-for-a-user':
  command  => 'sudo sed -i "s/holberton\shard.*/holberton\thard\tnofile\t10000/" /etc/security/limits.conf',
  provider => shell
}

# This script changes/increases the softfile for the user "holberton"
exec { 'increases-soft-file-for-a-user':
  command  => 'sudo sed -i "s/holberton\ssoft.*/holberton\tsoft\tnofile\t10000/" /etc/security/limits.conf',
  provider => shell
}