#todo: remove empty dirs when package gets removed

Name: nenadalm-config
Version: 0.0.2
Release: 1%{?dist}
Summary: Config

License: MIT
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: findutils

%description
Config

%prep
%autosetup

%install
mkdir -p %{buildroot}/usr/bin
cp -R %{_builddir}/%{name}-%{version}/_bin/* %{buildroot}/usr/bin
rm -rf %{_builddir}/%{name}-%{version}/_bin
cp -R %{_builddir}/%{name}-%{version} %{buildroot}/%{name}

%preun
for file in $(find '/nenadalm-config' -mindepth 1 -maxdepth 1 -type d); do
    package=$(basename "${file}")
    for package_config_file in $(find "${file}" -type f); do
        target_config_file="${package_config_file#/nenadalm-config/${package}}"
        if [[ -h "${target_config_file}" && $(readlink "${target_config_file}" = "${package_config_file}") ]]; then
            rm -f "${target_config_file}"
        fi
    done
done

### START GENERATED_SECTION
# postgresql-server
%triggerin -- postgresql-server
nc-triggerin '/nenadalm-config/postgresql-server'

%triggerun -- postgresql-server
nc-triggerun "${1}" "${2}" '/nenadalm-config/postgresql-server'

%triggerpostun -- postgresql-server
nc-triggerpostun "${1}" "${2}" '/nenadalm-config/postgresql-server'

# phpfarm
%triggerin -- phpfarm
nc-triggerin '/nenadalm-config/phpfarm'

%triggerun -- phpfarm
nc-triggerun "${1}" "${2}" '/nenadalm-config/phpfarm'

%triggerpostun -- phpfarm
nc-triggerpostun "${1}" "${2}" '/nenadalm-config/phpfarm'

### END GENERATED_SECTION

%files
/%{name}
%attr(755,-,-) /usr/bin/nc-triggerin
%attr(755,-,-) /usr/bin/nc-triggerun
%attr(755,-,-) /usr/bin/nc-triggerpostun

