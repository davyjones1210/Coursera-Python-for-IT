class ntp {
  package { 'ntp':
    ensure => latest,
  } 
  file { '/etc/ntp.conf':
    source => '/home/davy_jones/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify  => Service['ntp'],
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
    require => File['/etc/ntp.conf'],
  }
}

include ntp