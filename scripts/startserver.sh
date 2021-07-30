  
#!/bin/bash

sudo systemctl restart supervisor
 sudo systemctl enable supervisor
 sudo supervisorctl restart gunicorn
  sudo supervisorctl status gunicorn
 sudo nginx -t
 sudo service nginx restart