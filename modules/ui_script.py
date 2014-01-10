# Copyright (C) 2013 Kristoffer Gronlund <kgronlund@suse.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

import command
import scripts

from msg import err_buf


class Script(command.UI):
    '''
    Cluster scripts can perform cluster-wide configuration,
    validation and management. See the `list` command for
    an overview of available scripts.

    The script UI is a thin veneer over the scripts
    backend module.
    '''
    name = "script"

    def do_list(self, context):
        '''
        List available scripts.
        '''
        for name in scripts.list_scripts():
            main = scripts.load_script(name)
            print "%-16s %s" % (name, main.get('name', ''))

    def do_verify(self, context, name):
        '''
        Verify the given script.
        '''
        if scripts.verify(name):
            err_buf.ok(name)

    def do_describe(self, context, name):
        '''
        Describe the given script.
        '''
        return scripts.describe(name)

    def do_run(self, context, name, *args):
        '''
        Run the given script.
        '''
        nodes = None
        dry_run = False
        while len(args):
            if args[0] == '--nodes':
                nodes = args[1].replace(',', ' ').split()
                args = args[2:]
            elif args[0].startswith('--nodes='):
                nodes = args[0][9:].replace(',', ' ').split()
                args = args[1:]
            elif args[0] == '--dry-run':
                dry_run = True
                args = args[1:]
            else:
                break
        return scripts.run(nodes, name, args, dry_run=dry_run)
