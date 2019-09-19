# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['한상우_빅데이터저장관리_프로그램.py'],
             pathex=['C:\\python_workspace\\04_Application\\02_Distributed_Repository\\dist'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='한상우_빅데이터저장관리_프로그램',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='37f60f238e60467e8b9_JRs_icon.ico')
