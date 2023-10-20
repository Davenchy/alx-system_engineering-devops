# this script increase the limit of nginx requests and restart the service

$file_path = '/etc/default/nginx'
$line = 'ULIMIT="-n 4096"'

exec { 'modify the nginx limit':
        provider => 'shell',
        command  => "sed -i 's/^ULIMIT=.*/${line}/' ${file_path}",
        unless   => "grep -q '^${line}\$' ${file_path}",
}

exec { 'restart nginx server':
        provider => 'shell',
        command  => 'sudo service nginx restart',
}
