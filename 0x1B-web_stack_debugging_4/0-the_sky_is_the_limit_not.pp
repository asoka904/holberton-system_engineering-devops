# Increase limit
exec { 'Increase_workers':
  command  => "sed -i 's/worker_processes 4;/worker_processes 100;/g' /etc/nginx/nginx.conf && service nginx restart",
  provider => 'shell',
}
