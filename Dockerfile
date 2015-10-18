From fedora:22

RUN dnf install -y rpm-build shunit2

CMD cp -R /mnt/rpmbuild /root && /usr/share/shunit2/shunit2 /root/rpmbuild/TESTS/nenadalm-config/phpfarm && /usr/share/shunit2/shunit2 /root/rpmbuild/TESTS/nenadalm-config/postgresql-server

