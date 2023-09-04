# Setup Ubuntu server with NGINX Web Server

exec { 'apt update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => "Hello World!\n",
}

file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n\'est pas une page\n",
}

exec { 'configure nginx redirection':
  command  => 'sed -i "42 a\ \tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}\n" /etc/nginx/sites-enabled/default',
  user     => 'root',
  provider => 'shell',
}

exec { 'configure custom 404 error page':
  command  => 'sed -i "42 a\ \terror_page 404 /404.html;\n" /etc/nginx/sites-enabled/default',
  user     => 'root',
  provider => 'shell',
}

exec { 'add X-Served-By header':
  command  => 'sed -i "42 a\ \tadd_header X-Served-By \$hostname;\n" /etc/nginx/sites-enabled/default',
  user     => 'root',
  provider => 'shell',
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
