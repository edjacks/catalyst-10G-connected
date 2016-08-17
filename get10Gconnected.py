#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Retrieve information on any TenGig Ethernet interfaces.

Log into a seed switch, find any CDP neighbors, and subsequently
list all connected TenGigabit Ethernet interfaces that are found
on those neighboring switches.

This was used to look for any Cisco C3850 switches that had any
NM-2-10G modules that included both 2x 1G and 2x 10G ports in
use.

20160817 - edjacks@cisco.com

"""

import sys
import re

sys.path.append('/cygdrive/z/edjacks/files/<removed>/scripts/python-modules')

import thd

seed_switch = 'switch.<removed>.com'

def jumphost_login(user, password):
    """Log into the jump host

    """
    c = thd.open_jumphost(user, password)
    i_prompt = thd.get_prompt(c)

    return c, i_prompt


def main():
    """Main function.

    1) Get credentials from user
    2) Log into jump host
    3) Log into seed switch
    4) Find CDP neighbors
    5) Log into each CDP neighbor
    6) Generate list of connected 10G interfaces on neighbor
    7) Save data to neighbor specific file

    """
    # get credentials
    iu, ip, lu, lp = thd.get_credentials()

    # login to jump host
    c, i_prompt = jumphost_login(iu, ip)

    # login to cpc1agm01
    prompt = thd.netlogin(c, lu, lp, seed_switch)

    # get list of CDP neighbors
    sites = set()
    output = thd.send_command(c, prompt, 'show cdp neig detail')
    for line in output.splitlines():
        m = re.search('^Device ID: (.*)', line)
        if m:
            sites.add(m.groups()[0])

    null_output = thd.send_command(c, i_prompt, 'exit')

    # parse through CDP neighbors
    for site in sites:

        # get inventory of Ten Gig
        prompt = thd.netlogin(c, lu, lp, site)
        output = thd.send_command(c, prompt, 'show int status | inc Te.*connected')
        with open('{}.output'.format(site), 'w') as outfile:
            outfile.write(output)

        null_output = thd.send_command(c, i_prompt, 'exit')


if __name__ == '__main__':
    main()
