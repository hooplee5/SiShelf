#maya終了時にSiShelfの状態を記録
import SiShelf.shelf
SiShelf.shelf.make_quit_app_job()
#UI構築後にSiShelfを復元
import maya.utils
maya.utils.executeDeferred(SiShelf.shelf.restoration_ui)
