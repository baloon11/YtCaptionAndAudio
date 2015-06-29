# -*- coding: utf-8 -*-
import sys
import pafy

video = pafy.new(sys.argv[1])
bestaudio = video.getbestaudio()
bestaudio.download()


# import pafy
# url = "http://www.youtube.com/watch?v=OTEMuea9nx4"
# video = pafy.new(url)
# bestaudio = video.getbestaudio()
# bestaudio.download()