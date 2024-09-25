#! /usr/bin/env python3
'''
    AAS
    Copyright (C) 2024 Universitaetsklinikum Bonn AoeR

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import argparse
import sys
import logging
from armis import ArmisCloud
from helper.filesystem import get_config_directory
from helper.config import get_config_from_file
from helper.logging import setup_console_logger

PROGRAM_NAME = 'AAS - Get Devices in Site'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'Get all devices of a specific site'
DEFAULT_CONFIG_FILE = get_config_directory() / 'sample.cfg'

def setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('site')
    parser.add_argument('-c', '--config', default=DEFAULT_CONFIG_FILE, help='config file [{}]'.format(DEFAULT_CONFIG_FILE))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-L', '--log_level', default='INFO', help='set log level [INFO]: DEBUG, INFO, WARNING, ERROR')
    return parser.parse_args()


if __name__ == '__main__':
    args = setup_argparser()
    setup_console_logger(args.log_level)
    config = get_config_from_file(args.config)
    logging.info("connect to %s", config['armis-server']['url'])
    
    armis_conection = ArmisCloud(api_secret_key=config['armis-server']['APIkey'],tenant_hostname=config['armis-server']['url'])
    
    devices = armis_conection.get_devices(asq='in:devices timeFrame:"{}" site:"{}"'.format(config['query-defaults']['timeFrame'], args.site))
    for device in devices:
        print('{} - {}'.format(device['names'], device['macAddress']))

    sys.exit(0)
