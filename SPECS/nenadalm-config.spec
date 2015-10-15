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
file='/nenadalm-config/phpfarm'
package=$(basename "${file}")
for package_config_file in $(find "${file}" -type f); do
    target_config_file="${package_config_file#/nenadalm-config/${package}}"
    if [[ ! -h "${target_config_file}" || ! $(readlink "${target_config_file}") = "${package_config_file}" ]]; then
        mkdir -p $(dirname "${target_config_file}")
        if [[ -e "${target_config_file}" ]]; then
            mv -f "${target_config_file}" "${target_config_file}.orig"
        fi
        ln -s "${package_config_file}" "${target_config_file}"
    fi
done

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

