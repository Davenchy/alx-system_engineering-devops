# update ssh_config to authenticate ssh connection to server without password
file { '/etc/ssh/ssh_config':
  ensure  => present,
  content =>
    "${file('/etc/ssh/ssh_config')}

      Host 54.165.85.96
        User ubuntu
        PasswordAuthentication no
        IdentityFile ~/.ssh/school",
  owner   => 'root',
  group   => 'root',
  mode    => '0644'
}
