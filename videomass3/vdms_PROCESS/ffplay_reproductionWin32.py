# -*- coding: UTF-8 -*-

#########################################################
# Name: ffplay_reproduction.py 
# Porpose: simple media player with x-window-terminal-emulator for Ms Windows
# Compatibility: Python3, wxPython Phoenix
# Author: Gianluca Pernigoto <jeanlucperni@gmail.com>
# Copyright: (c) 2018/2019 Gianluca Pernigoto <jeanlucperni@gmail.com>
# license: GPL3
# Rev: Dec.27.2018, Sept.05.2019
#########################################################

# This file is part of Videomass.

#    Videomass is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    Videomass is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Videomass.  If not, see <http://www.gnu.org/licenses/>.

#########################################################

import wx
import subprocess
import time
from threading import Thread
from videomass3.vdms_SYS.os_interaction import copy_restore # if copy fiile log
from videomass3.vdms_IO.make_filelog import write_log # write initial log

########################################################################
# get data from bootstrap
get = wx.GetApp()
DIRconf = get.DIRconf # path to the configuration directory
PATH_log = get.path_log # if not 'none' save the log in other place
#########################################################################

def Messages(msg):
    """
    Receive error messages from Play(Thread) via wxCallafter
    """

    wx.MessageBox("FFplay Error:  %s" % (msg), 
                      "Videomass: FFplay", 
                      wx.ICON_ERROR
                      )
#########################################################################

class Play(Thread):
    """
    Run a separate process thread for media reproduction with a called 
    at ffplay witch need x-window-terminal-emulator for show files streaming.
    
    """
    def __init__(self, filepath, timeseq, ffplay_link, 
                 param, loglevel_type, OS):
        """
        The self.loglevel_type has 'error -stats' (see conf. file)
        then use error only with this class.
        
        """
        Thread.__init__(self)
        ''' constructor'''

        self.filename = filepath # file name selected
        self.ffplay = ffplay_link, # command process
        self.loglevel_type = loglevel_type # not used (used error)
        self.time_seq = timeseq # seeking
        self.param = param # additional parameters if present
        self.OS = OS # tipo di sistema operativo
        self.logf = "%s/log/%s" %(DIRconf, 'Videomass_FFplay.log')
        
        write_log('Videomass_FFplay.log', "%s/log" % DIRconf) 
        # set initial file LOG

        self.start() # start the thread (va in self.run())
        
    #----------------------------------------------------------------#
    def run(self):
        """
        NOTE 1: the loglevel is set on 'error'. Do not use 
               'self.loglevel_type' because -stats  option do not work.
    
        NOTE 2: The p.returncode always returns 0 value even when there 
                is an error. But since ffplay always returns the error 
                on the PIPE of the stderr, then I use the 'error' 
                variable of p.communicate ()

        NOTE 3: for subprocess.STARTUPINFO() 
                < Windows: https://stackoverflow.com/questions/1813872/running-
                a-process-in-pythonw-with-popen-without-a-console?lq=1>
        """
        #time.sleep(.5)
        loglevel_type = 'error'
        command = '%s %s -i "%s" %s -loglevel %s' % (self.ffplay,
                                                 self.time_seq,
                                                 self.filename,
                                                 self.param,
                                                 loglevel_type,
                                                 )
        self.logWrite(command)
        
        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            p = subprocess.Popen(command,
                                stderr=subprocess.PIPE,
                                universal_newlines=True,
                                startupinfo=startupinfo,
                                )
            error =  p.communicate()
        
        except OSError as err_0:
            pyerror = ("%s: 'ffplay.exe'") % (err_0)
            wx.CallAfter(Messages, pyerror)
            self.logError(pyerror) # append log error
            self.pathLog() # log in other place?
            return
        
        else:
            if error[1]:
                wx.CallAfter(Messages, error[1])
                self.logError(error[1]) # append log error
                self.pathLog() # log in other place?
                return
        
        self.pathLog() # log in other place?
        
    #----------------------------------------------------------------#    
    def logWrite(self, cmd):
        """
        write ffmpeg command log
        
        """
        with open(self.logf, "a") as log:
            log.write("%s\n\n" % (cmd))
            
    #----------------------------------------------------------------# 
    def logError(self, error):
        """
        write ffmpeg volumedected errors
        
        """
        print(error)
        with open(self.logf,"a") as logerr:
            logerr.write("[FFMPEG] FFplay "
                         "ERRORS:\n%s\n\n" % (error))
    #----------------------------------------------------------------#
    def pathLog(self):
        """
        if user want file log in a specified path
        
        """
        if not 'none' in PATH_log: 
            copy_restore(self.logf, "%s/%s" % (PATH_log, 
                                               'Videomass_FFplay.log'))
        
