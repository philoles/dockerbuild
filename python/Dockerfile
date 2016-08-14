FROM python:3.5

RUN apt-get update && apt-get install -y --no-install-recommends \
        xvfb \
        libgtk-3-0 \
        # install iceweasel to install dependencies for firefox 
        iceweasel \
    && apt-get remove iceweasel -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/* \
    && wget -P /usr/local http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/46.0.1/linux-x86_64/en-US/firefox-46.0.1.tar.bz2 \
    && tar xvjf /usr/local/firefox-46.0.1.tar.bz2 -C /usr/local \
    && ln -sf /usr/local/firefox/firefox /usr/bin/firefox \
    && rm /usr/local/firefox-46.0.1.tar.bz2 \
    && pip install selenium \
        requests \
        xvfbwrapper


