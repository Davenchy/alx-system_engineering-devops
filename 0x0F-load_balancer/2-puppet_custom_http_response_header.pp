# Setup Ubuntu server with NGINX Web Server

exec { 'apt update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

package { 'nginx':
  ensure => present,
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => "Hello World!\n",
}

exec { 'add X-Served-By header':
  command  => 'sed -i "42 a\ \tadd_header X-Served-By \$hostname;\n" /etc/nginx/sites-enabled/default',
  user     => 'root',
  provider => 'shell',
}

exec { 'restart nginx':
  command  => 'service nginx restart',
  user     => 'root',
  provider => 'shell',
}
