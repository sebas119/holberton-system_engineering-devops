exec { 'change':
  command  => 'sed -i "s/15/4096/g" /etc/default/nginx',
  provider => 'shell',
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
  require  => Exec['change'],
}
