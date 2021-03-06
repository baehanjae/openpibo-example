import time
import os
import sys

# 상위 디렉토리 추가 (for utils.config)
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from utils.config import Config as cfg

# openpibo 라이브러리 경로 추가
sys.path.append(cfg.OPENPIBO_PATH + '/lib')
from audio.audiolib import cAudio

def tts_f():
  obj = cAudio()
  obj.play(filename=cfg.TESTDATA_PATH+"/test.mp3", out='local', volume=-2000)
  time.sleep(5)
  obj.stop()

if __name__ == "__main__":
  tts_f()
