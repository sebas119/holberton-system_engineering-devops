# Install puppet-lint package with provider gem:
    package {'puppet-lint':
      ensure   =>  '2.1.1',
      name     =>  'puppet-lint',
      provider =>  'gem'
    }
