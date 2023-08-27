class { 'ssh_config':
  client_options => {
    'Host 54.165.85.96' => {
      'User'                   => 'ubuntu',
      'PasswordAuthentication' => 'no',
      'IdentityFile'           => '~/.ssh/school',
    }
  }
}
