import subprocess

def unzip(downloadDir,dataDir):
    return subprocess.call(f'python cnpj.py {downloadDir} sqlite {dataDir} --dir', shell=True)
