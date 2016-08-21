FROM scaleway/ubuntu:amd64-xenial

RUN /usr/local/sbin/builder-enter

# Install packages
RUN sed -i '/mirror.scaleway/s/^/#/' /etc/apt/sources.list \
 && apt-get -q update                   \
 && apt-get --force-yes -y -qq upgrade  \
 && apt-get --force-yes install -y -q   \
    apparmor            \
    arping              \
    aufs-tools          \
    btrfs-tools         \
    bridge-utils                    \
    cgroup-lite         \
    git             \
    ifupdown            \
    kmod                \
    lxc             \
    python-setuptools               \
    vlan                \
    mailutils \
    ssmtp \
    && apt-get clean \

COPY ssmtp_custom.conf /etc/ssmtp/ssmtp_custom.conf
COPY entrypoint.sh /usr/local/bin/
ENTRYPOINT ["sh","/usr/local/bin/entrypoint.sh"]
