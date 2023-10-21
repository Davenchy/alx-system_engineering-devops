# increase the number of opened files limit for holberton user

$file = '/etc/security/limits.conf'
$user = 'holberton'

exec { 'Increase soft number of files limit':
        provider => 'shell',
        command  => "sed -i 's/^${user} soft nofile.*\$/${user} soft nofile 4096/' ${file}",
}

exec { 'Increase hard number of files limit':
        provider => 'shell',
        command  => "sed -i 's/^${user} hard nofile.*\$/${user} hard nofile 4096/' ${file}",
}

exec { 'reload limits':
        provider => 'shell',
        command  => 'sudo sysctl -p',
}
