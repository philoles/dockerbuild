docker run -i -e TLS=YES -e mailhub=smtp.gmail.com:587 -e AuthUser=nine910ten@gmail.com -e AuthPass=song2656847 mail:test11 sh -c 'echo "test email" | mail -s "test email" 1062860666@qq.com'

docker run -i -e TLS=YES -e mailhub=smtp.gmail.com:587 -e AuthUser=nine910ten@gmail.com -e AuthPass=song2656847 mail:test11 cat /var/log/mail.log


docker run -i -e TLS=YES -e mailhub=smtp.gmail.com:587 -e AuthUser=nine910ten@gmail.com -e AuthPass=song2656847 mail:test14 /bin/bash

docker run -i -v /c/Users/ssmtp.conf:/etc/ssmtp/ssmtp.conf debian:jessie_mail /bin/bash
