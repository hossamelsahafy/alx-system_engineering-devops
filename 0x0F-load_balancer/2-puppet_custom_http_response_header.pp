# creating a custom HTTP header response, but with Puppet
node 'web-01', 'web-02' {
  class { 'nginx': }

  nginx::resource::server { 'default':
    listen_port => 80,
    use_default_location => false,
    locations => {
      '/' => {
        location => '/',
        location_custom_cfg => { 'add_header' => 'X-Served-By $hostname' },
      },
    },
  }
}

