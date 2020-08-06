# Installing Nginx on Server, Initializing index page and creating redirection

exec { '_installing_Nginx':
     command => 'sudo apt-get install nginx -y',
     path    => ['/usr/bin', '/bin'],
}

file { '/var/www/html/index.html':
     content => 'Holberton School',
}

file_line { 'title':
  ensure   => present,
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  multiple => true
}

exec { 'stoping_Nginx':
  require => Exec['_installing_Nginx'],
  command => 'sudo service nginx stop',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}

exec { 'starting_Nginx':
  require => Exec['stoping_Nginx'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}