Name: phantomjs
Version: 2.1.1
Release: 1%{?dist}
Summary: Headless browser

License: BSD
URL: http://phantomjs.org/
Source0: https://bitbucket.org/ariya/phantomjs/downloads/%{name}-%{version}-linux-x86_64.tar.bz2#/%{name}-%{version}.tar.bz2

BuildArch: x86_64
Requires: gcc gcc-c++ make flex bison gperf ruby openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel libpng-devel libjpeg-devel python

%description
Headless browser

%prep
%setup -n %{name}-%{version}-linux-x86_64

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt
cp -R %{_builddir}/%{name}-%{version}-linux-x86_64 %{buildroot}/opt/%{name}

%post
cat > /etc/profile.d/phantomjs.sh <<EOF
export PATH=\$PATH:/opt/phantomjs/bin
EOF

%postun
if [[ $1 -eq 0 ]]; then
    rm /etc/profile.d/phantomjs.sh
fi

%files
/opt/%{name}

%changelog
* Sun Nov 06 2016 Miloslav Nenadal <nenadalm@gmail.com> 2.1.1-1
- Initial packaging

