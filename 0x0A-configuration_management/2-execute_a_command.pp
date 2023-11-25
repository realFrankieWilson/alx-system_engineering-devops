# Using Puppet to create a manifest that kills a process named killmenow.

exec { 'pkill_process':
    command  => 'pkill -9 killmenow',
    provider => 'shell',
}
