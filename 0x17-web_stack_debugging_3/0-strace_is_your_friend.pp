# fix the server bug

exec { 'update the settings file':
        provider => 'shell',
        command  => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}

exec { 'restart apache2 service':
        provider => 'shell',
        command  => 'service apache2 restart',
}
