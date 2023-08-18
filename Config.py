import subprocess
class Config:
  SEARCHKEY = "Use of AI ML in breast cancer therapy, Artificial Intelligence and Machine Learning"
  NUMRECORDS = 50
  
  # Install the modules whic are missing
  def install_module(module_name):
    subprocess.check_call(["pip", "install", module_name])