# install puppet-lint using puppet

package { 'puppet-loint':
  ensure   => '2.1.0',
  provider => 'gem',
}
