# Install and configure Nginx
exec { 'update_ppa':
  command  => 'sudo apt-get update',
  provider => shell,
}

package { 'Install nginx':
  ensure   => installed,
  name     => 'nginx',
  provider => apt,
  require  => Exec['update_ppa'],
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  path    => '/var/www/html/index.html'
}

service { 'nginx':
  ensure  => true,
  require => Package['Install nginx'],
}
