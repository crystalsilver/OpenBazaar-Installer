# -*- mode: python -*-

block_cipher = None


a = Analysis(['./OpenBazaar-Server/openbazaard.py'],
             pathex=['./OpenBazaar-Server'],
             binaries=None,
             datas=None,
             hiddenimports=['zmq', 'cryptography', 'cffi', 'packaging'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
a.datas += [('ob.cfg', 'ob.cfg', 'DATA'),('bitcointools/english.txt','env/bitcointools/english.txt','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='openbazaard',
          debug=False,
          strip=False,
          upx=True,
          console=True )