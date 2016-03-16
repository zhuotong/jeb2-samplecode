# -*- coding: utf-8 -*-

"""
Sample client script for PNF Software's JEB2.

More samples are available on our website and within the scripts/ folder.

Refer to SCRIPTS.TXT for more information.
"""

from com.pnfsoftware.jeb.client.api import IScript


class JEB2SampleScript(IScript):
  def run(self, ctx):
    # For non-ASCII characters, remember to specify the encoding in the script header (here, UTF-8),
    # and do not forget to prefix all Unicode strings with "u", whether they're encoded (using \u or else) or not
    print('~~~\n' + u'Hello, ?????, ??, ?????!\n' + 'This line was generated by a JEB2 Python script\n~~~')
