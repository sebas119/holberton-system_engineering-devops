# Config Nginx and added a header
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

file_line { 'customHeader':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => ':80 default_server;',
  line    => "add_header X-Served-By ${hostname};",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => true,
  require => File_line['customHeader'],
}
