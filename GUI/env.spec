# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['env', 'PTVSD_LAUNCHER_PORT=58784', '/Library/Frameworks/Python.framework/Versions/3.7/bin/python3', '/Users/Cristian/.vscode/extensions/ms-python.python-2020.2.64397/pythonFiles/lib/python/new_ptvsd/wheels/ptvsd/launcher', '/Users/Cristian/Google Drive/Dropbox/Code/learning_python/Matplotlib/matplotlib.py'],
             pathex=['/Users/Cristian/Google Drive/Dropbox/Code/learning_python/GUI'],
             binaries=[],
             datas=[],
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
          name='env',
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
               upx_exclude=[],
               name='env')
