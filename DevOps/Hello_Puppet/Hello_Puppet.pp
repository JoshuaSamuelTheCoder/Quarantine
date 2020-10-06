node default {
  file { 'var/save/puppet_hello/hellopuppet.txt',
          path => 'var/save/puppet_hello/hellopuppet.txt',
          content => "Hello Puppet",
  }
}
