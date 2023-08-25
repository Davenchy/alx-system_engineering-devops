# kill a process called killmenow using pkill

exec { 'kill_killmenow_process':
  command  => 'pkill killmenow',
  provider => 'shell',
}
