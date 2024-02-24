#configuration Using pupet
file {'/home/hossam/.ssh/config':
    ensure  => 'file',
    mode    => '0600',
    content => "host *\n IdentityFile ~/.ssh/school\n passwordAuthentication no"
}
