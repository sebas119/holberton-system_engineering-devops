# Sky is the limit, let's bring that limit higher

exec { 'change':
  command  => 'sed -i "s/15/2000/g" /etc/default/nginx',
  provider => 'shell',
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
  require  => Exec['change'],
}
