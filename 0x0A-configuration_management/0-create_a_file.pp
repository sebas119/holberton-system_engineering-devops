# Create a new file with specific permissions:
    file {'holberton':
      ensure  =>  present,
      path    =>  '/tmp/holberton',
      owner   =>  'www-data',
      group   =>  'www-data',
      mode    =>  '0744',
      content =>  'I love Puppet'
    }
