notify { "The value is: ${file('/etc/ssh/ssh_config')}": }
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
