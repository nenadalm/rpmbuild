From fedora:24

RUN dnf install -y rpm-build shunit2

ADD . /root/rpmbuild
CMD usr/share/shunit2/shunit2 /root/rpmbuild/TESTS/nenadalm-config/phpfarm && /usr/share/shunit2/shunit2 /root/rpmbuild/TESTS/nenadalm-config/postgresql-server

