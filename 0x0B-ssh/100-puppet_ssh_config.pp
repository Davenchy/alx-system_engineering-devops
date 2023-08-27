file { '/etc/ssh/ssh_config':
  content => template('ssh_config.erb'),
}

template { 'ssh_config.erb':
  source    => 'ssh_config.erb'
  variables => {
    host_54_165_85_96 => {
      'User'                   => 'ubuntu',
      'PasswordAuthentication' => 'no',
      'IdentityFile'           => '~/.ssh/school',
    }
  }
}
