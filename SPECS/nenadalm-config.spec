#todo: remove empty dirs when package gets removed

Name: nenadalm-config
Version: 0.0.1
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

%triggerin -- phpfarm
file='/nenadalm-config/phpfarm'
package=$(basename "${file}")
for package_config_file in $(find "${file}" -type f); do
    target_config_file="${package_config_file#/nenadalm-config/${package}}"
    if [[ ! -h "${target_config_file}" || ! $(readlink "${target_config_file}") = "${package_config_file}" ]]; then
        existing_dir=$(dirname "${target_config_file}")
        while [[ ! -e "${existing_dir}" ]]; do
            existing_dir="${existing_dir%/*}"
        done
        mkdir -p $(dirname "${target_config_file}")
        if [[ "${existing_dir}" != $(dirname "${target_config_file}") ]]; then
            chown -R $(stat -c %U "${existing_dir}"):$(stat -c %G "${existing_dir}") "${existing_dir}"
        fi
        if [[ -e "${target_config_file}" ]]; then
            mv -f "${target_config_file}" "${target_config_file}.orig"
        fi
        ln -s "${package_config_file}" "${target_config_file}"
    fi
done

%triggerun -- phpfarm
if [[ $1 -eq 0 && $2 -gt 0 ]]; then
    file='/nenadalm-config/phpfarm'
    package=$(basename "${file}")
    for package_config_file in $(find "${file}" -type f); do
        target_config_file="${package_config_file#/nenadalm-config/${package}}"
        if [[ -e "${target_config_file}.orig" ]]; then
            mv -f "${target_config_file}.orig" "${target_config_file}"
        fi
    done
fi

%triggerpostun -- phpfarm
file='/nenadalm-config/phpfarm'
package=$(basename "${file}")
for package_config_file in $(find "${file}" -type f); do
    target_config_file="${package_config_file#/nenadalm-config/${package}}"
    if [[ $2 -eq 0 ]]; then
        rm -f "${target_config_file}.rpmsave" "${target_config_file}.orig"
    fi
    if [[ -e "${target_config_file}.rpmnew" ]]; then
        mv "${target_config_file}.rpmnew" "${target_config_file}.orig"
    fi
done

%files
/%{name}

