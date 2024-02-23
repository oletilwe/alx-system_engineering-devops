# Kill the process named killmenow
exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => '/bin:/usr/bin',
}
