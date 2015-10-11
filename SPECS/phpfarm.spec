Name: phpfarm
Version: 0.2.0
Release: 1%{?dist}
Summary: Set of scripts to install a dozen of PHP versions in parallel on a single system

License: AGPLv3+
URL: https://github.com/fpoirotte/phpfarm
Source0: https://github.com/fpoirotte/phpfarm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
Requires(pre): shadow-utils
Requires: make,wget,gcc,mod_fcgid,tar,bzip2,autoconf,libxml2-devel,libcurl,postgresql-devel,openssl-devel,libssh2-devel,openldap-devel,turbojpeg-devel,libjpeg-turbo-devel,libpng-devel,libicu-devel,libmcrypt-devel,ImageMagick-devel,librabbitmq-devel,gcc-c++,glibc-headers,binutils

%global __requires_exclude /bin/php$

%description
Set of scripts to install a dozen of PHP versions in parallel on a single system

%pre
getent group phpfarm > /dev/null || groupadd -r phpfarm
getent passwd phpfarm > /dev/null || useradd -r -g phpfarm -s /sbin/nologin phpfarm

%prep
%autosetup

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt
cp -R %{_builddir}/%{name}-%{version} %{buildroot}/opt/phpfarm

%files
%attr(-, phpfarm, phpfarm) /opt/phpfarm/

%changelog
* Sat Oct 10 2015 Miloslav Nenadal <nenadalm@gmail.com> 0.2.0
- Initial packaging

