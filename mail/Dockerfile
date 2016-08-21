FROM debian:jessie

RUN apt-get update && apt-get install -y --no-install-recommends \
        mailutils \
        ssmtp \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

COPY ssmtp_custom.conf /etc/ssmtp/ssmtp_custom.conf
COPY entrypoint.sh /usr/local/bin/
ENTRYPOINT ["entrypoint.sh"]
