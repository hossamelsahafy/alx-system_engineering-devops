class { 'nginx': }
nginx::resource::server { 'hello':
    listen_port          => 80,
    www_root             => '/var/www/hello',
    index_files          => ['index.html'],
    location_cfg_append  => {
        return => '301 https://emaple.com',
    },
}
file { '/var/www/hello/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Nginx::Resource::server['hello']
}
service { 'nginx:
ensure    => running,
enable    => True,
subscribe => Nginx::Resource::Server['hello']
}