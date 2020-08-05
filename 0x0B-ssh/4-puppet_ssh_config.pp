# sets up the client SSH configuration file to connect to a server
# without typing a password.

file_line { 'using_private_key':
      path => '/etc/ssh/ssh_config',
      line => '    IdentityFile ~/.ssh/holberton',
}

file_line { 'no_passwrd_use':
      path => '/etc/ssh/ssh_config',
      line => '    PasswordAuthentication no',
}