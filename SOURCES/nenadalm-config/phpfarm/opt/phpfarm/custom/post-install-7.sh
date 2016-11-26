#/usr/bin/env bash

set -eu

INSTALLATION_DIR="$(readlink -f $(dirname $0))/.."

cp "${INSTALLATION_DIR}/inst/php-${1}/etc/php.ini" "${INSTALLATION_DIR}/inst/php-${1}/lib/"
pecl install xdebug

