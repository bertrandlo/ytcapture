# coding=utf-8

import PyInstaller.config

PyInstaller.config.CONF['distpath'] = "b:\\"

block_cipher = None


a = Analysis(['ytcapture.py'],
             pathex=['C:\\Users\\brt\\PycharmProjects\\ytcapture'],
             binaries=[],
             datas=[('ffmpeg.exe', '.'),
                    ('resources/', './resources/'),
                    ('settings.json', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          icon='.\\resources\\box-multi-size.ico',
          name='ytcapture',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ytcapture')
