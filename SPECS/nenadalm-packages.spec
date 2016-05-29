Name: nenadalm-packages
Version: 0.0.2
Release: 1%{?dist}
Summary: Config

License: MIT

BuildArch: noarch
Requires: nenadalm-config,phpfarm,dex-autostart,community-mysql-server,postgresql-server,rabbitmq-server,awesome,vim,gvim,terminator,firefox,git,evince,thunderbird

%description
Installs all the packages

%files

%changelog
* Sun May 29 2016 Miloslav Nenadal <nenadalm@gmail.com> 0.0.1-1
- Initial packaging
* Sun May 29 2016 Miloslav Nenadal <nenadalm@gmail.com> 0.0.2-1
- Add phpfarm, dex-autostart

