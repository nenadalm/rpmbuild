Name: nenadalm-config
Version: 0.0.1
Release: 1%{?dist}
Summary: Config

License: MIT
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

%description
Config

%prep
%autosetup

%install
cp -R %{_builddir}/%{name}-%{version} %{buildroot}/%{name}

%postun
if [[ -h "/opt/phpfarm/custom/options.sh" && $(readlink "/opt/phpfarm/custom/options.sh") = "/nenadalm-config/phpfarm/opt/phpfarm/custom/options.sh" ]]; then
    rm -f "/opt/phpfarm/custom/options.sh"
fi

%triggerin -- phpfarm
if [[ ! -h "/opt/phpfarm/custom/options.sh" || ! $(readlink "/opt/phpfarm/custom/options.sh") = "/nenadalm-config/phpfarm/opt/phpfarm/custom/options.sh" ]]; then
    mkdir -p "/opt/phpfarm/custom"
    if [[ -e "/opt/phpfarm/custom/options.sh" ]]; then
        mv -f "/opt/phpfarm/custom/options.sh" "/opt/phpfarm/custom/options.sh.orig"
    fi
    ln -s "/nenadalm-config/phpfarm/opt/phpfarm/custom/options.sh" "/opt/phpfarm/custom/options.sh"
fi

%triggerun -- phpfarm
if [[ $1 -eq 0 && $2 -gt 0 && -e "/opt/phpfarm/custom/options.sh.orig" ]]; then
    mv -f "/opt/phpfarm/custom/options.sh.orig" "/opt/phpfarm/custom/options.sh"
fi

%triggerpostun -- phpfarm
if [[ $2 -eq 0 ]]; then
    rm -f "/opt/phpfarm/custom/options.sh.rpmsave" "/opt/phpfacrm/custom/options.sh.orig"
fi
if [[ -e "/opt/phpfarm/custom/options.sh.rpmnew" ]]; then
    mv "/opt/phpfarm/custom/otpions.sh.rpmnew" "/opt/phpfarm/custom/options.sh.orig"
fi

%files
/%{name}

