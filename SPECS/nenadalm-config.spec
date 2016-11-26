Name: nenadalm-config
Version: 0.0.4
Release: 1%{?dist}
Summary: Config

License: MIT
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: findutils

%description
Config

%prep
%setup -n %{name}

%install
mkdir -p %{buildroot}/usr/bin
cp -R %{_builddir}/%{name}/_bin/* %{buildroot}/usr/bin
rm -rf %{_builddir}/%{name}/_bin
cp -R %{_builddir}/%{name} %{buildroot}/%{name}

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

# awesome
%triggerin -- awesome
nc-triggerin '/nenadalm-config/awesome'

%triggerun -- awesome
nc-triggerun "${1}" "${2}" '/nenadalm-config/awesome'

%triggerpostun -- awesome
nc-triggerpostun "${1}" "${2}" '/nenadalm-config/awesome'

# vim-common
%triggerin -- vim-common
nc-triggerin '/nenadalm-config/vim-common'

%triggerun -- vim-common
nc-triggerun "${1}" "${2}" '/nenadalm-config/vim-common'

%triggerpostun -- vim-common
nc-triggerpostun "${1}" "${2}" '/nenadalm-config/vim-common'

# bash
%triggerin -- bash
nc-triggerin '/nenadalm-config/bash'

%triggerun -- bash
nc-triggerun "${1}" "${2}" '/nenadalm-config/bash'

%triggerpostun -- bash
nc-triggerpostun "${1}" "${2}" '/nenadalm-config/bash'

### END GENERATED_SECTION

%files
/%{name}
%attr(755,-,-) /usr/bin/nc-triggerin
%attr(755,-,-) /usr/bin/nc-triggerun
%attr(755,-,-) /usr/bin/nc-triggerpostun

